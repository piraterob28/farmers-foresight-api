import datetime

from sqlalchemy import text, null
from sqlalchemy.sql import func
from typing import List
from app.graphql_app.context import engine
from sqlalchemy.orm import Session, aliased
from app.dal.schema import Chore, DailyChoreList, Row, RowBatch, Zone
from app.graphql_app.models.chores import ChoreData, ChoreType, DailyChore


def get_chore_list_one_zone(chore_catagory: str, zone_id: int) -> List[DailyChore]:

    if chore_catagory == 'late chores':

        with engine.connect() as conn:
            with Session(engine) as sess:
                chores = sess.query(DailyChoreList)\
                    .join(Chore, DailyChoreList.chore_id == Chore.id)\
                    .join(RowBatch, Chore.row_batch_id == RowBatch.id)\
                    .join(Row, RowBatch.row_id == Row.id)\
                    .join(Zone, Row.zone_id == Zone.id)\
                    .where(Zone.id == zone_id)\
                    .where(DailyChoreList.completed.is_(False))\
                    .where(DailyChoreList.todo_date < datetime.datetime.now())\
                    .all()

                for chore in chores:
                    average_chore_time = sess.query(func.avg(DailyChoreList.time_end - DailyChoreList.time_start))\
                        .join(Chore, DailyChoreList.chore_id == Chore.id)\
                        .where(Chore.chore_type_id == chore.chore_data.chore_type_id)\
                        .where(DailyChoreList.record_time.is_(True))\
                        .where(DailyChoreList.completed.is_((True)))\
                        .group_by(Chore.chore_type_id)\
                        .one_or_none()

                    average_chore_time_string = str(average_chore_time[0]).split(".")[0] if average_chore_time else None
                    chore.chore_data.chore_type.average_chore_time = average_chore_time_string

                    (zone_number, row_number) = sess.query(Zone.farm_zone_number, Row.row_number)\
                                                    .join(Row, Row.zone_id == Zone.id)\
                                                    .join(RowBatch, RowBatch.row_id == Row.id)\
                                                    .join(Chore, Chore.row_batch_id == RowBatch.id)\
                                                    .where(Chore.id == chore.chore_data.id)\
                                                    .one_or_none()\

                    chore.chore_data.zone_number = zone_number if zone_number else None
                    chore.chore_data.row_number = row_number if row_number else None

        return chores

    if chore_catagory == 'day chores':
        with engine.connect() as conn:
            with Session(engine) as sess:
                chores = sess.query(DailyChoreList) \
                    .join(Chore, DailyChoreList.chore_id == Chore.id) \
                    .join(RowBatch, Chore.row_batch_id == RowBatch.id) \
                    .join(Row, RowBatch.row_id == Row.id) \
                    .join(Zone, Row.zone_id == Zone.id) \
                    .where(Zone.id == zone_id) \
                    .where(DailyChoreList.completed.is_(False)) \
                    .where(DailyChoreList.todo_date >= datetime.datetime.now()) \
                    .all()

                for chore in chores:
                    average_chore_time = sess.query(func.avg(DailyChoreList.time_end - DailyChoreList.time_start)) \
                        .join(Chore, DailyChoreList.chore_id == Chore.id) \
                        .where(Chore.chore_type_id == chore.chore_data.chore_type_id) \
                        .where(DailyChoreList.record_time.is_(True)) \
                        .where(DailyChoreList.completed.is_((True))) \
                        .group_by(Chore.chore_type_id) \
                        .one_or_none()

                    average_chore_time_string = str(average_chore_time[0]).split(".")[0] if average_chore_time else None
                    chore.chore_data.chore_type.average_chore_time = average_chore_time_string

                    (zone_number, row_number) = sess.query(Zone.farm_zone_number, Row.row_number) \
                        .join(Row, Row.zone_id == Zone.id) \
                        .join(RowBatch, RowBatch.row_id == Row.id) \
                        .join(Chore, Chore.row_batch_id == RowBatch.id) \
                        .where(Chore.id == chore.chore_data.id) \
                        .one_or_none()


                    chore.chore_data.zone_number = zone_number if zone_number else None
                    chore.chore_data.row_number = row_number if row_number else None

        return chores

    if chore_catagory == 'late harvest':
        print("late harvest")
        return zone_id

    if chore_catagory == 'day harvest':
        print("day harvest")
        return zone_id


def start_record_task_time(daily_chore_id: int) -> str:
    with Session(engine) as sess:
        sess.query(DailyChoreList)\
            .where(DailyChoreList.id == daily_chore_id)\
            .update({'time_start': datetime.datetime.now()})

        sess.commit()

        updated_daily_chore = sess.query(DailyChoreList.time_start)\
            .where(DailyChoreList.id == daily_chore_id)\
            .one()

        return updated_daily_chore[0]


def end_record_task_time(daily_chore_id: int) -> str:
    with Session(engine) as sess:
        sess.query(DailyChoreList)\
            .where(DailyChoreList.id == daily_chore_id)\
            .update({'time_end': datetime.datetime.now()})

        sess.commit()

        updated_daily_chore = sess.query(DailyChoreList.time_end)\
            .where(DailyChoreList.id == daily_chore_id)\
            .one()

        return updated_daily_chore[0]


def set_record_time(daily_chore_id: int, record_time: bool) -> bool:
    with Session(engine) as sess:
        sess.query(DailyChoreList)\
            .where(DailyChoreList.id == daily_chore_id)\
            .update({'record_time': record_time})

        sess.commit()

        updated_daily_chore = sess.query(DailyChoreList.record_time)\
            .where(DailyChoreList.id == daily_chore_id)\
            .one()

        return updated_daily_chore[0]


def dismiss_record_time(daily_chore_id: int) -> None:
    with Session(engine) as sess:
        sess.query(DailyChoreList)\
            .where(DailyChoreList.id == daily_chore_id)\
            .update({'record_time': False, 'time_start': null(), 'time_end': null()})

        sess.commit()

        return None


def complete_task(daily_chore_id: int, notes: str | None = None) -> bool:
    with Session(engine) as sess:
        sess.query(DailyChoreList)\
            .where(DailyChoreList.id == daily_chore_id)\
            .update({'completed': True, 'notes': notes})

        sess.commit()

        updated_daily_chore = sess.query(DailyChoreList.completed) \
            .where(DailyChoreList.id == daily_chore_id) \
            .one()

        return updated_daily_chore[0]
