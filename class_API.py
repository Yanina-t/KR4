import json
from abc import ABC, abstractmethod
import requests
from API_keys import SECRET_KEY_SJOB


class VacanciesAPI(ABC):
    @abstractmethod
    def get_vacancies(self, payload: dict):
        pass


class HeadHunter(VacanciesAPI):

    def __init__(self):
        self.vacancies_list = []

    def get_vacancies(self, payload: dict):
        url = 'https://api.hh.ru/vacancies'
        request = requests.get(url, payload)
        js_data = request.json()
        for line in js_data['items']:
            dict_vacancy = {
                "link": line['alternate_url'],
                "profession": line['name'],
                "company": line['employer']['name'],
                "town": line['area']['name'],
                "vacancy_description": line['snippet']['responsibility'],
                "experience": line['experience']['name']
            }
            if line['salary'] is not None:
                dict_vacancy['payment_from'] = 0 if line.get('salary').get('from') is None else line.get('salary').get(
                    'from')
            else:
                dict_vacancy['payment_from'] = 0
            self.vacancies_list.append(dict_vacancy)
        return self.vacancies_list


class SuperJob(VacanciesAPI):

    def __init__(self):
        self.vacancies_list = []

    def get_vacancies(self, payload: dict):
        url = 'https://api.superjob.ru/2.0/vacancies'
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': SECRET_KEY_SJOB,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        request = requests.get(url, headers=headers, params=payload)
        js_data = request.json()
        for line in js_data['objects']:
            dict_vacancy = {
                "link": line['link'],
                "profession": line['profession'],
                "company": line['firm_name'],
                "town": line['town']['title'],
                "payment_from": line['payment_from'],
                "vacancy_description": line['candidat'],
                "experience": line['experience']['title'],
            }
            self.vacancies_list.append(dict_vacancy)
        return self.vacancies_list


class Vacancy:
    @staticmethod
    def get_name_for_sort(x):
        """
        :param:
        :return: имя ключа для сортировки списка словарей
        """
        return x['payment_from']

    def sort_payment(self, data_list):
        """
        :return: Отсортированный список по "Оклад от"
        """
        data_sort_list = sorted(data_list, key=self.get_name_for_sort, reverse=True)
        return data_sort_list

    @staticmethod
    def top_n(data_sort_list):
        """
        :return: список топ N вакансий
        """
        num_top_vacancy = int(input('Введите количество вакансий для вывода в топ N: '))
        top_n_sort_list = data_sort_list[:num_top_vacancy]
        with open('vacancy_sort_top.json', "w", encoding='utf8') as json_file:
            json.dump(top_n_sort_list, json_file, ensure_ascii=False)
        return top_n_sort_list


    @staticmethod
    def print_vacancy(array: dict):
        """
        :return: печать информации для пользователя
        """
        for vacancy in array:
            print(f'\nСсылка на вакансию: {vacancy["link"]}\n'
                  f'Название вакансии: {vacancy["profession"]}\n'
                  f'Название организации: {vacancy["company"]}\n'
                  f'Город: {vacancy["town"]}\n'
                  f'Оклад от: {vacancy["payment_from"]}\n'
                  f'Описание вакансии: {vacancy["vacancy_description"][:250]}... и т.д.\n'
                  f'Опыт работы: {vacancy["experience"]}')




    # all_vacancies = []
    #
    # def __init__(self, array: dict):  # data_sort_list
    #     self.__array = array
    #     self.url = self.__array['link']
    #     self.profession = self.__array['profession']
    #     self.company = self.__array['company']
    #     self.town = self.__array['town']
    #     self.payment_from = self.__array['payment_from']
    #     self.vacancy_description = self.__array["vacancy_description"]
    #     self.experience = self.__array['experience']
    #     self.all_vacancies.append(self)
    #
    # def print_vacancy(self, array: dict):
    #     """
    #     :return: печать информации для пользователя
    #     """
    #     for _ in array:
    #         print(f'\nСсылка на вакансию: {self.url},\n'
    #               f'Название вакансии: {self.profession},\n'
    #               f'Название организации: {self.company},\n'
    #               f'Город: {self.town},\n'
    #               f'Оклад от: {self.payment_from},\n'
    #               f'Описание вакансии: {self.vacancy_description[:250]}... и т.д.\n'
    #               f'Опыт работы: {self.experience}')

# if __name__ == "__main__":
#     num = HeadHunter()
#
