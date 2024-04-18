from .auth import auth_backend
from .dependencies import UserRead, UserCreate
from .manager import fastapi_users

auth_router = fastapi_users.get_auth_router(auth_backend)
auth_router.prefix = "/auth/jwt"
auth_router.tags = ["auth"]

register_router = fastapi_users.get_register_router(UserRead, UserCreate)
register_router.prefix = "/auth"
register_router.tags = ["auth"]
