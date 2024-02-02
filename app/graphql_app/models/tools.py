from typing import Optional, List
import strawberry


@strawberry.type
class Tool:
    id: int
    name: str
    description: str
    use_guide: str
    inserted_at: str
    update_at: str
    active: bool