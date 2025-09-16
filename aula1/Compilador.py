from AnalisadorLexico import AnalisadorLexico
from AnalisadorSintatico import AnalisadorSintatico

# 1. Abrir arquivo com o código fonte
nome_arquivo = 'codigo_teste.py'
with open(nome_arquivo, 'r', encoding="utf-8") as arquivo_fonte:
    codigo = arquivo_fonte.read()
  
# 2. Análise Léxica
lexer = AnalisadorLexico(codigo)
tokens = lexer.analisar()

# Imprimir o resultado
for token in tokens:
    print(token)

# 3. Análise Sintática 
parser = AnalisadorSintatico(tokens) 
ast_resultado = parser.analisar() 
 
print("\n--- Tabela de Símbolos ---") 
print(parser.tabela_de_simbolos)

print("\n--- AST Resultante (estrutura) ---") 
# Para visualizar a AST, precisamos inspecionar o objeto 
atribuicao_node = ast_resultado.declaracoes[0] 
print(f"Nó principal: {type(atribuicao_node).__name__}") 
print(f"  -> Variável: {atribuicao_node.var.valor}") 
print(f"  -> Valor: {type(atribuicao_node.valor).__name__} com valor {atribuicao_node.valor.valor}")