from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
