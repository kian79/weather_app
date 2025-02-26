from fastapi import FastAPI
from .routes import router
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
import redis.asyncio as redis

app = FastAPI()

@app.on_event("startup")
async def startup():
    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

