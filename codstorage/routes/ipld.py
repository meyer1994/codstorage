import httpx
from fastapi import APIRouter, Depends, Request


router = APIRouter()


@router.get('/{ipld}')
async def getipld(ipld: str):
    params = {'arg': ipld}
    url = 'http://localhost:5001/api/v0/dag/get'
    res = httpx.post(url, params=params)
    return res.json()
