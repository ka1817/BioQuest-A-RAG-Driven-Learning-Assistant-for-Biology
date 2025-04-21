# tests/test_api.py
import httpx

def test_predict():
    response = httpx.post("http://localhost:2000/predict", json={"question": "What are different types of walls in heart"})
    assert response.status_code == 200
    assert "answer" in response.json()
