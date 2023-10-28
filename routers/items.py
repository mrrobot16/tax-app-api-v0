from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from fastapi import Body, HTTPException, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
import yaml

from models import Item, fake_db_items
from constants import openapi_extra_item

from dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["Items Router"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", operation_id="some_specific_id_you_define", openapi_extra={"x-aperture-labs-portal": "blue"})
async def root_items():
    return [{"item_id": "Foo"}]

@router.post("/items/", response_model = Item, summary = "Create an item", openapi_extra = openapi_extra_item)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    :param item: User input.
    """
    return item

@router.post(
    "/items-yaml/",
    openapi_extra={
        "requestBody": {
            "content": {"application/x-yaml": {"schema": Item.model_json_schema()}},
            "required": True,
        },
    },
)
async def create_item_yaml(request: Request):
    raw_body = await request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(status_code=422, detail="Invalid YAML")
    try:
        item = Item.model_validate(data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    return item


@router.put("/items/{item_id}")
async def upsert_item(
    item_id: str,
    name: Annotated[str | None, Body()] = None,
    size: Annotated[int | None, Body()] = None,
):
    if item_id in fake_db_items:
        item = fake_db_items[item_id]
        item["name"] = name
        item["size"] = size
        return item
    else:
        item = {"name": name, "size": size}
        fake_db_items[item_id] = item
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)

@router.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data, status_code=status.HTTP_202_ACCEPTED)
