# Exercício 3: Leitura e manipulação de um arquivo CSV
# Crie um arquivo CSV chamado "alunos.csv"
# com informações fictícias de alunos, como nome, idade e nota.
# Escreva um programa em Python que leia o arquivo CSV,
# calcule a média das notas e exiba-a na tela.

import csv

dados = [["Ana", 10], ["Carol", 8], ["Andre", 5]]

with open('notas.csv', 'w', newline='') as aluno_csv:
    escritor = csv.writer(aluno_csv)
    escritor.writerows(dados)

with open('notas.csv', 'r') as file_csv:
    file = csv.reader(file_csv)
    notas = []

    for linha in file:
        nota = int(linha[1])
        notas.append(nota)
    print(notas)

print(sum(notas) / len(notas))
