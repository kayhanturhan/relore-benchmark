from app.models.item import ItemCreate
from app.repositories.item_repository import ItemRepository


def test_create_and_get_item() -> None:
    repository = ItemRepository()
    created = repository.create(ItemCreate(name="Keyboard", price=100.0))

    assert created.id == 1
    assert repository.get(created.id) == created


def test_delete_item() -> None:
    repository = ItemRepository()
    created = repository.create(ItemCreate(name="Mouse", price=50.0))

    assert repository.delete(created.id) is True
    assert repository.get(created.id) is None
