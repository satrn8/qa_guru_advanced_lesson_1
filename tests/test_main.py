from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_item():
    body = {
        "name": "Алина",
        "description": "тест1",
        "price": 10.5,
        "tax": 1.5
    }
    response = client.post("/items/", json=body)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Item1"
    assert data["description"] == "A new item"
    assert data["price"] == 10.5
    assert data["tax"] == 1.5
    assert "id" in data


def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_item():
    body = {
        "name": "Ирина",
        "description": "тест2",
        "price": 20.0,
        "tax": 2.0
    }
    create_response = client.post("/items/", json=body)
    assert create_response.status_code == 200
    item_id = create_response.json()["id"]
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Item2"
    assert data["description"] == "Another item"
    assert data["price"] == 20.0
    assert data["tax"] == 2.0


def test_update_item():
    body = {
        "name": "Марина",
        "description": "тест3",
        "price": 30.0,
        "tax": 3.0
    }
    create_response = client.post("/items/",
                                  json=body)
    assert create_response.status_code == 200
    item_id = create_response.json()["id"]

    body = {
        "name": "Обновление",
        "description": "тест обновление",
        "price": 35.0,
        "tax": 3.5
    }
    update_response = client.put(f"/items/{item_id}", json=body)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["id"] == item_id
    assert data["name"] == "Updated Item3"
    assert data["description"] == "Updated item"
    assert data["price"] == 35.0
    assert data["tax"] == 3.5


def test_delete_item():
    body = {
        "name": "Карина",
        "description": "тест4",
        "price": 40.0,
        "tax": 4.0
    }
    create_response = client.post("/items/", json=body)
    assert create_response.status_code == 200
    item_id = create_response.json()["id"]

    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 200
    data = delete_response.json()
    assert data["id"] == item_id
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404
