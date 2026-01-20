"""
Test suite for the FastAPI application
"""
import pytest
from starlette.testclient import TestClient
from api.index import app


@pytest.fixture
def client():
    return TestClient(app=app)


def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["status"] == "running"
    print("✓ Root endpoint OK")


def test_hello_endpoint_default(client):
    """Test hello endpoint with default name"""
    response = client.get("/api/hello")
    assert response.status_code == 200
    data = response.json()
    assert "Hello, World!" in data["message"]
    print("✓ Hello endpoint (default) OK")


def test_hello_endpoint_with_name(client):
    """Test hello endpoint with custom name"""
    response = client.get("/api/hello?name=Test")
    assert response.status_code == 200
    data = response.json()
    assert "Hello, Test!" in data["message"]
    print("✓ Hello endpoint (with name) OK")


def test_get_item(client):
    """Test get item endpoint"""
    response = client.get("/api/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 1
    assert "Item 1" in data["name"]
    print("✓ Get item endpoint OK")


def test_create_item(client):
    """Test create item endpoint"""
    response = client.post("/api/items?item_name=Test&item_description=Test Description")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["item"]["name"] == "Test"
    print("✓ Create item endpoint OK")


def test_date_endpoint(client):
    """Test date endpoint"""
    response = client.get("/api/date")
    assert response.status_code == 200
    data = response.json()
    assert "date" in data
    assert "time" in data
    assert "datetime" in data
    assert "timestamp" in data
    # Verify date format (YYYY-MM-DD)
    assert len(data["date"]) == 10
    assert data["date"].count("-") == 2
    print("✓ Date endpoint OK")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
