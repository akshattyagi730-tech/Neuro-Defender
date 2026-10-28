import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

with open("test_img.png", "rb") as f:
    response = client.post("/api/v1/detect", files={"image": ("test_img.png", f, "image/png")})

print(f"Status: {response.status_code}")
print(response.json())
assert response.status_code == 200, f"Expected 200, got {response.status_code}"
assert "threat_level" in response.json(), "Missing threat_level in response"
print("test_detect.py: PASSED")

