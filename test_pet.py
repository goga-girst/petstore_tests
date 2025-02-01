import pytest
import logging
from utils.api_client import PetStoreClient

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def client():
    return PetStoreClient("https://petstore.swagger.io/v2")

def test_get_pet_by_id(client):
    logger.info("Starting test_get_pet_by_id")

    # Создаем питомца для тестирования
    pet_data = {
        "id": 1,
        "name": "Buddy",
        "status": "available"
    }
    create_response = client.add_pet(pet_data)
    assert create_response.status_code == 200, f"Failed to create pet: {create_response.status_code}"

    # Получаем питомца по ID
    response = client.get_pet_by_id(1)
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # Проверяем статус-код и данные
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["id"] == 1, f"Expected pet ID 1, but got {response.json()['id']}"
    assert response.json()["name"] == "Buddy", f"Expected pet name 'Buddy', but got {response.json()['name']}"

def test_add_pet(client):
    logger.info("Starting test_add_pet")

    # Данные для создания питомца
    pet_data = {
        "id": 2,
        "name": "Max",
        "status": "available"
    }

    # Добавляем питомца
    response = client.add_pet(pet_data)
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # Проверяем статус-код и данные
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["id"] == 2, f"Expected pet ID 2, but got {response.json()['id']}"
    assert response.json()["name"] == "Max", f"Expected pet name 'Max', but got {response.json()['name']}"

def test_update_pet(client):
    logger.info("Starting test_update_pet")

    # Сначала создаем питомца
    pet_data = {
        "id": 3,
        "name": "Charlie",
        "status": "available"
    }
    create_response = client.add_pet(pet_data)
    assert create_response.status_code == 200, f"Failed to create pet: {create_response.status_code}"

    # Обновляем данные питомца
    updated_pet_data = {
        "id": 3,
        "name": "Charlie Updated",
        "status": "sold"
    }
    response = client.update_pet(updated_pet_data)
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # Проверяем статус-код и обновленные данные
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["name"] == "Charlie Updated", f"Expected pet name 'Charlie Updated', but got {response.json()['name']}"
    assert response.json()["status"] == "sold", f"Expected pet status 'sold', but got {response.json()['status']}"

def test_delete_pet(client):
    logger.info("Starting test_delete_pet")

    # Сначала создаем питомца
    pet_data = {
        "id": 4,
        "name": "Rocky",
        "status": "available"
    }
    create_response = client.add_pet(pet_data)
    assert create_response.status_code == 200, f"Failed to create pet: {create_response.status_code}"

    # Удаляем питомца
    response = client.delete_pet(4)
    logger.info(f"Response: {response.status_code}")

    # Проверяем статус-код
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверяем, что питомец действительно удален
    get_response = client.get_pet_by_id(4)
    assert get_response.status_code == 404, f"Expected status code 404, but got {get_response.status_code}"