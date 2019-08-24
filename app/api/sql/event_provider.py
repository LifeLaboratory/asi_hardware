# coding=utf-8
from app.api.base.base_sql import Sql

class Provider:

    @staticmethod
    def get_all_events(args):
        query = """
    select
      event_id,
      Title title,
      Place place,
      Photo photo,
      Description description,
      Date date
    from event
                """
        return Sql.exec(query=query, args=args)


    @staticmethod
    def set_event(args):
        """Добавление нового ивента"""
        pass