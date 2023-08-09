from SuperJob.dataCounry.town_sb import main_town_sj


def payload_sj() -> dict:
    """
    :return: параметры, по которым будет происходить выборка вакансий на сайте
    """
    payloads = {
        'payment_from': payment_from(),
        'keyword': keyword(),
        'keywords': {'keys': keywords_keys()},
        'town': main_town_sj(),
        'count': 100
    }
    return payloads


def keyword():
    """
    Ключевое слово. Ищет по всей вакансии
    """
    keywords = input('Введите запрос для поиска вакансий: ')
    return keywords


def keywords_keys():
    """
    Расширенный поиск ключевых слов. Каждый элемент массива есть массив со следующими параметрами:
    :return list
    """
    words_keys = input('Введите ключевые слова для фильтрации вакансий: ').split()
    return words_keys


def payment_from():
    """
    :return: Сумма оклада от:
    """
    salary_from = int(input('Сумма оклада от: '))
    return salary_from
