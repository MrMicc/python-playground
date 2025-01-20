
from fastapi import APIRouter
from domain.apis.usuarios.usuario_api import UsuarioApi

usuarios_router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    # responses={404: {"description": "Not found"}},
)


usuarios_router.add_api_route(
    "/", UsuarioApi().create_usuario, methods=["POST"])
