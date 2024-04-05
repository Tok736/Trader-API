from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from .dependencies import User
from .utils import get_user_db

from config import settings

class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.auth_secret_key
    verification_token_secret = settings.auth_secret_key

    async def on_after_register(
            self, 
            user: User, 
            request: Request | None = None
        ) -> None:
        print(f"User {user.id} has registered")
        # return await super().on_after_register(self, user, request)

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)