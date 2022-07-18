from fastapi import APIRouter

from .ipfs import router as router_ipfs
from .repos import router as router_repos


router = APIRouter()
router.include_router(router_ipfs, prefix='/ipfs')
router.include_router(router_repos)
