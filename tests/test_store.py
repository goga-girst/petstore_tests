import pytest
import logging
from utils.api_client import PetStoreClient

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture
def client():
    """Фикстура для создания экземпляра PetStoreClient."""
    return PetStoreClient("https://petstore.swagger.io/v2")

def test_create_order(client):
    """
    Тест для проверки метода POST /store/order.
    Проверяет, что заказ успешно создается.
    """
    logger.info("Starting test_create_order")

    # Данные для создания заказа
    order_data = {
        "id": 1,
        "petId": 10,
        "quantity": 1,
        "shipDate": "2023-10-01T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }

    # Создаем заказ
    response = client.create_order(order_data)
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # Проверяем статус-код и данные
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["id"] == 1, f"Expected order ID 1, but got {response.json()['id']}"
    assert response.json()["status"] == "placed", f"Expected order status 'placed', but got {response.json()['status']}"

def test_get_order_by_id(client):
    """
    Тест для проверки метода GET /store/order/{orderId}.
    Проверяет, что заказ возвращается по ID.
    """
    logger.info("Starting test_get_order_by_id")

    # Сначала создаем заказ
    order_data = {
        "id": 1,
        "petId": 10,
        "quantity": 1,
        "shipDate": "2023-10-01T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    create_response = client.create_order(order_data)
    assert create_response.status_code == 200, f"Failed to create order: {create_response.status_code}"

    # Получаем заказ по ID
    response = client.get_order_by_id(1)
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # Проверяем статус-код и данные
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json()["id"] == 1, f"Expected order ID 1, but got {response.json()['id']}"
    assert response.json()["status"] == "placed", f"Expected order status 'placed', but got {response.json()['status']}"

def test_delete_order(client):
    logger.info("Starting test_delete_order")

    # Сначала создаем заказ
    order_data = {
        "id": 1,
        "petId": 10,
        "quantity": 1,
        "shipDate": "2023-10-01T00:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    create_response = client.create_order(order_data)
    assert create_response.status_code == 200, f"Failed to create order: {create_response.status_code}"

    # Удаляем заказ по ID
    response = client.delete_order(1)
    logger.info(f"Response: {response.status_code}")

    # Проверяем статус-код
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Проверяем, что заказ действительно удален
    get_response = client.get_order_by_id(1)
    assert get_response.status_code == 404, f"Expected status code 404, but got {get_response.status_code}"

def test_get_store_inventory(client):
    logger.info("Starting test_get_store_inventory")

    # Получаем информацию о запасах
    response = client.get_store_inventory()
    logger.info(f"Response: {response.status_code}, {response.json()}")

    # Проверяем статус-код и данные
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert isinstance(response.json(), dict), f"Expected response to be a dictionary, but got {type(response.json())}"