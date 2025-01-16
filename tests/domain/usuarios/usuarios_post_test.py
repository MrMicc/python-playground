import pytest
from fastapi import Request, Response, status
from domain.apis.usuarios.usuarios_post import UsuariosAPI


class TestUsuariosPost():

    def __cria_request_usuario(self, nome="Nome", email="email@email.com") -> Request:
        request = Request({"type": "http"})
        # pylint: disable=protected-access
        request._body = b'{"nome": "' + \
            bytes(nome, "utf-8") + b'", "email": "' + \
            bytes(email, "utf-8") + b'"}'
        return request

    '''
    Dado que preciso testar o método post
    quando enviar um request
    E passa o objeto usuário
    então devo receber 200
    '''
    @pytest.mark.asyncio
    @pytest.mark.parametrize("nome, email", [("Luiz Felipe", "email@email.com")])
    async def test_usuarios_post(self, nome, email):
        request = self.__cria_request_usuario(nome, email)

        response = Response()
        result = await UsuariosAPI().post(request, response)

        expected = status.HTTP_200_OK
        expected_result = b'{"message": "Usuario criado com sucesso"}'
        assert result.status_code == expected and result.body == expected_result

    '''
    Dado que preciso testar o método post
    quando enviar um request
    E passa o objeto usuário invalido
    então devo receber 400
    '''
    @pytest.mark.asyncio
    @pytest.mark.parametrize("nome, email", [("Luiz Felipe3", "email@email.com")])
    async def test_usuarios_invalidos_post(self, nome, email):
        request = self.__cria_request_usuario(nome, email)

        response = Response()
        result = await UsuariosAPI().post(request, response)

        expected = status.HTTP_400_BAD_REQUEST
        assert result.status_code == expected

    '''
    Dado que preciso testar validar o método post invalido
    quando enviar um request
    E passar um um usuário invalido
    então devo receber uma msensagem de erro no body
    '''
    @pytest.mark.asyncio
    @pytest.mark.parametrize("nome, email", [("Luiz Felipe3", "email@email.com")])
    async def test_usuarios_invalidos_post_mensagem_erro(self, nome, email):
        request = self.__cria_request_usuario(nome, email)

        response = Response()
        await UsuariosAPI().post(request, response)

        print(response.body)
        expected = b'{"error": "[\'Nome Invalido! N\xc3\xa3o pode conter n\xc3\xbameros!\']"}'
        assert response.body == expected
