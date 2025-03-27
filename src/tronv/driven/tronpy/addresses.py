from dataclasses import dataclass
from decimal import Decimal
from typing import cast

from tronpy.async_tron import AsyncTron
from tronpy.exceptions import AddressNotFound, BadAddress

from tronv.driven.pydantic.models import Address


@dataclass(kw_only=True, frozen=True, slots=True)
class Addresses:
    tron: AsyncTron

    async def address_with_text(self, text: str) -> Address | None:
        try:
            account_resource = await self.tron.get_account_resource(text)   
            account = await self.tron.get_account(text)
            bandwidth = cast(int, await self.tron.get_bandwidth(text))
        except AddressNotFound:
            return None
        except BadAddress:
            return None

        text = cast(str, account["address"])
        trx_balance = self._balance_from_raw_when(
            raw_balance=cast(int, account.get("balance", 0))
        )
        energy = cast(int, account_resource["TotalEnergyWeight"])

        return Address(
            bandwidth=bandwidth,
            trx_balance=trx_balance,
            energy=energy,
            text=text,
        )

    def _balance_from_raw_when(self, *, raw_balance: int) -> Decimal:
        return Decimal(raw_balance) / 1_000_000
