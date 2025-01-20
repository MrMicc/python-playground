from pydantic import BaseModel

# pylint: disable=too-few-public-methods


class UsuarioModel(BaseModel):
    nome: str
    email: str
