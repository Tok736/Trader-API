from typing import Any

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from redis.asyncio.client import Redis

from config import settings

def get_redis() -> Redis:
    ''' Connection to redis '''
    redis = aioredis.from_url(f"redis://{settings.redis_host}:{settings.redis_port}", decode_responses=False)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    return redis

