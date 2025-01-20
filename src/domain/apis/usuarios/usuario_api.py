

from fastapi import status
from fastapi.responses import JSONResponse
from domain.apis.usuarios.usuario_model import UsuarioModel
from domain.model.exception.custom_exception import EmailInvalidoError, NomeInvalidoError
from domain.model.usuario.usuario import Usuario

# pylint: disable=too-few-public-methods


class UsuarioApi():

    async def create_usuario(self, usuario_model: UsuarioModel) -> JSONResponse:
        try:
            usuario = Usuario(nome=usuario_model.nome,
                              email=usuario_model.email)
            return JSONResponse(content={"message": usuario.to_dict()}, status_code=status.HTTP_201_CREATED)

        except (EmailInvalidoError, NomeInvalidoError) as error:
            return JSONResponse(content={"message": error.messages}, status_code=status.HTTP_400_BAD_REQUEST)
