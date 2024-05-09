# Crie um arquivo de texto chamado "dados.txt"
# com algumas linhas de texto.
# Escreva um programa em Python que leia o
# conteúdo do arquivo e exiba-o na tela.

with open('dados.txt', 'r') as dados:
    dados = dados.read()
    print(dados)
