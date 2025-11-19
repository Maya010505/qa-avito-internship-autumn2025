import pytest
from utils.data_provider import DataProvider

# Загрузка тестовых данных
negative_data_provider = DataProvider("api\\v1\\statistic\\", "get_statistic_negative_data.json")
positive_data_provider = DataProvider("api\\v1\\statistic\\", "get_statistic_positive_data.json")


def test_get_statistic_positive(api_client, created_item):
    """
    TC-v1: Позитивный тест. Получение статистики по существующему объявлению.
    Использует фикстуру 'created_item' для получения ID.
    """
    response = api_client.get_statistic_by_id_v1(created_item["id"])

    expected_code = positive_data_provider.get_test_case("TC-1_GetExistingItemStatistic")["expected_status_code"]
    assert response.status_code == expected_code

    response_json = response.json()

    assert isinstance(response_json, list)
    assert len(response_json) == 1

    statistics_data = response_json[0]
    original_statistics = created_item["payload"]["statistics"]

    assert statistics_data["likes"] == original_statistics["likes"]
    assert statistics_data["viewCount"] == original_statistics["viewCount"]
    assert statistics_data["contacts"] == original_statistics["contacts"]

@pytest.mark.parametrize("test_data", negative_data_provider.get_all_test_cases(), ids=negative_data_provider.get_test_case_ids())
def test_get_statistic_negative(api_client, test_data):
    """
    TC-v2, TC-3: Негативные тесты для GET /statistic/:id.
    """
    response = api_client.get_statistic_by_id_v1(test_data["item_id"])

    assert response.status_code == test_data["expected_status_code"]

    response_json = response.json()
    assert "status" in response_json
    assert "result" in response_json