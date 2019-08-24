from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_active_id(args):
        query = """
    select 
        p1::json "person"
      , p2::json "connectionPersonId"
      , "Status" as "status"
      , "DateMatch" as "dateMatched"
      , "DateEnd" as "dateFinished"     
    from Lanch lch
      left Person p1 on lch."Person" = p1."@Person"
      left Person p2 on lch."ConnectedPerson" = p2."@Person"
    where lch."Person" = {user_id}
      and lch."DateEnd" is not null
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_id(args):
        query = """
    select 
        p1::json "person"
      , p2::json "connectionPersonId"
      , "Status" as "status"
      , "DateMatch" as "dateMatched"
      , "DateEnd" as "dateFinished"     
    from Lanch lch
      left Person p1 on lch."Person" = p1."@Person"
      left Person p2 on lch."ConnectedPerson" = p2."@Person"
    where lch."Person" = {user_id}
                """
        return Sql.exec(query=query, args=args)
