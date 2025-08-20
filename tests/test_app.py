import sys, os

# добавляем путь к корню проекта, чтобы импортировать app.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, CI/CD" in response.data
