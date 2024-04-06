from datetime import datetime

from pydantic import EmailStr

from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate

class UserRead(BaseUser):
    id:           int
    email:        EmailStr
    username:     str
    role_id:      int | None
    is_active:    bool = True
    is_superuser: bool = False
    is_verified:  bool = False
    updated_at:   datetime

    class Config:
        from_attributes = True


class UserCreate(BaseUserCreate):
    email:        EmailStr
    username:     str
    role_id:      int | None
    password:     str
    is_active:    bool | None = True
    is_superuser: bool | None = False
    is_verified:  bool | None = False
    updated_at:   datetime


class UserUpdate(BaseUserUpdate):
    password:     str | None = None
    email:        EmailStr | None = None
    username:     str | None = None
    role_id:      int | None = None
    is_active:    bool | None = None
    is_superuser: bool | None = None
    is_verified:  bool | None = None
    updated_at:   datetime



