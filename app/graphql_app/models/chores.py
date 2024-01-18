from typing import Optional, List
import strawberry


@strawberry.type
class ChoreType:
    id: int
    name: str
    description: str
    tool_ids: Optional[List[str]]
    inserted_at: str
    updated_at: str
    active: bool
    chore_type: str

    #derived
    average_chore_time: Optional[str]


@strawberry.type
class ChoreData:
    id: int
    row_batch_id: int
    recurring: bool
    recurr_type: Optional[str]
    recurr_week_days: Optional[str]
    start_date: str
    inserted_at: str
    updated_at: str
    active: bool
    assigned_to: int
    chore_type_id: int
    chore_type: Optional[ChoreType]
    zone_number: int
    row_number: int
    row_plant_info: str


