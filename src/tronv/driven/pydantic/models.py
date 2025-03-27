from decimal import Decimal

from pydantic import BaseModel


class Address(BaseModel):
    text: str
    bandwidth: int
    energy: int
    trx_balance: Decimal
