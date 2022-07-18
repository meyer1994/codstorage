import logging
from pathlib import Path
from dataclasses import dataclass

from fastapi import APIRouter, Request, Depends
from fastapi.responses import StreamingResponse

from codstorage.utils import magic
from codstorage.config import config
from codstorage.utils.git import Service, Git

CURRDIR = Path.cwd()

logger = logging.getLogger(__name__)

router = APIRouter()


@dataclass
class Get:
    user: str
    path: str
    service: Service


@dataclass
class Post:
    user: str
    path: str
    service: Service
    req: Request
    address: str = Depends(magic.ethaddress)


@router.get('/{user}/{path}/info/refs')
async def inforefs(ctx: Get = Depends(Get)):
    path = config.CODSTORAGE_REPOS_DIR / ctx.user / ctx.path
    repo = Git(path) if path.exists() else Git.init(path)

    hook = f'''
        #!/bin/sh
        cd {CURRDIR} && python -m codstorage {path}
    '''
    repo.add_hook('post-receive', hook)

    data = repo.inforefs(ctx.service.value)
    media = f'application/x-{ctx.service.value}-advertisement'
    return StreamingResponse(data, media_type=media)


@router.post('/{user}/{path}/{service}')
async def service(ctx: Post = Depends(Post)):
    path = config.CODSTORAGE_REPOS_DIR / ctx.user / ctx.path
    repo = Git(path)

    stream = ctx.req.stream()
    data = [data async for data in stream]
    data = b''.join(data)

    data = repo.service(ctx.service.value, data)
    media = f'application/x-{ctx.service.value}-result'
    return StreamingResponse(data, media_type=media)
