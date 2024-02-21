from sqlalchemy import (
    Text,
    Table,
    Column,
    String,
    Integer,
    Numeric,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import registry, relationship
from sqlalchemy.sql import func

from domains.models import City, Product, Category


mapper_registry = registry()


product = Table(
    "products",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, index=True),
    Column("title", String(64), unique=True),
    Column("description", Text),
    Column("price", Numeric(10, 4)),
    Column("category_id", Integer, ForeignKey("categories.id")),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)

category = Table(
    "categories",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, index=True),
    Column("title", String(64), unique=True),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)

city = Table(
    "cities",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, index=True),
    Column("name", String(128), unique=True),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)

city_category = Table(
    "city_category",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("city_id", Integer, ForeignKey("cities.id")),
    Column("category_id", Integer, ForeignKey("categories.id")),
)


def setup_mapper() -> None:
    mapper_registry.map_imperatively(Product, product)
    mapper_registry.map_imperatively(
        Category,
        category,
        properties={
            "products": relationship(Product, backref="category"),
            "cities": relationship(
                City, back_populates="categories", secondary=city_category
            ),
        },
    )
    mapper_registry.map_imperatively(
        City,
        city,
        properties={
            "categories": relationship(
                Category, back_populates="cities", secondary=city_category
            )
        },
    )
