
from fastapi import APIRouter

usuarios_router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    # responses={404: {"description": "Not found"}},
)
