from typing import Optional
import strawberry


@strawberry.type
class ZoneIconNumbers:
    day_chore_number: Optional[int]
    late_chore_number: Optional[int]
    day_harvest_number: Optional[int]
    late_harvest_number: Optional[int]
    empty_row_number: Optional[int]


@strawberry.type
class ZoneData:
    id: int
    farm_zone_number: int
    farm_id: int
    zone_type: str
    length: float
    width: float
    map_x: float
    map_y: float
    indoor: bool
    covered: bool
    inserted_at: str
    updated_at: str
    active: bool
    # zone_icons: Optional[ZoneIconNumbers]


@strawberry.input
class ZoneDataInputs:
    id: int
    farm_zone_number: Optional[int]
    farm_id: Optional[int]
    length: Optional[float]
    width: Optional[float]
    map_x: Optional[float]
    map_y: Optional[float]
    indoor: Optional[bool]
    covered: Optional[bool]
    inserted_at: Optional[str]
    updated_at: Optional[str]
    active: Optional[bool]



