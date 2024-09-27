import sys
import os

# Adiciona o diretório raiz do projeto ao caminho
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app  # A importação do app deve vir após o ajuste do sys.path

client = TestClient(app)

def test_create_character():
    response = client.post("/characters", json={
        "nickname": "Conan",
        "player": {
            "name": "Erick",
            "id": "12345"
        },
        "xp": 1000,
        "race": "Humano",
        "classes": ["Barbarian"],
        "background": {
            "name": "Soldier",
            "description": "A skilled leader of men"
        }
    })
    assert response.status_code == 200
    assert response.json()["nickname"] == "Conan"

def test_get_characters():
    response = client.get("/characters")
    assert response.status_code == 200
    assert len(response.json()) > 0
