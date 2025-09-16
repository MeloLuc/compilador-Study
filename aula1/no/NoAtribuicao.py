from no.NoAST import NoAST

class NoAtribuicao(NoAST):
    def __init__(self, var, valor):
        self.var = var
        self.valor = valor