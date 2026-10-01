from app.models.item import ItemCreate, ItemUpdate
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

def test_update_item() -> None:
    repository = ItemRepository()
    created = repository.create(ItemCreate(name="Keyboard", price=100.0))

    updated = repository.update(
        created.id,
        ItemUpdate(name="Mechanical Keyboard", price=150.0),
    )

    assert updated is not None
    assert updated.name == "Mechanical Keyboard"
    assert updated.price == 150.0
    assert repository.get(created.id) == updated


def test_update_missing_item() -> None:
    repository = ItemRepository()

    updated = repository.update(
        999,
        ItemUpdate(name="Missing", price=10.0),
    )

    assert updated is None