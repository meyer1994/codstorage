import httpx
from fastapi import APIRouter, Depends, Request


router = APIRouter()


@router.get('/{ipfs}')
async def getipfs(ipfs: str):
    params = {'arg': ipfs, 'progress': False}
    url = 'http://127.0.0.1:5001/api/v0/cat'
    res = httpx.post(url, params=params)
    return res.text
