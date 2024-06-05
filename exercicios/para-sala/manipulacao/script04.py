import csv

dados= [["nome","idadde"], ["alice", 30], ["bob", 32]]

with open("pessoas.csv", "w", newline="") as arquivo_csv:
    escrita = csv.writer(arquivo_csv)
    escrita.writerows(dados)

with open("pessoas.csv", "r") as file_csv:
    file = csv.reader(file_csv)
    for linha  in file:
        print(linha)