import pytest

from utils.data_provider import DataProvider


@pytest.fixture(scope="module")
def created_item(api_client):
    """
    Создает объявление через POST-запрос для тестов GET, DELETE, PUT.
    """
    data_provider = DataProvider("api\\1\\item\\","post_positive_data.json")
    test_case_data = data_provider.get_test_case("TC-1_ValidData")
    payload = test_case_data["payload"]

    response = api_client.create_item(payload)
    assert response.status_code == 200, "Предусловие не выполнено: не удалось создать объявление"

    response_json = response.json()

    yield {"id": response_json.get("id"), "payload": payload}