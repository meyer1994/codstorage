import logging
from pathlib import Path
from tempfile import TemporaryDirectory

from fastapi import APIRouter, Request

from codstorage.git import Service, Git


TEMPDIR = TemporaryDirectory()
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get('/{path}/info/refs')
async def inforefs(path: str, service: Service):
    path = Path(TEMPDIR.name, path)
    repo = Git(path) if path.exists() else Git.init(path)

    hook = r'''
        #!/bin/sh
        echo "hello world"
    '''
    repo.add_hook('post-receive', hook)

    data = repo.inforefs(service)
    media = f'application/x-{service}-advertisement'
    return StreamingResponse(data, media_type=media)



@router.post('/{path}/{service}')
async def service(path: str, service: Service, req: Request):
    path = Path(TEMPDIR.name, path)
    repo = Git(path)

    stream = req.stream()
    data = [data async for data in stream]
    data = b''.join(data)

    data = repo.service(service, data)
    media = f'application/x-{service}-result'
    return StreamingResponse(data, media_type=media)
