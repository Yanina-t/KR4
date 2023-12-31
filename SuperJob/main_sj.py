from SuperJob.sjob import payload_sj
from class_API import HeadHunter, SuperJob, Vacancy
from hh.hh import payload_hh
from payload import Payload

hh_api = HeadHunter()
superjob_api = SuperJob()
vacancy_sort = Vacancy()
payload = Payload()

def platform():
    platforms = ["HeadHunter", "SuperJob", 'Искать на всех платформах']
    print(f'Платформы для поиска вакансий: ')
    for i, vac in enumerate(platforms, 1):
        print('{} - {}'.format(i, vac))
    user_num = int(input('Введите номер: '))
    return user_num


def data_request(platform_n: int):
    if platform_n == 1:
        vacancies_list_hh = hh_api.get_vacancies(payload_hh())
        return vacancies_list_hh
    elif platform_n == 2:
        vacancies_list_sj = superjob_api.get_vacancies(payload_sj())
        return vacancies_list_sj
    else:
        list_vacancy = []
        list_vacancy.extend(payload_hh())
        list_vacancy.extend(payload_sj())
        return list_vacancy


platform_num = platform()
data_request = data_request(platform_num)
data_sort_list = vacancy_sort.sort_payment(data_request)
top_n = vacancy_sort.top_n(data_sort_list)
vacancy_sort.print_vacancy(top_n)
