import io
import json
import base64
import asyncio
from typing import IO
from functools import cache

import httpx
from git import Repo


class IPLD(object):
    def __init__(self, repo: Repo, url: str = None):
        super(IPLD, self).__init__()
        self.repo = repo
        self.url = url or 'http://localhost:5001/api/v0'
        self.client = httpx.AsyncClient(base_url=self.url)

    async def _add(self, data: IO) -> str:
        file = {'file': data}
        response = await self.client.post('/add', files=file)
        response = response.json()
        return {'/': response['Hash']}

    async def _put(self, data: dict) -> str:
        data = json.dumps(data).encode()
        data = io.BytesIO(data)
        file = {'file': data}
        response = await self.client.post('/dag/put', files=file)
        response = response.json()
        return response['Cid']

    async def _send_blob(self, blob: object) -> dict:
        data = blob.data_stream.read()
        data = io.BytesIO(data)
        return await self._add(data)

    async def _send_tree(self, tree: object) -> dict:
        if tree.type == 'blob':
            return await self._send_blob(tree)

        filesname = [f.name for f in tree.blobs]
        filessent = (self._send_blob(b) for b in tree.blobs)
        filessent = await asyncio.gather(*filessent)
        files = {n: t for n, t in zip(filesname, filessent)}

        treename = [t.name for t in tree.trees]
        treesent = (self._send_tree(t) for t in tree.trees)
        treesent = await asyncio.gather(*treesent)
        trees = {n: t for n, t in zip(treename, treesent)}

        # files = {b.name: self._send_blob(b) for b in tree.blobs}
        # trees = {t.name: self._send_tree(t) for t in tree.trees}
        return await self._put(trees | files)

    async def _commit(self, commit: object) -> dict:
        # tree = {t.name: self._send_tree(t) for t in commit.tree}
        treename = [t.name for t in commit.tree]
        treesent = (self._send_tree(t) for t in commit.tree)
        treesent = await asyncio.gather(*treesent)
        tree = {n: t for n, t in zip(treename, treesent)}

        return {
            'hash': commit.hexsha,
            'author': {
                'date': commit.authored_datetime.isoformat(),
                'email': commit.author.email,
                'name': commit.author.name,
            },
            'committer': {
                'date': commit.committed_datetime.isoformat(),
                'email': commit.committer.email,
                'name': commit.committer.name,
            },
            'tree': await self._put(tree),
            'message': commit.message,
        }

    async def _send_branch(self, branch: object) -> dict:
        commits = self.repo.iter_commits(branch.name)
        commits = (self._commit(c) for c in commits)
        commits = await asyncio.gather(*commits)
        commits = sorted(commits, key=lambda i: i['committer']['date'])
        commits = reversed(commits)
        commits = list(commits)
        return await self._put(commits)

    async def send(self) -> str:
        branchname = [b.name for b in self.repo.branches]
        branchsent = (self._send_branch(b) for b in self.repo.branches)
        branchsent = await asyncio.gather(*branchsent)
        branches = {n: t for n, t in zip(branchname, branchsent)}
        # branches = {b.name: self._send_branch(b) for b in self.repo.branches}
        data = await self._put(branches)
        return data['/']
