import json

import requests


def get_country(url: str):
    """
    :param url: ссылка для получения списка старн
    :return: список стран, пользователь может выбрать страну для поиска
    """
    request = requests.get(url)
    data_json = request.json()
    list_country = []
    for i_t in data_json:
        contr = f"{i_t['id']} - {i_t['name']}"
        list_country.append(contr)
    with open('country_town_hh.json', "w", encoding='utf8') as json_file:
        json.dump(list_country, json_file, ensure_ascii=False)
    return list_country


def get_town(url: str):
    """
    :param url: ссылка для получения списка городов из ранее выбранной страны
    :return: список городов, пользователь может выбрать город для поиска
    """
    request = requests.get(url)
    data_json = request.json()
    list_tower = []
    for i_t in data_json['areas']:
        contr = f"{i_t['id']} - {i_t['name']}"
        list_tower.append(contr)
    with open('town_hh.json', "w", encoding='utf8') as json_file:
        json.dump(list_tower, json_file, ensure_ascii=False)
    return list_tower



def print_id(list_date):
    try:
        for i in list_date:
            print(i)
        ID = input('Введите ID: ')
        return int(ID)
    except TypeError:
        print('Нет такого ID, попробуйте еще.')


def main_town_hh():
    try:
        url_country = 'https://api.hh.ru/areas'
        list_country = get_country(url_country)
        print(f'Выберите страну для поиска на HeadHunter. Введите номер ID из списка:\nID  Наименование')
        ID_country = print_id(list_country)
        url_town = f'https://api.hh.ru/areas/{ID_country}'
        list_town = get_town(url_town)
        print(f'Выберите город для поиска на HeadHunter. Введите номер ID из списка:\nID  Наименование')
        return print_id(list_town)
    except ValueError:
        print('Нет такого ID, попробуйте еще.')

# print(main_town_hh())
