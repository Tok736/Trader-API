from datetime import datetime

from sqlalchemy import String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, CreatedAt, UpdatedAt


class Role2User(Base, CreatedAt, UpdatedAt):
    ''' Table representing many to many relation between 'role' and 'user' '''
    __tablename__ = "role2user"

    id:              Mapped[int]          = mapped_column(primary_key=True)
    role_id:         Mapped[int]          = mapped_column(ForeignKey("role.id"))
    user_id:         Mapped[int]          = mapped_column(ForeignKey("user.id"))


class Role(Base, CreatedAt, UpdatedAt):
    __tablename__ = "role"

    id:              Mapped[int]          = mapped_column(primary_key=True)
    name:            Mapped[str]          = mapped_column()
    permissions:     Mapped[str | None]   = mapped_column(JSON)

    users:           Mapped[list["User"]] = relationship(secondary="role2user")


class User(Base, UpdatedAt):
    __tablename__ = "user"

    id:              Mapped[int]          = mapped_column(primary_key=True)
    username:        Mapped[str]          = mapped_column(index=True)
    registered_at:   Mapped[datetime]     = mapped_column(default=datetime.now, index=True)

    email:           Mapped[str]          = mapped_column(String(length=320), unique=True, index=True)
    hashed_password: Mapped[str]          = mapped_column(String(length=1024))
    is_active:       Mapped[bool]         = mapped_column(default=True)
    is_superuser:    Mapped[bool]         = mapped_column(default=False)
    is_verified:     Mapped[bool]         = mapped_column(default=False)

    roles:           Mapped[list["Role"]] = relationship(secondary="role2user")
    



