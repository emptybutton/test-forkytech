from collections.abc import Sequence
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tronv.driven.sqlalchemy.models import AddressViewLog


class InvalidPageNumberError(Exception): ...


@dataclass(kw_only=True, frozen=True, slots=True)
class ViewAddressViewLogs:
    session: AsyncSession
    page_size: int

    def __post_init__(self) -> None:
        assert self.page_size > 0

    async def __call__(self, page_number: int) -> Sequence[AddressViewLog]:
        """
        :raises tronv.application.view_request_logs.InvalidPageNumberError:
        """

        if page_number < 0:
            raise InvalidPageNumberError

        async with self.session.begin():
            result = await self.session.scalars(
                select(AddressViewLog)
                .order_by(AddressViewLog.viewing_time.desc())
                .offset(page_number * self.page_size)
                .limit(self.page_size)
            )
            logs = result.all()
            await self.session.commit()

        return logs
