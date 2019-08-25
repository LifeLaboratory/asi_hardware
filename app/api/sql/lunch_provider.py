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
      , "dateMatched" ::text
      , "dateFinished"::text  
    from Lunch lch
      left join Person p1 on lch."Person" = p1.id
      left join Person p2 on lch."connectionPersonId" = p2.id
    where lch."Person" = {user_id}
      and status = 1
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_id(args):
        query = """
    select 
        row_to_json(p1) "person"
      , row_to_json(p2) "connectionPersonId"
      , status
      , "dateMatched" :text
      , "dateFinished" :text
    from Lunch lch
      left join Person p1 on lch."Person" = p1.id
      left join Person p2 on lch."connectionPersonId" = p2.id
    where lch."Person" = {user_id}
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def set_lunch(args):
        query = """
    insert into Lunch
    (
      "Person",
       "DateCreation",
       status
    )
    values ({user_id}, now(), 0)
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def find_pair(args):
        """
        Находит пару пользователю и обновляет записи у обоих пользователей
        :param args:
        :return:
        """
        query = """
    with get_pair as (
    -- поиск записи пары
      select *
      from Lunch lch
      where 
        status = 0
        and "Person" not in (
          select {user_id}
          union all 
          select "connectionPersonId"
          from Lunch
          where "Person" = {user_id}
            and "connectionPersonId" is not null
        )
      order by "DateCreation"
      limit 1
    ),
    update_id as (
      select lunch_id
        from get_pair
        union all 
        select lunch_id
        from Lunch
        where 
          status = 0
          and "Person" = {user_id} 
    ),
    create_link as (
      -- обновление информации в двух записях
      update Lunch
      set status = 1
        , "connectionPersonId" = 
            case when "Person" = {user_id} 
            then (select "Person" from get_pair) 
            else {user_id} end
        ,  "dateMatched" = now()
      where lunch_id in (
        select lunch_id from update_id
      )
      and coalesce((
        select count(1)
        from update_id
      ), 0) = 2
      returning *
    )
    -- отбор нужной записи
    select *
    from (
      -- отбор нужной записи
      select 
          row_to_json(p1) "person"
        , row_to_json(p2) "connectionPersonId"
        , status
        , "dateMatched" ::text
        , "dateFinished" ::text
      from create_link lch
        left join Person p1 on lch."Person" = p1.id
        left join Person p2 on lch."connectionPersonId" = p2.id
      where lch."Person" = {user_id}  
      union all
      select 
          row_to_json(p1) "person"
        , row_to_json(p2) "connectionPersonId"
        , status
        , "dateMatched" ::text
        , "dateFinished" ::text
      from Lunch lch
        left join Person p1 on lch."Person" = p1.id
        left join Person p2 on lch."connectionPersonId" = p2.id
      where lch."Person" = {user_id} and status = 0 
    ) q
    limit 1 
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def set_lunch_status(args):
        """
        Установка статуса последней записи у пользователя
        :param args:
        :return:
        """
        query = """
    with selected_row as (
      select *
      from lunch
      where
        "Person" = {user_id}
        and status <> 3
      order by "DateCreation" desc
      limit 1
    ),
    associated_row as (
       select *
        from lunch
        where "Person" in (
          select "connectionPersonId"
          from selected_row
        )
        and status <> 3
        order by "DateCreation" desc
        limit 1
    )    
    update lunch
    set status={status}
    where lunch_id in (
      select lunch_id
      from selected_row
      union all
      select lunch_id
      from associated_row
    )
        """
        return Sql.exec(query=query, args=args)

