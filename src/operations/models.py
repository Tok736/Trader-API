from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from database import Base, CreatedAt, UpdatedAt

class Operation(Base, CreatedAt, UpdatedAt):
    __tablename__ = "operation"

    id:               Mapped[int]        = mapped_column(primary_key=True)
    quantity:         Mapped[int]        = mapped_column()
    figi:             Mapped[str]        = mapped_column()
    instrument_type:  Mapped[str | None] = mapped_column(index=True)
    date:             Mapped[datetime]   = mapped_column(index=True)
    type:             Mapped[str]        = mapped_column()
    




