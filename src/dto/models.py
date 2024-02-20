from datetime import datetime

from pydantic import BaseModel


class CityNameDTO(BaseModel):
    name: str


class CityCreateDTO(BaseModel):
    id: int
    name: str
    created_at: datetime
