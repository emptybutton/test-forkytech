from collections.abc import Sequence
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from tronv.driven.pydantic.models import Address
from tronv.driven.sqlalchemy.models import AddressViewLog


class AddressViewLogSchema(BaseModel):
    address: str = Field(alias="address")
    trx_balance: Decimal | None = Field(alias="trxBalance")
    bandwidth: int | None = Field(alias="bandwidth")
    energy: int | None = Field(alias="energy")
    viewing_time: datetime | None = Field(alias="viewingTime")

    @classmethod
    def of(cls, log: AddressViewLog) -> "AddressViewLogSchema":
        return AddressViewLogSchema(
            address=log.address_text,
            trxBalance=log.trx_balance,
            bandwidth=log.bandwidth,
            energy=log.energy,
            viewingTime=log.viewing_time,
        )


class AddressViewLogsSchema(BaseModel):
    logs: list[AddressViewLogSchema] = Field(alias="logs")

    @classmethod
    def of(
        cls, logs: Sequence[AddressViewLog]
    ) -> "AddressViewLogsSchema":
        return AddressViewLogsSchema(
            logs=list(map(AddressViewLogSchema.of, logs)),
        )


class AddressSchema(BaseModel):
    address: str = Field(alias="address")
    trx_balance: Decimal = Field(alias="trxBalance")
    bandwidth: int = Field(alias="bandwidth")
    energy: int = Field(alias="energy")

    @classmethod
    def of(cls, address: Address) -> "AddressSchema":
        return AddressSchema(
            address=address.text,
            bandwidth=address.bandwidth,
            energy=address.energy,
            trxBalance=address.trx_balance,
        )
