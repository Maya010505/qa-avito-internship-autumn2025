import json
from pathlib import Path

class DataProvider:
    """
    Класс DataProvider предназначен для загрузки и предоставления тестовых данных из JSON-файла.
    """

    def __init__(self, div: str, filename: str):
        """
        Загружает данные из указанного JSON-файла.
        """
        base_path = Path(__file__).parent.parent
        file_path = base_path / "test_data" / div / filename
        with open(file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def get_test_case(self, case_name: str):
        """
        Возвращает данные для конкретного тест-кейса.
        """
        return self.data.get(case_name)

    def get_all_test_cases(self):
        """
        Возвращает все тестовые данные из файла в виде списка для параметризации.
        """
        return list(self.data.values())

    def get_test_case_ids(self):
        """
        Возвращает список ключей (ID) для всех тест-кейсов.
        """
        return list(self.data.keys())