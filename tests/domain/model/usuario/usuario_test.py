import pytest
from domain.model.usuario.enum_usuario import UsuarioEnum
from domain.model.usuario.usuario import Usuario
from domain.model.exception.custom_exception import EmailInvalidoError, NomeInvalidoError


class TestUsuario():

    def criar_usuario(self, nome: str = "Teste", email: str = "email@email.com"):
        return Usuario(nome, email)

    @pytest.mark.parametrize("nome", ["Micci", "Luiz", "udy", "João", " Luis", " Marcia ", "vica ", "luiz    felipe", "Luiz Felipe"])
    def test_criando_usuario_dados_minimos(self, nome):
        usuario = self.criar_usuario(nome)
        assert usuario.nome == " ".join(nome.split())

    @pytest.mark.parametrize("nome", ["", None])
    def test_nome_nao_pode_ter_vazio(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert UsuarioEnum.NOME_INVALIDO.value in target.value.messages

    @pytest.mark.parametrize("nome", [123, 123.0])
    def test_nome_precisa_ser_string(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert UsuarioEnum.NOME_PRECISA_SER_STRING.value in target.value.messages

    @pytest.mark.parametrize("nome", ["Mic13ci", "Luiz123", "123"])
    def test_nome_nao_pode_conter_numeros(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert UsuarioEnum.NOME_NAO_PODE_TER_NUMEROS.value in target.value.messages

    @pytest.mark.parametrize("nome", ["n@me", "Lu!z", "Jo@o", "Luis&", "$hirley", "marc*s"])
    def test_nome_nao_pode_conter_caracteres_especiais(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert UsuarioEnum.NOME_NAO_PODE_TER_CARACTERES_ESPECIAIS.value in target.value.messages

    @pytest.mark.parametrize("nome", ["An", "a", "zu", "    a"])
    def test_nome_nao_pode_conter_menos_de_3_caracteres(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert UsuarioEnum.NOME_NAO_PODE_SER_MENOR_QUE_3_CHAR.value in target.value.messages

    @pytest.mark.parametrize("nome",
                             [(
                                 "Aadasdadasdasdasdasdsasdasdsadsasdadadadadsadadsasdasdasdadadada"
                                 "dasdsadasdadadasdadasdasdasdadadadsadadadadadadasdasdasdasdasdasdas"
                                 "dasdasdasdasdasdasdasdasdasadadasdasdasdasdasdasdasdasdasdasdasdasd"
                                 "aisdasdjahdjahsdhsjdhajaskhdshaahudsahduahsaaAA"),

                              ])
    def test_nome_nao_poder_conter_mais_de_245_char(self, nome):
        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)
        assert UsuarioEnum.NOME_TAMANHO_INVALIDO.value in target.value.messages

    @pytest.mark.parametrize("nome", [" 1@   ", "3@"])
    def test_nome_invalido_tamnanho_numero_simbolo(self, nome):
        lista_erros_esperados = []
        lista_erros_esperados.append(
            UsuarioEnum.NOME_NAO_PODE_TER_NUMEROS.value)
        lista_erros_esperados.append(
            UsuarioEnum.NOME_NAO_PODE_TER_CARACTERES_ESPECIAIS.value)
        lista_erros_esperados.append(
            UsuarioEnum.NOME_NAO_PODE_SER_MENOR_QUE_3_CHAR.value)

        with pytest.raises(NomeInvalidoError) as target:
            self.criar_usuario(nome)

        assert target.value.messages == lista_erros_esperados

    """
    ###################### VALIDAÇÕES DO ATRIBUTO EMAIL ####################
    """

    @pytest.mark.parametrize("email", [" email@email.com", "email@mail.com.br", "email@email.cm ", "email@email.com",  "ema@mail.com",
                                       "ema@a.c"])
    def test_email_valido(self, email: str):
        usuario = self.criar_usuario(email=email)
        assert usuario.email == "".join(email.split())

    # validações do atributo email\

    @pytest.mark.parametrize("email", ["", None])
    def test_email_nao_pode_ser_vazio(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert str(target.value) == "Email Invalido!"

    @pytest.mark.parametrize("email", ["emai @email.com", "e mail@ mail.com"])
    def test_email_remover_espacos(self, email: str):
        usuario = self.criar_usuario(email=email)
        assert usuario.email == "".join(email.split())

    # email não pode comecar ou terminar com caracteres especiais
    @pytest.mark.parametrize("email", ["?aaa@email.com", ".email@.com", "!email@.com", ".emai@l.com.",
                                       "email@.com."])
    def test_email_nao_pode_comecar_ou_terminar_com_caracteres_especiais(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert UsuarioEnum.EMAIL_NAO_PODE_COMECAR_OU_TERMINAR_COM_CARACTERES_ESPECIAIS.value in target.value.messages

    """
    quadno email não tiver pelo menos um @
    entao um erro deve ser gerado E informar que email é invalido
    """
    @pytest.mark.parametrize("email", ["email.mail", "email"])
    def test_email_deve_conter_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert UsuarioEnum.EMAIL_DEVE_CONTER_ARROBA.value in target.value.messages

    """
    quando email tiver mais de um @
    entao deve ser gerado um erro E informar que email e invalido
    """
    @pytest.mark.parametrize("email", ["email@email@.com", "email@email@.com", "email@@mail"])
    def test_email_nao_pode_conter_mais_de_um_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert UsuarioEnum.EMAIL_NAO_PODE_CONTER_MAIS_QUE_UM_ARROBA.value in target.value.messages
    """
    quuando o não existir um ponto apos o @
    entao deve ser gerado um erro E informar que email e invalido
    """
    @pytest.mark.parametrize("email", ["email@mail", "meu.email@mail"])
    def test_email_deve_conter_ponto_apos_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert UsuarioEnum.EMAIL_DEVE_CONTER_PONTOS_APOS_ARROBA.value in target.value.messages
    """
    quando email não tiver ao menos 3 caracteres antes do @
    entao deve ser gerado um erro E informar que email e invalido
    """
    @pytest.mark.parametrize("email", ["an@email.com", "a@mail.com.net"])
    def test_email_deve_conter_3_caracteres_antes_do_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert UsuarioEnum.EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_ANTES_ARROBA.value in target.value.messages
    """
    quando email não tiver ao menos 3 caracteres depois do @
    entao deve ser gerado um erro E informar que email e invalido
    """
    @pytest.mark.parametrize("email", ["emai@.a"])
    def test_email_deve_conter_3_caracteres_depois_do_arroba(self, email: str):
        with pytest.raises(EmailInvalidoError) as target:
            self.criar_usuario(email=email)
        assert UsuarioEnum.EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_DEPOIS_ARROBA.value in target.value.messages
    """
    quando email estiver valido 
    então atributo email deve ser igual a email
    """
    @pytest.mark.parametrize("email", ["email@.com", "email@.com.br", "meu+email@mail.com.br", "meu-email@mail.com", "em123@mail.com.net"])
    def test_email_deve_ser_igual_a_email(self, email: str):
        usuario = self.criar_usuario(email=email)
        assert usuario.email == email

    """
    Dado que existem caracteres especiais
    quando eles forem checados pelo sistema
    então eles devem ser dessa lista:  "@#$%^&*()-+?_=,<>!/."

    """
    @pytest.mark.parametrize("caracteres_especiais", ["@#$%^&*()-+?_=,<>!/."])
    def test_verifica_lista_de_caracteres_especiais(self, caracteres_especiais: str):
        usuario = self.criar_usuario()
        assert usuario.caracteres_especiais == caracteres_especiais
