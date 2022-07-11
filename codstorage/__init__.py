from fastapi import FastAPI

from codstorage.routes import router

app = FastAPI()
app.include_router(router)
