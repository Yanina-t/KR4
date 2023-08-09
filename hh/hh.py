def payload_hh() -> dict:
    """
    :return: параметры, по которым будет происходить выборка вакансий на сайте
    """
    payloads = {
        'salary': payment_from(),
        'text': keyword(),
        # 'search_field': keywords_keys(),
        'area': town(),
        'page': 0,
    }
    # payloads = {
    #     'salary': 50000,
    #     'text': 'python developer',
    #     'area': 1,
    #     'page': 0,
    # }
    return payloads

def keyword():
    """
    Ключевое слово. Ищет по всей вакансии
    """
    keywords = input('Введите запрос для поиска вакансий: ')
    return keywords

def payment_from():
    """
    :return: Сумма оклада от:
    """
    salary_from = int(input('Сумма оклада от: '))
    return salary_from

def town():
    """
    :return: ID города, в котором будет производиться поиск вакансий
    """
    from hh.dataCounryHH.town_hh import main_town_hh
    return main_town_hh()
