import pytest
from utils.api_client import ApiClient

@pytest.fixture(scope="session")
def base_url():
    """Фикстура, которая возвращает базовый URL."""
    return "https://qa-internship.avito.com"

@pytest.fixture(scope="session")
def api_client(base_url):
    """Фикстура для создания клиента API на всю сессию тестов."""
    return ApiClient(base_url)
