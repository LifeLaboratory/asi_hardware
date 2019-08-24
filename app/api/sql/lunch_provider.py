# coding=utf-8
from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_active_id(args):
        query = """     
    select 
        row_to_json(p1) "person"
      , row_to_json(p2) "connectionPersonId"
      , status
      , "dateMatched"
      , "dateFinished"  
    from Lunch lch
      left join Person p1 on lch."Person" = p1.id
      left join Person p2 on lch."connectionPersonId" = p2.id
    where lch."Person" = {user_id}
      and lch."dateFinished" is not null
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_id(args):
        query = """
    select 
        row_to_json(p1) "person"
      , row_to_json(p2) "connectionPersonId"
      , status
      , "dateMatched"
      , "dateFinished"  
    from Lunch lch
      left join Person p1 on lch."Person" = p1.id
      left join Person p2 on lch."connectionPersonId" = p2.id
    where lch."Person" = {user_id}
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def set_event(args):
        query = """
    insert into Lunch
    values (
      "Person",
       "DateCreation",
       status
    )
    values ({user_id}, now(), 0)
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def find_pair(args):
        query = """
    with get_pair as (
    -- поиск записи пары
      select *
      from Lunch lch
      where 
        status = 0
        and "Person" <> {user_id}
      order by "DateCreation"
      limit 1
    ),
    create_link as (
      -- обновление информации в двух записях
      update Lunch
      set status = 1
        , "ConnectionPersonId" = case when "Person" = {user_id} then (select "Person" from get_pair) else {user_id} end
        ,  "dateMatched" = now()
      where lunch_id in (
        select lunch_id
        from get_pair
        union all 
        select lunch_id
        from Lunch
        where 
          status = 0
          and "Person" = {user_id}
      )
      returning *
    )
    -- отбор нужной записи
    select 
        p1::json "person"
      , p2::json "connectionPersonId"
      , status
      , dateMatched
      , dateFinished  
    from create_link lch
      left Person p1 on lch."Person" = p1."@Person"
      left Person p2 on lch."ConnectedPerson" = p2."@Person"
    where lch."Person" = {user_id}  
        """
        return Sql.exec(query=query, args=args)
