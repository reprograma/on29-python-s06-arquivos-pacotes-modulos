'''
Exercício 3: Leitura e manipulação de um arquivo CSV

Crie um arquivo CSV chamado "alunos.csv" com informações fictícias de alunos, como nome, idade e nota. Escreva um programa em Python que leia o arquivo CSV, calcule a média das notas e exiba-a na tela.
'''

import csv

dados = [['nome', 'idade', 'nota'], ['fulano', 15, 9.0], ['ciclano', 16, 7.0], ['beltrano', 15, 5.0]]

# Parte 1
with open('alunos.csv', 'w', newline='') as aluno_csv:
    escrita = csv.writer(aluno_csv)
    escrita.writerows(dados)

# Parte 2
with open('alunos.csv', 'r') as aluno_file:
    file = csv.reader(aluno_file)
    notas = []
    
    # Ignorando a primeira linha
    next(file)
    
    for linha in file:
        nota = float(linha[2])
        notas.append(nota)

print(sum(notas) / len(notas))