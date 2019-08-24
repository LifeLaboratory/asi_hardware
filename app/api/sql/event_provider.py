# coding=utf-8
from app.api.base.base_sql import Sql

class Provider:

    @staticmethod
    def get_all_events(args):
        query = """
    select
      event_id,
      title,
      place,
      photo,
      description,
      "date"
    from event
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def set_event(args):
        """Добавление нового ивента"""
        query = """
    insert into event (
      title,
      place,
      photo,
      description,
      "date"
    )
    values (
      {title},
      {place},
      {photo},
      {description},
      {date}
    )
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def put_event(args):
        """
        запрос на обновление ивента
        :param args:
        :return:
        """
        query = """
    update event 
    set
      title = {title},
      place = {place},
      photo = {photo},
      description = {description}, 
      "date" = {date}
    where event_id = {eventId}
                """
        return Sql.exec(query=query, args=args)