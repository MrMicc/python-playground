import json
import pytest
from domain.apis.usuarios.usuario_api import UsuarioApi
from domain.apis.usuarios.usuario_model import UsuarioModel
from domain.model.usuario.enum_usuario import UsuarioEnum


class TestUsuarioApi():

    '''
    Dado que faço uma chamada post em usuarios
    Quando request do tipo em usuarios/
    E um nome e email vier no json
    Então usuario deve ser validado na model
    '''

    @pytest.mark.asyncio
    async def test_criar_usuario_api(self):

        usuario_model = UsuarioModel(nome="Luiz", email="email@email.com")
        api = UsuarioApi()
        result = await api.create_usuario(usuario_model)

        assert result.status_code == 201

        response_content = self.__get_response_content(result.body)

        response_message = response_content.get("message")
        assert response_message == {"nome": "Luiz", "email": "email@email.com"}

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "nome, email, exception",
        [
            ("Luiz1", "email@email.com", UsuarioEnum.NOME_NAO_PODE_TER_NUMEROS),
            ("Luiz Felipe", "email@email",
             UsuarioEnum.EMAIL_DEVE_CONTER_PONTOS_APOS_ARROBA),
            ("1231", "email@mail", UsuarioEnum.NOME_NAO_PODE_TER_NUMEROS)])
    async def test_criar_usuario_api_invalido(self, nome, email, exception):

        usuario_model = UsuarioModel(nome=nome, email=email)
        api = UsuarioApi()
        result = await api.create_usuario(usuario_model)

        assert result.status_code == 400

        response_content = self.__get_response_content(result.body)

        response_message = response_content.get("message", [])
        assert exception.value in response_message

    def __get_response_content(self, body):
        response_content = {}

        if isinstance(body, memoryview):
            response_content = json.loads(
                body.tobytes().decode("utf-8"))
        elif isinstance(body, bytes):
            response_content = json.loads(body.decode("utf-8"))

        return response_content
