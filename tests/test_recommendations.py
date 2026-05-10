from fastapi.testclient import TestClient
from app.main import app
from app.services.recommendation_service import get_recommendations

client = TestClient(app)

def test_recommendations_returns_ranked_results():
    payload = {
        "mood" : "sad",
        "dietary_tags": ["vegan", "gluten_free"],
        "effort": "medium",
        "preparation_time_mins": 20
    }


    response = client.post("/recommendations", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert isinstance(data["recommendations"], list)
    assert len(data["recommendations"]) > 0

def test_chicken_rice_bowl_recommendation():
    result = get_recommendations(
        mood="tired",
        dietary_tags=["high_protein"],
        effort="low",
        preparation_time_mins=15
    )

    recommendations = result["recommendations"]
    assert recommendations[0]["meal_name"] == "Chicken Rice Bowl"

def test_recommendations_invalid_input():
    payload = {
        "mood": 20,
        "dietary_tags": "vegan",
        "effort": 0,
        "preparation_time_mins": "fast"
    }

    response = client.post("/recommendations", json = payload)
    assert response.status_code == 422

# Test that ensures scoring logic is working as expected
# Test for no recommendations found scenario

