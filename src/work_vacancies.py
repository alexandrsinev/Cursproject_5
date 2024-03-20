from src.hhruapi import GetVacansies


class WorkVacancies:
    """
        Класс для обработки ответа с сайта HH.ru и создания списка вакансий
    """
    vacancies_list = []

    def __init__(self, url, name, company_name, city, salary, requirement):
        self.vacancy_url = url
        self.name = name
        self.company_name = company_name
        self.city = city
        self.salary = salary
        self.requirement = requirement

    def __str__(self):
        return (f"\nСсылка на вакансию: {self.vacancy_url}\n"
                f"Вакансия: {self.name}\n"
                f"Название компании: {self.company_name}\n"
                f"Город: {self.city}\n"
                f"Зарплата: {self.salary}\n"
                f"Требования: {self.requirement}\n")

    @classmethod
    def format_vacancies(cls, response):
        """
            Функция возвращает переработанный список вакансий
        """
        for i in response:
            if i["salary"] is None:
                i["salary"] = 'Зарплата не указана'
                continue
            if i["salary"]["from"] is None:
                i["salary"]["from"] = 0
            if i["salary"]["to"] is None:
                i["salary"]["to"] = 0
            if i["published_at"]:
                url = i["alternate_url"]
                name = i["name"]
                company_name = i["employer"]["name"]
                city = i["area"]["name"]
                salary = i["salary"]["from"]
                requirement = i["snippet"]["requirement"]
                instance = cls(url, name, company_name, city, salary, requirement)
                WorkVacancies.vacancies_list.append(instance)

        return cls.vacancies_list
