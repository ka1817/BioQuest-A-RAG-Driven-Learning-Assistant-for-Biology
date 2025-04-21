
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_endpoint_success():
    response = client.post("/predict", json={"question": "What is different types of wall?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert isinstance(data["answer"], str)

def test_predict_endpoint_invalid_payload():
    response = client.post("/predict", json={})
    assert response.status_code == 422  

def test_out_of_syllabus_response():
    response = client.post("/predict", json={"question": "What is the capital of France?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert data["answer"] == "Out of syllabus" or isinstance(data["answer"], str)
