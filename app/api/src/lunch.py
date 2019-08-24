# coding=utf-8
from app.api.sql.lunch_provider import Provider


def base_func(provider, user_data):
    '''
    Инкапсуляция общей логики вызова провайдера и обработки ответа
    :provider: провадер (функция, которую планируем вызывать)
    :user_data: данные
    '''
    answer = provider(user_data)
    if isinstance(answer, list) and len(answer) > 0:
        answer = answer[0]
    return answer

def lunch_get_all_id(user_data):
    provider = Provider()
    return base_func(provider.get_all_id, user_data)

def lunch_get_active_id(user_data):
    provider = Provider()
    return base_func(provider.get_active_id, user_data)

def lunch_set(user_data):
    provider = Provider()
    base_func(provider.set_lunch, user_data)
    return base_func(provider.find_pair, user_data)

def lunch_status_set(user_data):
    provider = Provider()
    return base_func(provider.set_lunch_status, user_data)



