# coding=utf-8
from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_profile(args):
        query = """
    select *
    from Person
    where id = {user_id}
    """
        print(query)
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
      contacts,
      description
    )
    values (
        {firstName} -- firstName
      , {lastName} -- lastName
      , coalesce({role}, 0) -- role
      , coalesce({birthDay}, now()) -- birthDate
      , {company} -- company
      , {about} -- about
      , {photo} -- photo
      , {city} -- city
      , {contacts} -- contacts
      , {description} -- description
    )
    returning id
        """

        return Sql.exec(query=query, args=args)
