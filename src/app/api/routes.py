from fastapi import APIRouter, HTTPException, status

from app.models.item import Item, ItemCreate
from app.services.item_service import ItemService


def build_router(service: ItemService) -> APIRouter:
    router = APIRouter(prefix="/items", tags=["items"])

    @router.get("", response_model=list[Item])
    def list_items() -> list[Item]:
        return service.list_items()

    @router.get("/{item_id}", response_model=Item)
    def get_item(item_id: int) -> Item:
        item = service.get_item(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
    def create_item(payload: ItemCreate) -> Item:
        return service.create_item(payload)

    @router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_item(item_id: int) -> None:
        if not service.delete_item(item_id):
            raise HTTPException(status_code=404, detail="Item not found")

    return router
