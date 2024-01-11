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
    farm_row_number: int
    farm_id: int
    zone_type: str
    length: int
    width: int
    map_x: int
    map_y: int
    indoor: bool
    covered: bool
    inserted_at: str
    updated_at: str
    active: bool
    # zone_icons: Optional[ZoneIconNumbers]

