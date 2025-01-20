import json
from domain.model.exception.custom_exception import EmailInvalidoError, NomeInvalidoError
from domain.model.usuario.enum_usuario import UsuarioEnum


class Usuario():

    __caracter_especiais = UsuarioEnum.CARACTERES_ESPECIAIS.value

    def __init__(self, nome: str, email: str) -> None:
        self.__nome = self.__nome_valido(nome)

        self.__email = self.__email_valido(email)
        # self.__email = "".join(email.split())

    def __nome_valido(self, nome: str) -> str:
        lista_erros = []

        if not nome:
            lista_erros.append(UsuarioEnum.NOME_INVALIDO.value)
        if not isinstance(nome, str):
            lista_erros.append(UsuarioEnum.NOME_PRECISA_SER_STRING.value)
            raise NomeInvalidoError(lista_erros)
        nome = nome.strip()

        if isinstance(nome, str) and any(char.isdigit() for char in nome):
            lista_erros.append(
                UsuarioEnum.NOME_NAO_PODE_TER_NUMEROS.value)
        if any(char in self.__caracter_especiais for char in nome):
            lista_erros.append(
                UsuarioEnum.NOME_NAO_PODE_TER_CARACTERES_ESPECIAIS.value)
        if len(nome) < 3:
            lista_erros.append(
                UsuarioEnum.NOME_NAO_PODE_SER_MENOR_QUE_3_CHAR.value)
        if len(nome) >= 245:
            lista_erros.append(
                UsuarioEnum.NOME_TAMANHO_INVALIDO.value)

        if len(lista_erros) > 0:
            raise NomeInvalidoError(lista_erros)
        nome = " ".join(nome.split())

        return nome

    def __email_valido(self, email: str) -> str:
        lista_erros = []
        character_especiais = self.__caracter_especiais
        if not email:
            raise EmailInvalidoError("Email Invalido!")
        # check se o email começa ou termina com carcter especiais
        if email[0] in character_especiais or email[-1] in character_especiais:
            lista_erros.append(
                UsuarioEnum.EMAIL_NAO_PODE_COMECAR_OU_TERMINAR_COM_CARACTERES_ESPECIAIS.value)
        # check se o email possui @
        if "@" not in email:
            lista_erros.append(
                UsuarioEnum.EMAIL_DEVE_CONTER_ARROBA.value)
        # check se email possuim mais de um @
        else:
            if email.count("@") > 1:
                lista_erros.append(
                    UsuarioEnum.EMAIL_NAO_PODE_CONTER_MAIS_QUE_UM_ARROBA.value)
            # check se o email tem um ponto apos o arroba
            if "." not in email.split("@")[1]:
                lista_erros.append(
                    UsuarioEnum.EMAIL_DEVE_CONTER_PONTOS_APOS_ARROBA.value)
             # check se email possui mais de 3 caracteres antes do arroba
            if len(email.split("@")[0]) < 3:
                lista_erros.append(
                    UsuarioEnum.EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_ANTES_ARROBA.value)
            # check se email possui mais de 3 caracteres depois do arroba
            if len(email.split("@")[1]) < 3:
                lista_erros.append(
                    UsuarioEnum.EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_DEPOIS_ARROBA.value)

        if len(lista_erros) > 0:
            raise EmailInvalidoError(lista_erros)

        email = "".join(email.split())
        return email

    @property
    def caracteres_especiais(self) -> str:
        """This caracters_especiais property."""
        return self.__caracter_especiais

    @property
    def nome(self):
        """The nome property."""
        return self.__nome

    @property
    def email(self) -> str:
        """Email property."""
        return self.__email

    def to_dict(self) -> dict:
        return {
            "nome":  self.__nome,
            "email": self.__email
        }

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=4)
