from app.cache.item_cache import ItemCache
from app.models.item import Item, ItemCreate, ItemUpdate
from app.repositories.item_repository import ItemRepository


class ItemService:
    def __init__(self, repository: ItemRepository, cache: ItemCache) -> None:
        self.repository = repository
        self.cache = cache

    def list_items(self) -> list[Item]:
        return self.repository.list()

    def get_item(self, item_id: int) -> Item | None:
        cached = self.cache.get(item_id)
        if cached is not None:
            return cached

        item = self.repository.get(item_id)
        if item is not None:
            self.cache.put(item)
        return item

    def create_item(self, payload: ItemCreate) -> Item:
        return self.repository.create(payload)

    def update_item(self, item_id: int, payload: ItemUpdate) -> Item | None:
        updated = self.repository.update(item_id, payload)
        if updated is not None:
            self.cache.invalidate(item_id)
        return updated

    def delete_item(self, item_id: int) -> bool:
        deleted = self.repository.delete(item_id)
        if deleted:
            self.cache.invalidate(item_id)
        return deleted