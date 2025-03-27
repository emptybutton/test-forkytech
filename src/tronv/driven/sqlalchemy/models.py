from datetime import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy import DECIMAL, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Model(DeclarativeBase): ...


class AddressViewLog(Model):
    __tablename__ = "address_view_logs"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    address_text: Mapped[str]
    trx_balance: Mapped[Decimal | None] = mapped_column(DECIMAL())
    bandwidth: Mapped[int | None]
    energy: Mapped[int | None]
    viewing_time: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
