from fastapi import APIRouter

from .ipfs import router as router_ipfs
from .users import router as router_users
from .repos import router as router_repos


router = APIRouter()


@router.get('/ping')
async def ping():
    return 'pong'


router.include_router(router_ipfs, prefix='/ipfs')
router.include_router(router_users, prefix='/users')
router.include_router(router_repos)

