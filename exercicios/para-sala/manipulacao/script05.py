import csv

dados= [["alice", 8], ["bob", 10], ["cadu", 7]]

with open("alunos.csv", "w", newline="") as arquivo_csv:
    escrita = csv.writer(arquivo_csv)
    escrita.writerows(dados)

with open("alunos.csv", "r") as file:
    leitor_csv = csv.reader(file)
    notas = []

    for linha in leitor_csv:
        nota = int(linha[1])
        notas.append(nota)

print (sum(notas) / len(notas))