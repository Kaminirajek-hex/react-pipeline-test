from typing import Optional
from pydantic import BaseModel


class Testing_entity(BaseModel):
    id: Optional[int]

    name: str
    number: int
