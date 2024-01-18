import datetime

from sqlalchemy import text
from sqlalchemy.sql import func
from typing import List
from app.graphql_app.context import engine
from sqlalchemy.orm import Session, aliased
from app.dal.schema import Chore, DailyChoreList, Row, RowBatch, Zone
from app.graphql_app.models.chores import ChoreData, ChoreType


def get_chore_list_one_zone(chore_catagory: str, zone_id: int) -> List[ChoreData]:

    if chore_catagory == 'late chores':

        with engine.connect() as conn:
            with Session(engine) as sess:
                chores = sess.query(Chore)\
                    .join(DailyChoreList, DailyChoreList.chore_id == Chore.id)\
                    .join(RowBatch, Chore.row_batch_id == RowBatch.id)\
                    .join(Row, RowBatch.row_id == Row.id)\
                    .join(Zone, Row.zone_id == Zone.id)\
                    .where(Zone.id == zone_id)\
                    .where(DailyChoreList.completed.is_(False))\
                    .where(DailyChoreList.todo_date < datetime.datetime.now())\
                    .all()

                for chore in chores:
                    average_chore_time = sess.query(func.avg(DailyChoreList.time_end - DailyChoreList.time_start))\
                        .join(Chore, DailyChoreList.chore_id == chore.id)\
                        .where(Chore.chore_type_id == chore.chore_type_id)\
                        .group_by(Chore.chore_type_id)\
                        .one()

                    chore.chore_type.average_chore_time = average_chore_time[0] if average_chore_time else None

        return chores
    if chore_catagory == 'day chores':
        with engine.connect() as conn:
            with Session(engine) as sess:
                chores = sess.query(Chore) \
                    .join(DailyChoreList, DailyChoreList.chore_id == Chore.id) \
                    .join(RowBatch, Chore.row_batch_id == RowBatch.id) \
                    .join(Row, RowBatch.row_id == Row.id) \
                    .join(Zone, Row.zone_id == Zone.id) \
                    .where(Zone.id == zone_id) \
                    .where(DailyChoreList.completed.is_(False)) \
                    .where(DailyChoreList.todo_date >= datetime.datetime.now()) \
                    .all()

                for chore in chores:
                    average_chore_time = sess.query(func.avg(DailyChoreList.time_end - DailyChoreList.time_start)) \
                        .join(Chore, DailyChoreList.chore_id == chore.id) \
                        .where(Chore.chore_type_id == chore.chore_type_id) \
                        .group_by(Chore.chore_type_id) \
                        .one()

                    chore.chore_type.average_chore_time = average_chore_time[0] if average_chore_time else None

        return chores

    if chore_catagory == 'late harvest':
        print("late harvest")
        return zone_id

    if chore_catagory == 'day harvest':
        print("day harvest")
        return zone_id