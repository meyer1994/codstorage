from pathlib import Path
from dataclasses import dataclass

from pfluent import Runner
from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse

from codstorage.config import config
from codstorage.utils.git import Service, Git


router = APIRouter()


@router.get('/Qm{qmhash}/info/refs')
async def ipfsinforefs(qmhash: str, service: Service):
    qmhash = f'Qm{qmhash}'
    path = config.CODSTORAGE_REPOS_DIR / qmhash
    repo = Git(path)

    Runner('ipfs')\
        .arg('get', qmhash)\
        .arg('--output', path)\
        .arg('--api', '/ip4/127.0.0.1/tcp/5001')\
        .run(check=True)

    data = repo.inforefs(service.value)
    media = f'application/x-{service.value}-advertisement'
    return StreamingResponse(data, media_type=media)


@dataclass
class Post:
    qmhash: str
    service: Service
    req: Request


@router.post('/Qm{qmhash}/{service}')
async def service(ctx: Post = Depends(Post)):
    qmhash = f'Qm{ctx.qmhash}'
    path = config.CODSTORAGE_REPOS_DIR / qmhash
    repo = Git(path)

    stream = ctx.req.stream()
    data = [data async for data in stream]
    data = b''.join(data)

    data = repo.service(ctx.service.value, data)
    media = f'application/x-{ctx.service.value}-result'
    return StreamingResponse(data, media_type=media)
