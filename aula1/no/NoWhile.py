from no.NoAST import NoAST

class NoWhile(NoAST):
    def __init__(self, condicao, corpo):
        self.condicao = condicao
        self.corpo = corpo
