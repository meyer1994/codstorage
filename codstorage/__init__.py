import shutil

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from codstorage.db import db
from codstorage.routes import router
from codstorage.config import config

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

    # Create
    config.CODSTORAGE_REPOS_DIR.mkdir(parents=True, exist_ok=True)
    config.CODSTORAGE_SQLITE_FILE.touch(exist_ok=True)


@app.on_event('shutdown')
async def shutdown():
    # Remove
    shutil.rmtree(config.CODSTORAGE_REPOS_DIR)
    config.CODSTORAGE_SQLITE_FILE.unlink(missing_ok=True)
