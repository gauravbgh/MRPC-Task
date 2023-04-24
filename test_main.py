from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_item():
    response = client.post("/predict",
    json={"sentence1": "let's watch a movie", "sentence2": "I would love to watch a movie"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "class is": [1],
    }

