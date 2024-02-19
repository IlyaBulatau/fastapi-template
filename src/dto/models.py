from pydantic import BaseModel

from datetime import datetime


class CityNameDTO(BaseModel):
    name: str

class CityCreateDTO(BaseModel):
    id: int
    name: str
    created_at: datetime