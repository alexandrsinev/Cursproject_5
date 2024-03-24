import psycopg2
from config import *


class BDManager:
    db_name = 'vacancies_data'
    params = config(filename)
    conn = psycopg2.connect(dbname=db_name, **params)

    @classmethod
    def get_companies_and_vacancies_count(cls):
        try:
            with cls.conn:
                with cls.conn.cursor() as cur:
                    cur.execute('select company_name, count(*) as count_vacancy from Vacancies group by company_name')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            cls.conn.close()

    @classmethod
    def get_all_vacancies(cls):
        try:
            with cls.conn:
                with cls.conn.cursor() as cur:
                    cur.execute('select company_name, name, salary, url from Vacancies')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            cls.conn.close()

    @classmethod
    def get_avg_salary(cls):
        try:
            with cls.conn:
                with cls.conn.cursor() as cur:
                    cur.execute('select avg(salary) from vacancies')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            cls.conn.close()

    @classmethod
    def get_vacancies_with_higher_salary(cls):
        try:
            with cls.conn:
                with cls.conn.cursor() as cur:
                    cur.execute('select * from vacancies where salary > (select avg(salary) from vacancies)')
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            cls.conn.close()

    @classmethod
    def get_vacancies_with_keyword(cls, word):
        try:
            with cls.conn:
                with cls.conn.cursor() as cur:
                    cur.execute(f"select * from vacancies where name like '%{word}%'")
                    rows = cur.fetchall()
                    for row in rows:
                        print(row)
        finally:
            cls.conn.close()
