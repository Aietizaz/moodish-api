from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_meals_check():
    response = client.get("/meals")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]

