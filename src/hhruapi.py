import json
from abc import ABC, abstractmethod
import requests


class APIHHru(ABC):
    """
    Абстрактный класс для работы с API HH.ru
    """

    @abstractmethod
    def get_vacancies(self, vacancies):
        pass


class GetVacansies(APIHHru):
    url = 'https://api.hh.ru/vacancies'

    def __init__(self):
        self.response = None

    def get_vacancies(self):
        """
        Метод для отправки запроса и получения ответа в виде json
        """
        list_ = []
        for i in range(20):
            params = {
                'industry': "7",
                'enable_snippets': "true",
                'page': i,
                'per_page': 100  # Кол-во вакансий на 1 странице
            }
            response = requests.get(self.url, params)
            response = json.dumps(response.json(), indent=4, ensure_ascii=False)
            response = json.loads(response)
            list_ += response["items"]
        return list_


