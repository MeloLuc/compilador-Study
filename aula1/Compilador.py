from AnalisadorLexico import AnalisadorLexico

nome_arquivo = 'codigo_teste.py'

with open(nome_arquivo, 'r', encoding="utf-8") as arquivo_fonte:
    codigo = arquivo_fonte.read()
    

lexer = AnalisadorLexico(codigo)
tokens = lexer.analisar()

# Imprimir o resultado
for token in tokens:
    print(token)

