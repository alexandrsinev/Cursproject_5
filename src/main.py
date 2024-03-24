from src.hhruapi import GetVacansies
from src.work_vacancies import WorkVacancies
from src.fuction import *
from src.database_management import BDManager


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = GetVacansies()

# Делаем запрос на HH.ru ответ сjхраняем в переменной response
response = hh_api.get_vacancies()

# Формируем список вакансий
vacancies_list = WorkVacancies.format_vacancies(response)

# Список интересующих нас компаний
company_name_list = ['Caltat', 'Comrade Web Agency', 'Datanomica', 'Flip.kz', 'INGURU.RU', 'INNOVA GROUP',
                     'BestDoctor', 'CRTEX', '4А.Консалтинг', '22Byte']
# Создаем список вакансий только от интересующих нас компаний
company_name_vl = get_company_name(vacancies_list, company_name_list)

# Создаем базу данных "vacancy_data"
create_bd()

# Создаем таблицу vacancies и заполняем ее данными из списка company_name_vl
filling_bd(company_name_vl)

# Функция получает список всех компаний и количество вакансий у каждой компании
#BDManager.get_companies_and_vacancies_count()

# Функция получает список всех вакансий с указанием названия компании,
# названия вакансии и зарплаты и ссылки на вакансию.
# BDManager.get_all_vacancies()

# Функция получает среднюю зарплату по вакансиям.
# BDManager.get_avg_salary()

# Функция получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
#BDManager.get_vacancies_with_higher_salary()

# Функция получает список всех вакансий, в названии которых содержатся переданные в метод слова.
BDManager.get_vacancies_with_keyword('Тестировщик')