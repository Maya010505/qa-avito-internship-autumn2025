import pytest
from utils.data_provider import DataProvider

# Загрузка тестовых данных
negative_data_provider = DataProvider("api\\2\\item\\", "delete_item_negative_data.json")
positive_data_provider = DataProvider("api\\2\\item\\", "delete_item_positive_data.json")

def test_delete_item_v2_positive(api_client, created_item):
    """
    TC-1: Позитивный тест для DELETE /api/2/item/:id
    """
    delete_response = api_client.delete_item_by_id_v2(created_item["id"])

    expected_code = positive_data_provider.get_test_case("TC-1_DeleteItemSuccessfully")["expected_status_code"]
    assert delete_response.status_code == expected_code
    assert delete_response.text == "", "Тело ответа должно быть пустым после успешного удаления"

    get_response = api_client.get_item_by_id(created_item["id"])
    assert get_response.status_code == 404, "Объявление не было удалено: GET-запрос после DELETE не вернул 404"

@pytest.mark.parametrize("test_data", negative_data_provider.get_all_test_cases(), ids=negative_data_provider.get_test_case_ids())
def test_delete_item_v2_negative(api_client, test_data):
    """
    TC-2, TC-3: Негативные тесты для DELETE /api/2/item/:id
    """
    response = api_client.delete_item_by_id_v2(test_data["item_id"])

    assert response.status_code == test_data["expected_status_code"]

    response_json = response.json()
    assert "status" in response_json
    assert "result" in response_json