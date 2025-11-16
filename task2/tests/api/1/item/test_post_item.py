import pytest
from utils.data_provider import DataProvider

# Загрузка тестовых данных
boundary_data_provider = DataProvider("api\\1\\item\\","post_boundary_data.json")
negative_data_provider = DataProvider("api\\1\\item\\", "post_negative_data.json")
positive_data_provider = DataProvider("api\\1\\item\\","post_positive_data.json")

@pytest.mark.parametrize("test_data", boundary_data_provider.get_all_test_cases(), ids=boundary_data_provider.get_test_case_ids())
def test_create_item_boundary(api_client, test_data):
    """
    Граничные тесты для создания объявления.
    """
    # Отправка запроса
    response = api_client.create_item(test_data["payload"])

    # Проверка статус-кода
    assert response.status_code == test_data["expected_status_code"]

    if response.status_code == 200:
        # Проверка структуры успешного ответа
        response_json = response.json()
        assert "id" in response_json
        assert response_json["sellerId"] == test_data["payload"]["sellerID"]
    else:
        # Проверка структуры ответа об ошибке
        response_json = response.json()
        assert "result" in response_json
        assert "status" in response_json
        assert "error" in response_json["status"]

@pytest.mark.parametrize("test_data", negative_data_provider.get_all_test_cases(), ids=negative_data_provider.get_test_case_ids())
def test_create_item_negative(api_client, test_data):
    """
    Негативные тесты для создания объявления.
    """
    # Отправка запроса
    response = api_client.create_item(test_data["payload"])

    # Проверка статус-кода
    assert response.status_code == test_data["expected_status_code"]

    # Проверка структуры ответа об ошибке
    response_json = response.json()
    assert "result" in response_json
    assert "status" in response_json
    assert "message" in response_json["result"]
    assert "messages" in response_json["result"]
    assert response_json["status"] == "error"

@pytest.mark.parametrize("test_data", positive_data_provider.get_all_test_cases(), ids=positive_data_provider.get_test_case_ids())
def test_create_item_positive(api_client, test_data):
    """
    Позитивные тесты для создания объявления.
    """
    # Отправка запроса
    response = api_client.create_item(test_data["payload"])

    # Проверка статус-кода
    assert response.status_code == test_data["expected_status_code"]

    # Проверка структуры ответа
    response_json = response.json()
    assert "id" in response_json
    assert "createdAt" in response_json

    # Проверка соответствия данных в ответе
    for key, value in test_data["payload"].items():
        if key == "sellerID":
            assert response_json["sellerId"] == value
        elif isinstance(value, dict):
            for inner_key, inner_value in value.items():
                assert response_json[key][inner_key] == inner_value
        else:
            assert response_json[key] == value