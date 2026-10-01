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
