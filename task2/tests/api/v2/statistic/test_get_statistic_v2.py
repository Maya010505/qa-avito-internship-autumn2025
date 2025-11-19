import pytest
from utils.data_provider import DataProvider

# Загрузка тестовых данных
negative_data_provider = DataProvider("api\\v2\\statistic\\", "get_statistic_negative_data.json")
positive_data_provider = DataProvider("api\\v2\\statistic\\", "get_statistic_positive_data.json")

def test_get_statistic_v2_positive(api_client, created_item):
    """
    TC-v1: Позитивный тест для GET /api/v2/statistic/:id
    """
    response = api_client.get_statistic_by_id_v2(created_item["id"])

    expected_code = positive_data_provider.get_test_case("TC-1_GetExistingItemStatisticV2")["expected_status_code"]
    assert response.status_code == expected_code

    response_json = response.json()
    assert isinstance(response_json, list) and len(response_json) > 0

    statistics_data = response_json[0]
    original_statistics = created_item["payload"]["statistics"]
    assert statistics_data == original_statistics

@pytest.mark.parametrize("test_data", negative_data_provider.get_all_test_cases(), ids=negative_data_provider.get_test_case_ids())
def test_get_statistic_v2_negative(api_client, test_data):
    """
    TC-v2, TC-3: Негативные тесты для GET /api/v2/statistic/:id
    """
    response = api_client.get_statistic_by_id_v2(test_data["item_id"])

    assert response.status_code == test_data["expected_status_code"]

    response_json = response.json()
    assert "status" in response_json
    assert "result" in response_json