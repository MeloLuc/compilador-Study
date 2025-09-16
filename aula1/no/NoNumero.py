from no.NoAST import NoAST

class NoNumero(NoAST): 
    def __init__(self, token): 
        self.token = token 
        self.valor = token.valor