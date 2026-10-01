from app.models.item import Item


class ItemCache:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def put(self, item: Item) -> None:
        self._items[item.id] = item

    def invalidate(self, item_id: int) -> None:
        self._items.pop(item_id, None)

    def clear(self) -> None:
        self._items.clear()
