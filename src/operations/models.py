from datetime import datetime

from sqlalchemy import MetaData, String, Boolean, ForeignKey, Integer, TIMESTAMP, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs

from database import Base

class Operation(Base):
    __tablename__ = "operation"

    id:               Mapped[int]        = mapped_column(primary_key=True)
    quantinity:       Mapped[int]        = mapped_column()
    figi:             Mapped[str]        = mapped_column()
    instrument_type:  Mapped[str | None] = mapped_column()
    date:             Mapped[datetime]   = mapped_column()
    type:             Mapped[str]        = mapped_column()
    




