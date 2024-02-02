from typing import Optional, List
import strawberry
from app.graphql_app.models.tools import Tool

@strawberry.type
class ChoreType:
    id: int
    name: str
    description: str
    tool_ids: Optional[List[int]]
    tools: Optional[List[Tool]]
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


@strawberry.type
class DailyChore:
    id: int
    chore_id: int
    chore_batch_id: int
    todo_date: str
    completed: bool
    completed_by: Optional[List[int]]
    record_time: bool
    time_start: Optional[str]
    time_end: Optional[str]
    notes: Optional[str]
    inserted_at: str
    updated_at: str
    active: bool
    chore_data: ChoreData
