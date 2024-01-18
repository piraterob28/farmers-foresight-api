import datetime

from sqlalchemy import text
from typing import List
from app.graphql_app.context import engine
from sqlalchemy.orm import Session, aliased
from app.dal.schema import Chore, DailyChoreList, Row, RowBatch, Zone
from app.graphql_app.models.chores import ChoreData, ChoreType


def get_chore_list_one_zone(chore_catagory: str, zone_id: int) -> List[ChoreData]:

    if chore_catagory == 'late chores':
        print("late chores")

        with engine.connect() as conn:
            with Session(engine) as sess:
                chore_type = sess.query(DailyChoreList).subquery(name='chore_type', with_labels=False, reduce_columns=False)
                chores = sess.query(Chore)\
                    .join(DailyChoreList, DailyChoreList.chore_id == Chore.id)\
                    .join(RowBatch, Chore.row_batch_id == RowBatch.id)\
                    .join(Row, RowBatch.row_id == Row.id)\
                    .join(Zone, Row.zone_id == Zone.id)\
                    .where(Zone.id == zone_id)\
                    .where(DailyChoreList.completed.is_(False))\
                    .where(DailyChoreList.todo_date < datetime.datetime.now())\
                    .all()
        print("chores **************", chores)
        return chores
        # with engine.connect() as conn:
        #     with Session(engine) as sess:
        #         chore_query: List[ZoneData] = sess.query(Zone)\

    if chore_catagory == 'day chores':
        print("day chores")
        return zone_id

    if chore_catagory == 'late harvest':
        print("late harvest")
        return zone_id

    if chore_catagory == 'day harvest':
        print("day harvest")
        return zone_id