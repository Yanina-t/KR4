import json

from API_keys import SECRET_KEY_SJOB
import requests

headers = {
    'Host': 'api.superjob.ru',
    'X-Api-App-Id': SECRET_KEY_SJOB,
    'Authorization': 'Bearer r.000000010000001.example.access_token',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def get_country(url: str):
    request = requests.get(url)
    data_json = request.json()
    country_list = []
    for i_t in data_json['objects']:
        contr = f"{i_t['id']} - {i_t['title']}"
        country_list.append(contr)
    with open('country_town_sj.json', "w", encoding='utf8') as json_file:
        json.dump(country_list, json_file, ensure_ascii=False)
    return country_list


def get_town(url: str):
    request = requests.get(url)
    data_json = request.json()
    town_list = []
    for i_t in data_json['objects']:
        contr = f"{i_t['id']} - {i_t['title']}"
        town_list.append(contr)
    with open('town_sh.json', "w", encoding='utf8') as json_file:
        json.dump(town_list, json_file, ensure_ascii=False)
    return town_list


def print_id(list_date):
    for i in list_date:
        print(i)
    ID = input('Введите ID: ')
    return int(ID)


def main_town_sj():
    try:
        url_country = 'https://api.superjob.ru/2.0/countries/'
        list_country = get_country(url_country)
        print(f'Выберите страну для поиска на SuperJob. Введите номер ID из списка:\nID  Наименование\n')
        ID_country = print_id(list_country)
        url_town = f'https://api.superjob.ru/2.0/towns/{ID_country}'
        list_town = get_town(url_town)
        print(f'Выберите город для поиска на SuperJob. Введите номер ID из списка:\nID  Наименование\n')
        return print_id(list_town)
    except ValueError:
        print('Нет такого ID, попробуйте еще.')


# print(main_town_sj())

# url_town = 'https://api.superjob.ru/2.0/towns/'
# list_town = get_town(url_town, ID_country)

# def get_town(url: str, id_country: int):
#     params = {
#         'id_country': id_country
#     }
#     request = requests.get(url, headers=headers, params=params)
#     data_json = request.json()
#     town_list = []
#     for i_t in data_json['objects']:
#         contr = f"{i_t['id']} - {i_t['title']}"
#         town_list.append(contr)
#     return town_list
