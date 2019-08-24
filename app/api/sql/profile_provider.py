# coding=utf-8
from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_profile(args):
        query = """
    select *
    from Person
    where id = {id_user}
    """
        # print(query)
        return Sql.exec(query=query, args=args)

    @staticmethod
    def set_profile(args):
        query = """
    insert into person(
      firstName, 
      lastName, 
      role, 
      "birthDate", 
      company, 
      about, 
      photo, 
      city, 
      contacts
    )
    values (
      {} -- firstName
      , {} -- lastName
      , coalesce({}, 0) -- role
      , coalesce({}, now()) -- birthDate
      , {} -- company
      , {} -- about
      , {} -- photo
      , {} -- city
      , {} -- contacts
    )
        """
