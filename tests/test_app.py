import pytest
from flask import Flask

# Создаём минимальное Flask-приложение для примера
app = Flask(__name__)

@app.route("/")
def home():
    return "Добро пожаловать! Новости на главной странице."

# Фикстура для тестового клиента
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Тест
def test_home(client):
    response = client.get("/")
    # response.data — это байты, поэтому строку нужно закодировать в UTF-8
    assert "Новости".encode("utf-8") in response.data
