# Library imports
import pytest
from fastapi.testclient import TestClient
from main import app

# Test client
client = TestClient(app)

# Test cases
def test_health_check():
    """
    Test health check endpoint
    """
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_generate_image():
    """
    Test generate image endpoint
    """
    response = client.get("/generate_image/?prompt=photo of an astronaut riding a horse on mars")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

def test_root():
    """
    Test root endpoint
    """
    response = client.get("/")
    assert response.status_code == 200
