from fastapi import FastAPI

from app.api.routes import build_router
from app.cache.item_cache import ItemCache
from app.repositories.item_repository import ItemRepository
from app.services.item_service import ItemService

repository = ItemRepository()
cache = ItemCache()
service = ItemService(repository=repository, cache=cache)

app = FastAPI(title="Relore Benchmark API", version="0.1.0")
app.include_router(build_router(service))


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
