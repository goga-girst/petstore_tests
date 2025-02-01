import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PetStoreClient:
    def __init__(self, base_url):
        self.base_url = base_url

    # Методы для Pet API
    def get_pet_by_id(self, pet_id):
        """
        Метод для получения информации о питомце по ID.
        """
        logger.info(f"Fetching pet with ID: {pet_id}")
        response = requests.get(f"{self.base_url}/pet/{pet_id}")
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def add_pet(self, pet_data):
        logger.info(f"Adding pet with data: {pet_data}")
        response = requests.post(f"{self.base_url}/pet", json=pet_data)
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def update_pet(self, pet_data):
        logger.info(f"Updating pet with data: {pet_data}")
        response = requests.put(f"{self.base_url}/pet", json=pet_data)
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def delete_pet(self, pet_id):
        logger.info(f"Deleting pet with ID: {pet_id}")
        response = requests.delete(f"{self.base_url}/pet/{pet_id}")
        logger.info(f"Response status code: {response.status_code}")
        return response

    # Методы для Store API
    def create_order(self, order_data):
        logger.info(f"Creating order with data: {order_data}")
        response = requests.post(f"{self.base_url}/store/order", json=order_data)
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def get_order_by_id(self, order_id):
        logger.info(f"Fetching order with ID: {order_id}")
        response = requests.get(f"{self.base_url}/store/order/{order_id}")
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def delete_order(self, order_id):
        logger.info(f"Deleting order with ID: {order_id}")
        response = requests.delete(f"{self.base_url}/store/order/{order_id}")
        logger.info(f"Response status code: {response.status_code}")
        return response

    def get_store_inventory(self):
        logger.info("Fetching store inventory")
        response = requests.get(f"{self.base_url}/store/inventory")
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    # Методы для User API
    def create_user(self, user_data):
        logger.info(f"Creating user with data: {user_data}")
        response = requests.post(f"{self.base_url}/user", json=user_data)
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def get_user_by_username(self, username):
        logger.info(f"Fetching user with username: {username}")
        response = requests.get(f"{self.base_url}/user/{username}")
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def update_user(self, username, user_data):
        logger.info(f"Updating user with username: {username}")
        response = requests.put(f"{self.base_url}/user/{username}", json=user_data)
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def delete_user(self, username):
        logger.info(f"Deleting user with username: {username}")
        response = requests.delete(f"{self.base_url}/user/{username}")
        logger.info(f"Response status code: {response.status_code}")
        return response