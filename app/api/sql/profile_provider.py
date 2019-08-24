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
      "role", 
      "birthDate", 
      company, 
      about, 
      photo, 
      city, 
      contacts
    )
    values (
        {first_name} -- firstName
      , {last_name} -- lastName
      , coalesce({role}, 0) -- role
      , coalesce({birth_day}, now()) -- birthDate
      , {company} -- company
      , {about} -- about
      , {photo} -- photo
      , {city} -- city
      , {contacts} -- contacts
    )
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_profile(args):
        query = """
    update person
    set firstName = {first_name}
      , lastName = {last_name}
      , "role" = coalesce({role}, 0)
      , "birthDate" = coalesce({birth_day}, now())
      , company = {company}
      , about = {about}
      , photo = {photo}
      , city = {city}
      , contacts = {contacts}
    where id = {id_user}
        """
        return Sql.exec(query=query, args=args)
