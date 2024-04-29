from contextlib import asynccontextmanager

from fastapi import FastAPI

from redis_connection.get_redis import get_redis

@asynccontextmanager
async def lifespan(app: FastAPI):
    ''' 
    Function get all resources at project start. 
    Resources are released after "yield" command. 
    '''
    redis = get_redis()

    yield

    await redis.close()

app = FastAPI(
    lifespan=lifespan,
    title="Trading App"
)
