from src.database_management import BDManager

# Функция получает список всех компаний и количество вакансий у каждой компании
# BDManager.get_companies_and_vacancies_count()

# Функция получает список всех вакансий с указанием названия компании,
# названия вакансии и зарплаты и ссылки на вакансию.
# BDManager.get_all_vacancies()

# Функция получает среднюю зарплату по вакансиям.
# BDManager.get_avg_salary()

# Функция получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
BDManager.get_vacancies_with_higher_salary()

# Функция получает список всех вакансий, в названии которых содержатся переданные в метод слова.
# BDManager.get_vacancies_with_keyword('Тестировщик')