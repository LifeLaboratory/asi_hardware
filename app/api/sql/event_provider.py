# coding=utf-8
from app.api.base.base_sql import Sql

class Provider:

    @staticmethod
    def get_all_events(args):
        query = """
    select *
      , (
          select count(1) 
          from event_person ep 
          where ep.event_id = e.event_id
        ) count_person
    from event e
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
      "date",
      creator,
      max_person
    )
    values (
      {title},
      {place},
      {photo},
      {description},
      {date}::text,
      {creator},
      {maxPerson}
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
      "date" = {date}::text
    where event_id = {eventId}
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_active(args):
        """
        метод возвращающий активные на текущий момент ивенты
        :param args:
        :return:
        """
        query = """
    select *
      , (
          select count(1) 
          from event_person ep 
          where ep.event_id = e.event_id
        ) count_person
    from event
    where "date"::date >= now()::date
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_event(args):
        """
        метод возвращающий данные конкретного ивента
        :param args:
        :return:
        """
        query = """
    select *
      , (
          select count(1) 
          from event_person ep 
          where ep.event_id = e.event_id
        ) count_person
    from event
    where event_id = {eventId}
                """
        return Sql.exec(query=query, args=args)

