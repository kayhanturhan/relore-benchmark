from app.models.item import Item, ItemCreate, ItemUpdate


class ItemRepository:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._next_id = 1

    def list(self) -> list[Item]:
        return list(self._items.values())

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def create(self, payload: ItemCreate) -> Item:
        item = Item(id=self._next_id, name=payload.name.strip().lower(), price=payload.price)
        self._items[item.id] = item
        self._next_id += 1
        return item

    def update(self, item_id: int, payload: ItemUpdate) -> Item | None:
        if item_id not in self._items:
            return None

        item = Item(id=item_id, name=payload.name.strip().lower(), price=payload.price)
        self._items[item_id] = item
        return item

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None