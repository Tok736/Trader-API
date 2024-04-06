from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from app import app

from .auth import auth_backend
from .manager import get_user_manager
from .dependencies import UserRead, UserCreate, UserUpdate, User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend]
)

auth_router = fastapi_users.get_auth_router(auth_backend)
auth_router.prefix = "/auth/jwt"
auth_router.tags = ["auth"]

register_router = fastapi_users.get_register_router(UserRead, UserCreate)
register_router.prefix = "/auth"
register_router.tags = ["auth"]
