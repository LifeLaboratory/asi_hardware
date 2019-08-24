# coding=utf-8
from app.api.sql.profile_provider import Provider


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

def get_profile (user_data):
    provider = Provider()
    return base_func(provider.get_profile, user_data)

def set_profile(user_data):
    provider = Provider()
    return base_func(provider.set_profile, user_data)

def put_profile(user_data):
    provider = Provider()
    return base_func(provider.put_profile, user_data)