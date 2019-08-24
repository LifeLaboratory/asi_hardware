from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def check_user(args):
        query = """
  select 1
  from Pesrson
  where ("login" = '{login}'
    and "password" = '{password}'
    )
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def register_user(args):
        query = """
    insert into "Person"("login", "password", "Name") 
    VALUES ('{login}', 
    '{password}', 
    '{name}')
    returning "@Person"
    """
        print(query)
        return Sql.exec(query=query, args=args)
