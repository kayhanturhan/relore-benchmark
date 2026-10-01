from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_item_lifecycle() -> None:
    create_response = client.post("/items", json={"name": "Laptop", "price": 1500.0})
    assert create_response.status_code == 201
    item = create_response.json()

    get_response = client.get(f"/items/{item['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Laptop"

    delete_response = client.delete(f"/items/{item['id']}")
    assert delete_response.status_code == 204

    missing_response = client.get(f"/items/{item['id']}")
    assert missing_response.status_code == 404


def test_rejects_non_positive_price() -> None:
    response = client.post("/items", json={"name": "Broken", "price": 0})
    assert response.status_code == 422
    
def test_update_item() -> None:
    create_response = client.post(
        "/items",
        json={"name": "Laptop", "price": 1500.0},
    )
    item = create_response.json()

    update_response = client.put(
        f"/items/{item['id']}",
        json={"name": "Gaming Laptop", "price": 2000.0},
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == "Gaming Laptop"
    assert update_response.json()["price"] == 2000.0


def test_update_missing_item_returns_404() -> None:
    response = client.put(
        "/items/9999",
        json={"name": "Missing", "price": 100.0},
    )

    assert response.status_code == 404

def test_delete_missing_item_returns_404() -> None:
    response = client.delete("/items/9999")

    assert response.status_code == 404