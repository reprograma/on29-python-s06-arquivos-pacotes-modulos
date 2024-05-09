import csv

dados = [["nome", "idade"],["Alice", 30],["bob", 25]]

with open ("pessoas.csv", "w", newline = "") as arq_csv:
    escrita = csv.writer(arq_csv)
    escrita.writerows (dados)

