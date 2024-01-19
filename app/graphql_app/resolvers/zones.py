import datetime

from sqlalchemy import text
from typing import List
from app.graphql_app.context import engine
from sqlalchemy.orm import Session
from app.dal.schema import Chore, DailyChoreList, Farm, Harvest, Row, RowBatch, User, Zone
from app.graphql_app.models.zones import ZoneData, ZoneDataInputs, ZoneIconNumbers


def get_zones_quick_view() -> List[ZoneData]:
    #TODO: Remove hard coded values here when passing in context
    user_id = 1
    farm_id = 1
    with engine.connect() as conn:
        with Session(engine) as sess:
            zone_query: List[ZoneData] = sess.query(Zone)\
                .join(Farm, Zone.farm_id == Farm.id)\
                .where(Farm.id == farm_id)\
                .all()

            for zone in zone_query:
                day_chore_number = sess.query(DailyChoreList)\
                    .join(Chore, DailyChoreList.chore_id == Chore.id)\
                    .join(User, Chore.assigned_to == User.id)\
                    .join(RowBatch, RowBatch.id == Chore.row_batch_id)\
                    .join(Row, Row.id == RowBatch.row_id)\
                    .join(Zone, Row.zone_id == Zone.id)\
                    .where(Zone.id == zone.id)\
                    .where(User.id == user_id)\
                    .where(DailyChoreList.todo_date >= datetime.datetime.now())\
                    .where(DailyChoreList.completed.is_(False))\
                    .count()

                late_chore_number = sess.query(DailyChoreList) \
                    .join(Chore, DailyChoreList.chore_id == Chore.id) \
                    .join(User, Chore.assigned_to == User.id) \
                    .join(RowBatch, RowBatch.id == Chore.row_batch_id) \
                    .join(Row, Row.id == RowBatch.row_id) \
                    .join(Zone, Row.zone_id == Zone.id) \
                    .where(Zone.id == zone.id) \
                    .where(User.id == user_id) \
                    .where(DailyChoreList.completed.is_(False)) \
                    .where(DailyChoreList.todo_date <= datetime.datetime.now()) \
                    .count()

                late_harvest_number = sess.query(Harvest) \
                    .join(RowBatch, RowBatch.id == Harvest.row_batch_id) \
                    .join(Row, Row.id == RowBatch.row_id) \
                    .join(Zone, Row.zone_id == Zone.id) \
                    .where(Zone.id == zone.id) \
                    .where(User.id == user_id) \
                    .where(Harvest.completed.is_(False)) \
                    .where(Harvest.harvest_date_planned <= datetime.datetime.now()) \
                    .count()

                day_harvest_number = sess.query(Harvest) \
                    .join(RowBatch, RowBatch.id == Harvest.row_batch_id) \
                    .join(Row, Row.id == RowBatch.row_id) \
                    .join(Zone, Row.zone_id == Zone.id) \
                    .where(Zone.id == zone.id) \
                    .where(User.id == user_id) \
                    .where(Harvest.completed.is_(False)) \
                    .where(Harvest.harvest_date_planned >= datetime.datetime.now()) \
                    .count()

                empty_row_number = sess.query(Row)\
                    .join(Zone, Row.zone_id == Zone.id)\
                    .where(Zone.farm_id == farm_id)\
                    .where(Row.is_planted.is_(False))\
                    .where(Zone.id == zone.id)\
                    .count()

                zone.zone_icons = ZoneIconNumbers(
                    day_chore_number=day_chore_number,
                    late_chore_number=late_chore_number,
                    late_harvest_number=late_harvest_number,
                    day_harvest_number=day_harvest_number,
                    empty_row_number=empty_row_number
                )

            return zone_query








def set_zones_quick_view(zones_to_update: List[ZoneDataInputs]) -> None:
    with Session(engine) as sess:
        for zone in zones_to_update:
            sess.query(Zone).\
                filter(Zone.id == zone.id).\
                update({
                    'map_x': zone.map_x,
                    'map_y': zone.map_y,
                    'length': zone.length,
                    'width': zone.width,
                })

        sess.commit()