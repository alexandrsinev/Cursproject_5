from src.hhruapi import GetVacansies
from src.work_vacancies import WorkVacancies
import psycopg2
from config import *


def get_company_name(vacancies_list, companies):
    # Создание списка вакансий только от интересующих нас компаний
    company_name_vacancies_list = []
    for i in vacancies_list:
        i_dict = vars(i)
        if i_dict["company_name"] in companies:
            company_name_vacancies_list.append(i_dict)
    return company_name_vacancies_list


def create_bd():
    # создание BD vacancy_data
    db_name = 'vacancies_data'
    params = config(filename)
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    cur.execute(f'CREATE DATABASE {db_name}')

    conn.close()
    params.update({'dbname': db_name})


def filling_bd(company_name_vl):
    # Создание таблицы в BD и наполнение таблицы данными о вакансиях
    db_name = 'vacancies_data'
    params = config(filename)
    conn = psycopg2.connect(dbname=db_name, **params)

    column_table = ('url varchar(100) not null, name varchar(100) not null, company_name varchar(100) not null,'
                    'city varchar(100) not null, salary int, requirement text')
    vacancies_data = []
    for i in company_name_vl:
        rez = (i['vacancy_url'], i['name'], i['company_name'], i['city'], i['salary'], i['requirement'])
        vacancies_data.append(rez)
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f'create table vacancies ({column_table})')
                cur.executemany("insert into vacancies values(%s, %s, %s, %s, %s, %s)", vacancies_data)
    finally:
        conn.close()
