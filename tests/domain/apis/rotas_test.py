import pytest
from fastapi import APIRouter, FastAPI, status
from fastapi.testclient import TestClient
from domain.apis.rotas import usuarios_router


# pylint: disable=too-few-public-methods
class TestRotas:

    def test_rotas(self):
        result = usuarios_router
        expected = APIRouter(prefix="/usuarios", tags=["usuarios"])
        assert result.prefix == expected.prefix and result.tags == expected.tags

    @pytest.fixture
    def set_fastapi_test(self) -> FastAPI:
        app = FastAPI()
        app.include_router(usuarios_router)  # Incluindo o router com as rotas
        return app

    @pytest.mark.parametrize("nome, email", [("Luiz", "email@email.com")])
    def test_criar_usuario(self, set_fastapi_test, nome, email):
        client = TestClient(set_fastapi_test)

        result = client.post(
            "/usuarios", json={"nome": nome, "email": email})

        assert result.status_code == status.HTTP_201_CREATED

    @pytest.mark.parametrize("nome, email", [("Luiz 1", "email@email.com"), ("Luiz Felipe", "email@email")])
    def test_criar_usuario_invalidos(self, set_fastapi_test, nome, email):
        client = TestClient(set_fastapi_test)

        result = client.post(
            "/usuarios", json={"nome": nome, "email": email})

        assert result.status_code == status.HTTP_400_BAD_REQUEST
