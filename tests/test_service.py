from app.cache.item_cache import ItemCache
from app.models.item import ItemCreate, ItemUpdate
from app.repositories.item_repository import ItemRepository
from app.services.item_service import ItemService


def build_service() -> ItemService:
    return ItemService(ItemRepository(), ItemCache())


def test_get_item_populates_cache() -> None:
    service = build_service()
    created = service.create_item(ItemCreate(name="Monitor", price=300.0))

    fetched = service.get_item(created.id)

    assert fetched == created
    assert service.cache.get(created.id) == created


def test_delete_invalidates_cache() -> None:
    service = build_service()
    created = service.create_item(ItemCreate(name="Dock", price=120.0))
    service.get_item(created.id)

    service.delete_item(created.id)

    assert service.cache.get(created.id) is None


def test_update_refreshes_cache() -> None:
    service = build_service()
    created = service.create_item(ItemCreate(name="Monitor", price=300.0))

    service.get_item(created.id)
    assert service.cache.get(created.id) == created

    updated = service.update_item(
        created.id,
        ItemUpdate(name="Gaming Monitor", price=450.0),
    )

    assert updated is not None
    assert updated.name == "Gaming Monitor"
    assert service.cache.get(created.id) == updated