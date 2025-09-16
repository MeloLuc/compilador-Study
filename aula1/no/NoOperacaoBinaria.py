from no.NoAST import NoAST

class NoOperacaoBinaria(NoAST):
    def __init__(self, esquerda, op, direita):
        self.esquerda = esquerda
        self.op = op
        self.direita = direita