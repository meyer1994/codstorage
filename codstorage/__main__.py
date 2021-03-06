import asyncio
from pathlib import Path
from argparse import ArgumentParser

from git import Repo
from pfluent import Runner

from codstorage.db import db
from codstorage.config import config
from codstorage.utils.ipld import IPLD

parser = ArgumentParser()
parser.add_argument('path', type=Path)


async def run_ipfs(path: str):
    result = Runner('ipfs')\
        .arg('add')\
        .arg('--recursive')\
        .arg('--quieter')\
        .arg('--pin', path)\
        .arg('--api', '/ip4/127.0.0.1/tcp/5001')\
        .run(check=True, capture_output=True, text=True)
    return result.stdout.strip()


async def run_ipld(path: str):
    ipld = Repo(path)
    ipld = IPLD(ipld)
    return await ipld.send()


async def run_ceramic(path: str):
    pass


async def main():
    args = parser.parse_args()

    ipfs = run_ipfs(args.path)
    ipld = run_ipld(args.path)
    conn = db.connect()

    ipfs, ipld, _ = await asyncio.gather(ipfs, ipld, conn)

    print()
    print(f'IPLD: {ipld}')
    print(f'IPFS: {ipfs}')
    print()

    query = 'INSERT INTO repos(ipfs, ipld, likes) VALUES (:ipfs, :ipld, 0)'
    values = {'ipfs': ipfs, 'ipld': ipld}
    await db.execute(query, values)


asyncio.run(main())
