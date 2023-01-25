from django.shortcuts import render
from main.models import ProfessionInfo, Page
import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами
import os            # Для работы с файлами

from main.utils import get_vacancies

def index(request):
    page = Page.objects.get(name="Главная")


    return render(request, "main/index.html", {"page": page})

def demand(request):

    page = Page.objects.get(name="Востребованность")

    return render(request, "main/demand.html", {"page": page})

def geography(request):

    page = Page.objects.get(name="География")

    return render(request, "main/geography.html", {"page": page})

def skills(request):

    page = Page.objects.get(name="Навыки")

    return render(request, "main/skills.html", {"page": page})

def last_vacancies(request):  #

    page = Page.objects.get(name="Последние вакансии")
    vacancies = get_vacancies()

    return render(request, "main/last_vacancies.html", {"page": page, "vacancies": vacancies})
