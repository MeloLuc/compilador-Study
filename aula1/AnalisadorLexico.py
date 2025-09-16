from TipoToken import TipoToken
from Token import Token

class AnalisadorLexico:
    def __init__(self, codigo_fonte):
        self.codigo = codigo_fonte
        self.posicao = 0
        self.tokens = []
        self.palavras_chave = {
            "if": Token(TipoToken.IF, "if"),
            "elif": Token(TipoToken.ELIF, "elif"),
            "else": Token(TipoToken.ELSE, "else"),
            "while": Token(TipoToken.WHILE, "while"),
            "True": Token(TipoToken.TRUE, True),
            "False": Token(TipoToken.FALSE, False),
            }
    
    def analisar(self):
        # Loop principal que gera todos os tokens
        print("\nIniciando análise léxica...\n")
        
        while self._caractere_atual() is not None:
            char = self._caractere_atual()
            
            # 1. Ignorar espaços em branco (espaço, tab, nova linha)
            if char.isspace():
                self._avancar()
                continue
            
            # 2. Reconhecer números inteiros
            if char.isdigit():
                numero_str = ""
                # enquanto não acaba o arquivo e o caracter é um digito
                while self._caractere_atual() is not None and self._caractere_atual().isdigit():
                    numero_str += self._caractere_atual()
                    self._avancar()
                self.tokens.append(Token(TipoToken.NUMERO_INTEIRO, int(numero_str)))
                continue            
          
            # 3. Reconhecer Identificadores e Palavras-chave
            if char.isalpha() or char == '_':
                identificador = ""
                
                while self._caractere_atual() is not None and (self._caractere_atual().isalnum() or self._caractere_atual() == '_'):
                    identificador += self._caractere_atual()
                    self._avancar()
                    
                # É uma palavra-chave ou um identificador?
                token = self.palavras_chave.get(identificador)
                
                if token:
                    self.tokens.append(token)
                else:
                    self.tokens.append(Token(TipoToken.IDENTIFICADOR, identificador))
                continue          
            
            # 4. Reconhecer Strings (simplificado, com aspas duplas)
            # (Exercício para os alunos completarem a lógica com aspas simples)

            if char == '"':
                self._avancar() # Pula a primeira aspa
                string_literal = ""
                
                while self._caractere_atual() is not None and self._caractere_atual() != '"':
                    string_literal += self._caractere_atual()
                    self._avancar()
                    
                self._avancar() # Pula a última aspa
                self.tokens.append(Token(TipoToken.STRING, string_literal))
                continue

            if char == "'":
                self._avancar() # Pula a primeira aspa
                string_literal = ""
                
                while self._caractere_atual() is not None and self._caractere_atual() != "'":
                    string_literal += self._caractere_atual()
                    self._avancar()
                    
                self._avancar() # Pula a última aspa
                self.tokens.append(Token(TipoToken.STRING, string_literal))
                continue         

            # 5. Reconhecer Operadores e Pontuação
            if char == '=':
                # Olhamos um caractere à frente para ver se é '=='
                if self.posicao + 1 < len(self.codigo) and self.codigo[self.posicao + 1] == '=':
                    self._avancar()
                    self._avancar()
                    self.tokens.append(Token(TipoToken.IGUALDADE, "=="))
                else:
                    self._avancar()
                    self.tokens.append(Token(TipoToken.ATRIBUICAO, "="))
                continue
            
            if char == '>':
                if self.posicao + 1 < len(self.codigo) and self.codigo[self.posicao + 1] == '=':
                    self._avancar()
                    self._avancar()
                    self.tokens.append(Token(TipoToken.MAIOR_IGUAL, ">="))
                else:
                    self._avancar()
                    self.tokens.append(Token(TipoToken.MAIOR, ">"))
                continue
        
            if char == '<':
                if self.posicao + 1 < len(self.codigo) and self.codigo[self.posicao + 1] == '=':
                    self._avancar()
                    self._avancar()
                    self.tokens.append(Token(TipoToken.MENOR_IGUAL, "<="))
                else:
                    self._avancar()
                    self.tokens.append(Token(TipoToken.MENOR, "<"))
                continue
        
            if char == '+':
                self._avancar()
                self.tokens.append(Token(TipoToken.SOMA, "+"))
                continue
        
            if char == '-':
                self._avancar()
                self.tokens.append(Token(TipoToken.SUBTRACAO, "-"))
                continue
        
            if char == '*':
                self._avancar()
                self.tokens.append(Token(TipoToken.MULTIPLICACAO, "*"))
                continue
        
            if char == '/':
                self._avancar()
                self.tokens.append(Token(TipoToken.DIVISAO, "/"))
                continue
        
            if char == ':':
                self._avancar()
                self.tokens.append(Token(TipoToken.DOIS_PONTOS, ":"))
                continue
        
            # Se nenhum token foi reconhecido, é um caractere inválido
            raise ValueError(f"Caractere inválido encontrado: '{char}'") #impleementar erro por linha
        
        # Adiciona um token EOF (End of File) para sinalizar o fim
        self.tokens.append(Token(TipoToken.EOF))
        
        return self.tokens
    
    def _avancar(self):
        self.posicao += 1
        
    def _caractere_atual(self):
        if self.posicao < len(self.codigo):
            return self.codigo[self.posicao]
        return None # Retorna None se chegamos ao fim