import json
from collections import defaultdict

from fastapi import APIRouter

from codstorage.config import config

DB = defaultdict(set)

router = APIRouter()


@router.get('/{name}/repos')
async def getrepos(name: str):
    path = config.CODSTORAGE_REPOS_DIR / name

    repos = {}

    for file in path.glob('*.json'):
        with open(file, 'rt') as f:
            repos[file.stem] = json.load(f)

    return repos
