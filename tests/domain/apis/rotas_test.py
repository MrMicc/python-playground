
from fastapi import APIRouter
from domain.apis.rotas import usuarios_router


# pylint: disable=too-few-public-methods
class TestRotas:

    def test_rotas(self):
        result = usuarios_router
        expected = APIRouter(prefix="/usuarios", tags=["usuarios"])
        assert result.prefix == expected.prefix and result.tags == expected.tags
