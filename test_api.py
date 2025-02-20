# test_api.py
import requests

BASE_URL = "http://127.0.0.1:8060/api"

def test_health_endpoint():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "API is running"

def test_analytics_endpoint():
    response = requests.get(f"{BASE_URL}/analytics")
    assert response.status_code == 200
    data = response.json()
    assert "total_clubs" in data
    assert "total_members" in data
