import json
from dataclasses import dataclass

import requests


@dataclass
class TeamLead:  #Удобнее обращяться с данными для обращения через точку
    name: str
    description: str
    skills: str
    employer: str
    salary: str
    area: str
    published_date: str

def create_vacancy_description(vacancy): # Описание вакансии и есть ли отвественность
    description = ""
    description += f"Тип Вакансии: {vacancy['type']['name']}\n"
    description += vacancy.get("snippet", {}).get("responsibility", "")
    return description

def get_vacancy_employer(vacancy): # Получаем название вакансии и проверяем его
    employer = ""
    employer += f'Название: {vacancy.get("employer", {}).get("name", "")}\n'
    employer += f'Сайт: {vacancy.get("employer", {}).get("alternate_url", "")}\n'
    employer += f'Доверие: {"есть" if vacancy.get("employer", {}).get("trusted", "") else "нету"}\n'

    return employer

def get_vacancy_salary(vacancy): # Проверяем зарплату
    salary = ""
    if vacancy.get("salary", {}):
        salary += f"От {vacancy['salary']['from']} "
        if vacancy.get("salary", {}).get("to", ""):
            salary += f"до {vacancy['salary']['to']}"
        salary += f" {vacancy['salary']['currency']}"
    else:
        salary += "Не указана"
    return salary

def get_vacancies():  #Перечисление названий вакансий для поиска по API
    vacancy_name = '"team lead"' \
                   ' OR "тимлид"' \
                   ' OR "тим лид"' \
                   'OR "teamlead"' \
                   'OR "lead"' \
                   'OR "руководит"' \
                   'OR "директор"' \
                   'OR "leader"' \
                   'OR "director"' \
                   'OR "начальник"' \
                   'OR "лидер"' \
                   'OR "управляющий проект"' \
                   'OR "керівник"' \
                   'OR "chief"' \
                   'OR "начальник it"'
    req = requests.get(f'https://api.hh.ru/vacancies?text={vacancy_name}'  #Запрос на HH.ru
                       f'&area=113'
                       f'&page=0'
                       f'&per_page=10'
                       f'&date_from=2022-12-21'
                       f'&date_to=2022-12-22')
    data = req.content.decode("utf-8")
    req.close()
    jsObj = json.loads(data)

    vacancies = []

    for item in jsObj['items']: #Создаём объект и заполняем данными
        team_lead = {} #Питоновский словарь
        team_lead['name'] = item['name']
        team_lead['description'] = create_vacancy_description(item)
        team_lead['skills'] = item['snippet']['requirement'] or "Нет"
        team_lead['employer'] = get_vacancy_employer(item)
        team_lead['salary'] = get_vacancy_salary(item)
        team_lead['area'] = item['area']['name']
        team_lead['published_date'] = item['published_at']

        vacancies.append(TeamLead(**team_lead)) # Распоковываем словарь по ключам, создаём дата класс и добовляем в список вакансий

    return vacancies