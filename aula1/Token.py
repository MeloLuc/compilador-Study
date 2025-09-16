from TipoToken import TipoToken

class Token:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor
        
    def __str__(self):
        return f'Token: < {self.tipo.value}, {self.valor} >'
    
    def __repr__(self):
        # Esta representação ajuda na hora de imprimir a lista de tokens
        return f"Token({self.tipo.name}, {repr(self.valor)})"
        


