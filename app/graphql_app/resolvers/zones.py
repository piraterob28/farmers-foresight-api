from sqlalchemy import text
from typing import List
from app.graphql_app.context import engine
from sqlalchemy.orm import Session
from app.dal.schema import Zone
from app.graphql_app.models.zones import ZoneData, ZoneDataInputs


def get_zones_quick_view() -> List[ZoneData]:
    with engine.connect() as conn:
        result = conn.execute(text("select * from zones"))
        zones = result.all()
        return zones


def set_zones_quick_view(zones_to_update: List[ZoneDataInputs]) -> None:
    print('Hit', zones_to_update)
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