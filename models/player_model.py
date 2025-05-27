from pydantic import BaseModel
from typing import List, Optional

class Player(BaseModel):
    name: str
    age: Optional[int]
    photo: Optional[str]
    rate: Optional[float]
    city_id: str
    username: str
    password: str
    sports: Optional[List[str]] = []
