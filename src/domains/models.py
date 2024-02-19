from dataclasses import dataclass, asdict, field
from datetime import datetime


@dataclass
class BaseModel:
    id: int = field(init=False, default_factory=int)
    created_at: datetime = field(init=False, default=None)
    updated_at: datetime = field(init=False, default=None)

    
    def to_dict(self):
        return asdict(self)

@dataclass(unsafe_hash=True)
class Category(BaseModel):
    title: str


@dataclass(unsafe_hash=True)
class Product(BaseModel):
    title: str
    description: str
    price: float


@dataclass(unsafe_hash=True)
class City(BaseModel):
    name: str
