from TipoToken import TipoToken

class Token:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor
        
    def __str__(self):
        return f'Token: < {self.tipo.value}, {self.valor} >'
    
 
        


