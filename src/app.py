from fastapi import FastAPI

from database.orm import setup_mapper
from endpoints.healthcheck import router as healtcheck_router
from endpoints.city_controllers import router as city_router


def setup_router(app: FastAPI) -> None:
    app.include_router(city_router)
    app.include_router(healtcheck_router)


app = FastAPI()

setup_mapper()
setup_router(app)
