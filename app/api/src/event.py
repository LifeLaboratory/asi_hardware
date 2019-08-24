# coding=utf-8
from app.api.sql.event_provider import Provider


def base_func(provider, user_data):
    '''
    Инкапсуляция общей логики вызова провайдера и обработки ответа
    :provider: провадер (функция, которую планируем вызывать)
    :user_data: данные
    '''
    answer = provider(user_data)
    if isinstance(answer, list):
        answer = answer[0]
    return answer

def event_get(user_data):
    provider = Provider()
    return base_func(provider.get_event, user_data)

def event_get_all(user_data):
    provider = Provider()
    return base_func(provider.get_all_events, user_data)

def event_get_active(user_data):
    provider = Provider()
    return base_func(provider.get_active, user_data)

def event_set(user_data):
    provider = Provider()
    return base_func(provider.set_event, user_data)

def event_put(user_data):
    provider = Provider()
    return base_func(provider.put_event, user_data)

def event_add(user_data):
    provider = Provider()
    return base_func(provider.event_add, user_data)