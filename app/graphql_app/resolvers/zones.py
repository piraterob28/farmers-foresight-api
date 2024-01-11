from sqlalchemy import text
from typing import List
from app.graphql_app.context import engine

from app.graphql_app.models.zones import ZoneData


def get_zones() -> List[ZoneData]:
    with engine.connect() as conn:
        result = conn.execute(text("select * from zones"))
        zones = result.all()
        return zones
