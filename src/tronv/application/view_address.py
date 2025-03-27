from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from tronv.driven.pydantic.models import Address
from tronv.driven.sqlalchemy.models import AddressViewLog
from tronv.driven.tronpy.addresses import Addresses


@dataclass(kw_only=True, frozen=True, slots=True)
class ViewAddress:
    session: AsyncSession
    addresses: Addresses

    async def __call__(
        self, address_text: str,
    ) -> Address | None:
        address = await self.addresses.address_with_text(address_text)

        if address is not None:
            log = AddressViewLog(
                id=uuid4(),
                viewing_time=datetime.now(UTC),
                address_text=address.text,
                trx_balance=address.trx_balance,
                bandwidth=address.bandwidth,
                energy=address.energy,
            )
        else:
            log = AddressViewLog(
                id=uuid4(),
                viewing_time=datetime.now(UTC),
                address_text=address_text,
                trx_balance=None,
                bandwidth=None,
                energy=None,
            )

        async with self.session.begin():
            self.session.add(log)
            await self.session.commit()

        return address
