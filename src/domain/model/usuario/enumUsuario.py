from enum import Enum


class UsuarioEnum(Enum):
    NOME_INVALIDO = "Nome Invalido!"
    NOME_NAO_PODE_TER_NUMEROS = "Nome Invalido! Não pode conter números!"
    NOME_NAO_PODE_TER_CARACTERES_ESPECIAIS = "Nome Invalido! Nome pode conter caracteres especiais!"
    NOME_NAO_PODE_SER_MENOR_QUE_3_CHAR = "Nome Invalido! Nome deve ter pelo menos 3 caracteres"
    NOME_PRECISA_SER_STRING = "Nome invalido! Nome precisa ser do tipo String"

    EMAIL_NAO_PODE_COMECAR_OU_TERMINAR_COM_CARACTERES_ESPECIAIS = "Email Invalido! Email nao pode comecar ou terminar com caracteres especiais!"
    EMAIL_DEVE_CONTER_ARROBA = "Email Invalido! Email deve conter @"
    EMAIL_NAO_PODE_CONTER_MAIS_QUE_UM_ARROBA = "Email Invalido! Email nao pode conter mais de um @!"
    EMAIL_DEVE_CONTER_PONTOS_APOS_ARROBA = "Email Invalido! Email deve conter ponto apos o @!"
    EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_ANTES_ARROBA = "Email Invalido! Email deve conter mais de 2 caracteres antes do @!"
    EMAIL_DEVE_TER_PELO_MENOS_2_CARACTERES_DEPOIS_ARROBA = "Email Invalido! Email deve conter mais de 2 caracteres depois do @!"

    CARACTERES_ESPECIAIS = "@#$%^&*()-+?_=,<>!/."


