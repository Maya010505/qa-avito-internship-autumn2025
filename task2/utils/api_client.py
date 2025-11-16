import requests

class ApiClient:
    """
    Клиент для взаимодействия с API.
    """

    def __init__(self, base_url: str):
        """
        Инициализирует клиент с базовым URL.
        """
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}

    def create_item(self, payload: dict):
        """
        Отправляет POST-запрос на создание объявления.
        """
        url = f"{self.base_url}/api/1/item"
        return requests.post(url, json=payload, headers=self.headers)

    def get_item_by_id(self, item_id: str):
        """
        Отправляет GET-запрос на получение объявления по ID.
        """
        url = f"{self.base_url}/api/1/item/{item_id}"
        return requests.get(url, headers=self.headers)

    def get_statistic_by_id_v1(self, item_id: str):
        """
        Отправляет GET-запрос на получение статистики по ID объявления.
        """
        url = f"{self.base_url}/api/1/statistic/{item_id}"
        return requests.get(url, headers=self.headers)

    def get_items_by_seller_id(self, seller_id: int):
        """
        Отправляет GET-запрос на получение всех объявлений пользователя по sellerID.
        """
        url = f"{self.base_url}/api/1/{seller_id}/item"
        return requests.get(url, headers=self.headers)

    def get_statistic_by_id_v2(self, item_id: str):
        """
        Отправляет GET-запрос на получение статистики для API v2.
        """
        url = f"{self.base_url}/api/2/statistic/{item_id}"
        return requests.get(url, headers=self.headers)

    def delete_item_by_id_v2(self, item_id: str):
        """
        Отправляет DELETE-запрос на удаление объявления для API v2.
        """
        url = f"{self.base_url}/api/2/item/{item_id}"
        return requests.delete(url, headers=self.headers)