import pytest
from pydantic import BaseModel
from domain.apis.usuarios.usuario_model import UsuarioModel


class TestUsuarioModel():

    '''
    Dado que é necessário validar o modelo usuário na api 
    quando usuarioModel for invocado 
    então o objeto pydandic devera ser cirado 
    '''
    @pytest.mark.parametrize("nome, email", [("Luiz", "email@email.com")])
    def test_validando_modelo_de_usuario(self, nome, email):
        result = UsuarioModel(nome=nome, email=email)

        assert isinstance(result, BaseModel)

    '''
    Dado que é necessario criar um baseModel com nome e email
    Quando for usarioModel for invocado
    então o objeto deveraconter nome E email 
    '''
    @pytest.mark.parametrize("nome, email", [("Luiz", "email@email.com")])
    def test_criando_modelo_de_usuario(self, nome, email):
        result = UsuarioModel(nome=nome, email=email)

        assert result.nome == nome and result.email == email
