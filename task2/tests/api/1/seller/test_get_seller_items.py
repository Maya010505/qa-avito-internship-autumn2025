import pytest
from utils.data_provider import DataProvider

# Загрузка тестовых данных
boundary_data_provider = DataProvider("api\\1\\seller\\", "get_seller_items_boundary_data.json")
negative_data_provider = DataProvider("api\\1\\seller\\", "get_seller_items_negative_data.json")
positive_data_provider = DataProvider("api\\1\\seller\\", "get_seller_items_positive_data.json")

def test_get_seller_items_positive(api_client, created_item):
    """
    TC-1: Позитивный тест. Получение списка объявлений для существующего продавца.
    """
    seller_id = created_item["payload"]["sellerID"]

    response = api_client.get_items_by_seller_id(seller_id)

    expected_code = positive_data_provider.get_test_case("TC-1_GetItemsForExistingSeller")["expected_status_code"]
    assert response.status_code == expected_code

    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) > 0

    found_item = next((item for item in response_json if item["id"] == created_item["id"]), None)
    assert found_item is not None
    assert found_item["name"] == created_item["payload"]["name"]

@pytest.mark.parametrize("test_data",negative_data_provider.get_all_test_cases(),ids=negative_data_provider.get_test_case_ids())
def test_get_seller_items_negative(api_client, test_data):
    """
    TC-2: Негативные тесты.
    """
    response = api_client.get_items_by_seller_id(test_data["sellerID"])
    assert response.status_code == test_data["expected_status_code"]

    response_json = response.json()
    assert "status" in response_json
    assert "result" in response_json

@pytest.mark.parametrize("test_data",boundary_data_provider.get_all_test_cases(),ids=boundary_data_provider.get_test_case_ids())
def test_get_seller_items_boundary(api_client, test_data):
    """
    TC-3, TC-4, TC-5, TC-6: Граничные тесты.
    """
    response = api_client.get_items_by_seller_id(test_data["sellerID"])
    assert response.status_code == test_data["expected_status_code"]

    response_json = response.json()
    if response.status_code == 200:
        assert isinstance(response_json, list)
    else:
        assert "status" in response_json
        assert "result" in response_json