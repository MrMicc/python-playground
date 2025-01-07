from domain.model.usuario.enumUsuario import UsuarioEnum
import pytest


class TestUsuarioEnum:

    @pytest.mark.parametrize("enum", ["Nome Invalido!"]) 
    def test_enum_nome_invalido(self, enum: str):
        assert UsuarioEnum.NOME_INVALIDO.value == enum 

    @pytest.mark.parametrize("enaum", ["Nome Invalido! Não pode conter números!"])
    def test_enum_nome_nao_pode_conter_numeros(self, enaum: str):
        assert UsuarioEnum.NOME_NAO_PODE_TER_NUMEROS.value == enaum

    @pytest.mark.parametrize("enum", ["Nome Invalido! Nome pode conter caracteres especiais!"])
    def test_enum_nome_nao_pode_conter_caracteres_especiais(self, enum: str):
        assert UsuarioEnum.NOME_NAO_PODE_TER_CARACTERES_ESPECIAIS.value == enum

    @pytest.mark.parametrize("enum", ["Nome Invalido! Nome deve ter pelo menos 3 caracteres"])
    def test_enum_nome_nao_pode_ser_menor_que_3_char(self, enum: str):
        assert UsuarioEnum.NOME_NAO_PODE_SER_MENOR_QUE_3_CHAR.value == enum

    @pytest.mark.parametrize("enum", ["Nome invalido! Nome precisa ser do tipo String"])
    def test_enum_nome_precisa_ser_string(self, enum: str):
        assert UsuarioEnum.NOME_PRECISA_SER_STRING.value == enum

    @pytest.mark.parametrize("enum", ["Email Invalido! Email nao pode comecar ou terminar com caracteres especiais!"])
    def test_enum_email_nao_pode_comecar_ou_terminar_com_caracteres_especiais(self, enum: str):
        assert UsuarioEnum.EMAIL_NAO_PODE_COMECAR_OU_TERMINAR_COM_CARACTERES_ESPECIAIS.value == enum

    @pytest.mark.parametrize("enum", ["Email Invalido! Email deve conter @"])
    def test_enum_email_deve_conter_arroba(self, enum: str):
        assert UsuarioEnum.EMAIL_DEVE_CONTER_ARROBA.value == enum

    @pytest.mark.parametrize("enum", ["Email Invalido! Email nao pode conter mais de um @!"])
    def test_enum_email_nao_pode_conter_mais_de_um_arroba(self, enum: str):
        assert UsuarioEnum.EMAIL_NAO_PODE_CONTER_MAIS_QUE_UM_ARROBA.value == enum

    @pytest.mark.parametrize("enum", ["Email Invalido! Email deve conter ponto apos o @!"])
    def test_enum_email_deve_conter_ponto_a_pos_arroba(self, enum: str):
        assert UsuarioEnum.EMAIL_DEVE_CONTER_PONTOS_APOS_ARROBA.value == enum


    @pytest.mark.parametrize("enum", ["Email Invalido! Email deve conter mais de 2 caracteres antes do @!"])
    def test_enum_email_deve_ter_mais_de_2_caracteres_antes_arroba(self, enum: str):
        assert UsuarioEnum.EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_ANTES_ARROBA.value == enum

    @pytest.mark.parametrize("enum", ["Email Invalido! Email deve conter mais de 2 caracteres depois do @!"])
    def test_enum_email_deve_ter_mais_de_2_caracteres_depois_arroba(self, enum: str):
        assert UsuarioEnum.EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_DEPOIS_ARROBA.value == enum

