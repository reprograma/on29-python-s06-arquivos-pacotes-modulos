import csv

dados = [['Pedro', 12, 7], ['Marla', 13, 9], ['Flavia', 12, 9]]

with open('tabela_alunos.csv', 'w', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerows(dados)

with open('tabela_alunos.csv', 'r') as filecsv:
    leitor_csv = csv.reader(filecsv)
    notas = []
    for linha in leitor_csv:
        nota = int(linha[2])
        notas.append(nota)
print(sum(notas) / len(notas))