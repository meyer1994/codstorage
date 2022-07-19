import httpx
from fastapi import APIRouter, Depends, Request

from codstorage.db import db

router = APIRouter()


@router.get('/')
async def getrepos():
    return await db.fetch_all('SELECT * FROM repos')
