from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, Field

from tronv.application.view_address import ViewAddress
from tronv.driver.fastapi.schemas.common import NoDataSchema
from tronv.driver.fastapi.schemas.output import AddressSchema
from tronv.driver.fastapi.tags import Tag


view_address_router = APIRouter()


class ViewAddressSchema(BaseModel):
    address_text: str = Field(alias="address")


@view_address_router.post(
    "/address",
    responses={
        status.HTTP_200_OK: {"model": AddressSchema},
        status.HTTP_404_NOT_FOUND: {"model": NoDataSchema},
    },
    summary="View an address",
    description="View an address and write a log about this.",
    tags=[Tag.address],
)
@inject
async def view_address_route(
    view_address: FromDishka[ViewAddress],
    request_body: ViewAddressSchema,
) -> Response:
    address = await view_address(request_body.address_text)

    if address is None:
        response_body = NoDataSchema().model_dump(by_alias=True, mode="json")
        status_code = status.HTTP_404_NOT_FOUND
        return JSONResponse(response_body, status_code=status_code)

    response_body = (
        AddressSchema.of(address).model_dump(by_alias=True, mode="json")
    )
    return JSONResponse(response_body)
