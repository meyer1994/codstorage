from fastapi import APIRouter

from .git import router as router_git
from .ipfs import router as router_ipfs
from .ipld import router as router_ipns
from .repos import router as router_repos


router = APIRouter()


@router.get('/ping')
async def ping():
    return 'pong'


router.include_router(router_ipns, prefix='/ipld')
router.include_router(router_repos, prefix='/repos')

router.include_router(router_ipfs)
router.include_router(router_git)
