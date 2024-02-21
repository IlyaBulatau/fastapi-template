from fastapi import APIRouter


router = APIRouter()


@router.get("/ping", status_code=200, summary="Ping-Pong")
async def ping_pong():
    return "pong"
