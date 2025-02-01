import pytest
import logging
from utils.api_client import PetStoreClient

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def client():
    return PetStoreClient("https://petstore.swagger.io/v2")

def test_create_user(client):
    logger.info("Starting test_create_user")

    # Данные для создания пользователя

    user_data = {
        "id": 1,
        "username": "testUser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }

    # Создаем пользователя
    response = client.create_user(user_data)
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # статус-код
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_get_user_by_username(client):
    logger.info("Starting test_get_user_by_username")
    user_data = {
        "id": 1,
        "username": "testUser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }
    create_response = client.create_user(user_data)
    assert create_response.status_code == 200, f"Failed to create user: {create_response.status_code}"

    # Получаем пользователя по имени
    response = client.get_user_by_username("testUser")
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # Проверяем статус-код и данные
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["username"] == "testUser", f"Expected username 'testUser', but got {response.json()['username']}"

def test_update_user(client):
    logger.info("Starting test_update_user")

    # Сначала создаем пользователя
    user_data = {
        "id": 1,
        "username": "testUser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }
    create_response = client.create_user(user_data)
    assert create_response.status_code == 200, f"Failed to create user: {create_response.status_code}"

    # Обновляем данные пользователя
    updated_user_data = {
        "id": 1,
        "username": "updatedUser",
        "firstName": "Updated",
        "lastName": "User",
        "email": "updated@example.com",
        "password": "newpassword123",
        "phone": "0987654321",
        "userStatus": 1
    }
    response = client.update_user("testUser", updated_user_data)
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # Проверяем статус-код
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_delete_user(client):
    logger.info("Starting test_delete_user")

    # Сначала создаем пользователя
    user_data = {
        "id": 1,
        "username": "testUser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }
    create_response = client.create_user(user_data)
    assert create_response.status_code == 200, f"Failed to create user: {create_response.status_code}"

    # Удаляем пользователя по имени
    response = client.delete_user("testUser")
    logger.info(f"Response: {response.status_code}")

    # Проверяем статус-код
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверяем, что пользователь действительно удален
    get_response = client.get_user_by_username("testUser")
    assert get_response.status_code == 404, f"Expected status code 404, but got {get_response.status_code}"