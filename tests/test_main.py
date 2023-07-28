import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_generate_image():
    response = client.get("/generate_image/photo of an astronaut riding a horse on mars")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

def test_root():
    response = client.get("/")
    assert response.status_code == 302
    assert response.headers["location"] == "/docs"
