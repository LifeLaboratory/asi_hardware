from app.api.sql.profile_provider import Provider


def get_profile(args):

    provider = Provider()
    answer = provider.get_profile(args)
    if isinstance(answer, list):
        answer = answer[0]
    return answer
