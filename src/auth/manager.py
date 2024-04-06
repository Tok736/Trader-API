from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from config import settings

from .dependencies import User
from .utils import get_user_db

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.auth_secret_key
    verification_token_secret = settings.auth_secret_key

    async def on_after_register(
            self, 
            user: User, 
            request: Request | None = None
    ) -> None:
        print(f"User {user.id} has registered")

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)