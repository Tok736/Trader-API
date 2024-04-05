from datetime import datetime

from sqlalchemy import String, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Role(Base):
    __tablename__ = "role"

    id:              Mapped[int]        = mapped_column(primary_key=True)
    name:            Mapped[str]        = mapped_column()
    permissions:     Mapped[str | None] = mapped_column(JSON)

class User(Base):
    __tablename__ = "user"

    id:              Mapped[int]        = mapped_column(primary_key=True)
    username:        Mapped[str]        = mapped_column(index=True)
    registered_at:   Mapped[datetime]   = mapped_column(default=datetime.now, index=True)

    email:           Mapped[str]        = mapped_column(String(length=320), unique=True, index=True)
    hashed_password: Mapped[str]        = mapped_column(String(length=1024))
    is_active:       Mapped[bool]       = mapped_column(default=True)
    is_superuser:    Mapped[bool]       = mapped_column(default=False)
    is_verified:     Mapped[bool]       = mapped_column(default=False)

    role_id:         Mapped[int | None] = mapped_column(ForeignKey("role.id"))
    



