from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from codstorage.db import db
from codstorage.routes import router

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
)


@app.on_event('startup')
async def startup():
    await db.connect()
    query = '''
        CREATE TABLE IF NOT EXISTS repos(
            ipfs TEXT,
            ipld TEXT,
            likes INT
        )
    '''
    await db.execute(query)
