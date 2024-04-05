from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from .auth import auth_backend
from .manager import get_user_manager
from .dependencies import UserRead, UserCreate, UserUpdate, User

from app import app

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(UserRead, UserCreate)

