
from fastapi import Request, Response, status
from domain.model.usuario.usuario import Usuario
from domain.model.exception.custom_exception import EmailInvalidoError, NomeInvalidoError


# pylint: disable=too-few-public-methods
class UsuariosAPI():

    async def post(self, request: Request) -> Response:
        response = Response()

        try:
            dados_request = await request.json()
            Usuario(
                nome=dados_request["nome"], email=dados_request["email"])

            response.status_code = status.HTTP_200_OK
            response.body = b'{"message": "Usuario criado com sucesso"}'
        except (NomeInvalidoError, EmailInvalidoError) as exception:
            response.status_code = status.HTTP_400_BAD_REQUEST
            response.body = bytes(f'{{"error": "{str(exception)}"}}', "utf-8")
        return response
