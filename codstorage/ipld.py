import io
import json
import base64
from typing import IO
from functools import cache

import httpx
from git import Repo


class IPLD(object):
    def __init__(self, repo: Repo, url: str = None):
        super(IPLD, self).__init__()
        self.repo = repo
        self.url = url or 'http://localhost:5001/api/v0'
        self.client = httpx.Client(base_url=self.url)

    def _add(self, data: IO) -> str:
        file = {'file': data}
        response = self.client.post('/add', files=file)
        response = response.json()
        return {'/': response['Hash']}

    def _put(self, data: dict) -> str:
        data = json.dumps(data).encode()
        data = io.BytesIO(data)
        file = {'file': data}
        response = self.client.post('/dag/put', files=file)
        response = response.json()
        return response['Cid']

    @cache
    def _send_blob(self, blob: object) -> dict:
        data = blob.data_stream.read()
        data = io.BytesIO(data)
        return self._add(data)

    def _send_tree(self, tree: object) -> dict:
        if tree.type == 'blob':
            return self._send_blob(tree)
        data = {b.name: self._send_blob(b) for b in tree.blobs}
        return self._put(data)

    def _send_commit(self, commit: object) -> dict:
        node = {
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
            'tree': {t.name: self._send_tree(t) for t in commit.tree},
            'message': commit.message,
        }
        return self._put(node)

    def _send_branch(self, branch: object) -> dict:
        commits = self.repo.iter_commits(branch.name)
        commits = {c.hexsha: self._send_commit(c) for c in commits}
        return self._put(commits)

    def send(self) -> dict:
        branches = {b.name: self._send_branch(b) for b in self.repo.branches}
        branches = {'blobs': branches}
        return self._put(branches)
