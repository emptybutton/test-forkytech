from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response

from tronv.application.view_address_view_logs import ViewAddressViewLogs
from tronv.driver.fastapi.queries import page_number_query
from tronv.driver.fastapi.schemas.output import AddressViewLogsSchema
from tronv.driver.fastapi.tags import Tag


view_address_view_logs_router = APIRouter()


@view_address_view_logs_router.get(
    "/address-view-log",
    responses={
        status.HTTP_200_OK: {"model": AddressViewLogsSchema},
    },
    summary="View all logs about viewing addresses",
    description="View all logs about viewing addresses with pagination.",
    tags=[Tag.monitoring],
)
@inject
async def view_address_view_logs_route(
    view_logs: FromDishka[ViewAddressViewLogs],
    page_number: int = page_number_query
) -> Response:
    logs = await view_logs(page_number)

    response_body = (
        AddressViewLogsSchema.of(logs).model_dump(by_alias=True, mode="json")
    )
    return JSONResponse(response_body)
