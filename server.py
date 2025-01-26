from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.gzip import GZipMiddleware
from app.routes.users import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000,
    compresslevel=5,
)

app.include_router(user_router)
