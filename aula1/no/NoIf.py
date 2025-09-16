from no.NoAST import NoAST

class NoIf(NoAST):
    def __init__(self, condicao, corpo_if, corpo_else=None):
        self.condicao = condicao
        self.corpo_if = corpo_if
        self.corpo_else = corpo_else #Sem elif por enquanto