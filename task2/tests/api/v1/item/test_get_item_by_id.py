import pytest
from utils.data_provider import DataProvider

# Загрузка тестовых данных
negative_data_provider = DataProvider("api\\v1\\item\\","get_negative_data.json")
positive_data_provider = DataProvider("api\\v1\\item\\","get_positive_data.json")

def test_get_item_positive(api_client, created_item):
    """
    TC-v1: Получение успешно созданного объявления.
    Фикстура 'created_item' приходит из tests/item/conftest.py
    """
    response = api_client.get_item_by_id(created_item["id"])

    assert response.status_code == positive_data_provider.get_test_case("TC-1_GetExistingItem")["expected_status_code"]

    item_data = response.json()[0]
    original_payload = created_item["payload"]

    assert item_data["name"] == original_payload["name"]
    assert item_data["price"] == original_payload["price"]


@pytest.mark.parametrize("test_data",negative_data_provider.get_all_test_cases(),ids=negative_data_provider.get_test_case_ids())
def test_get_item_negative(api_client, test_data):
    """
    TC-v2, TC-3: Негативные тесты для GET-запроса.
    """
    response = api_client.get_item_by_id(test_data["item_id"])
    assert response.status_code == test_data["expected_status_code"]

    response_json = response.json()
    assert "status" in response_json
    assert "result" in response_json