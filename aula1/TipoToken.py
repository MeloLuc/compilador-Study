import enum

class TipoToken(enum.Enum):
    # Palavras-chave
    IF = "PALAVRA_CHAVE_IF"
    ELIF = "PALAVRA_CHAVE_ELIF"
    ELSE = "PALAVRA_CHAVE_ELSE"
    WHILE = "PALAVRA_CHAVE_WHILE"
    TRUE = "PALAVRA_CHAVE_TRUE"
    FALSE = "PALAVRA_CHAVE_FALSE"
    
    # Identificadores e Literais
    IDENTIFICADOR = "IDENTIFICADOR"
    NUMERO_INTEIRO = "NUMERO_INTEIRO"
    STRING = "STRING"
    
    # Operadores
    ATRIBUICAO = "ATRIBUICAO" # =
    IGUALDADE = "IGUALDADE" # ==
    MAIOR = "MAIOR" # >
    MENOR = "MENOR" # <
    MAIOR_IGUAL = "MAIOR_IGUAL" # >=
    MENOR_IGUAL = "MENOR_IGUAL" # <=
    SOMA = "SOMA" # +   
    SUBTRACAO = "SUBTRACAO" # -
    MULTIPLICACAO = "MULTIPLICACAO" # *
    DIVISAO = "DIVISAO" # /
    
    # Pontuação e Delimitadores
    DOIS_PONTOS = "DOIS_PONTOS" # :
    
    # Fim do arquivo
    EOF = "EOF" # End of File

