from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000,
    compresslevel=5,
)
