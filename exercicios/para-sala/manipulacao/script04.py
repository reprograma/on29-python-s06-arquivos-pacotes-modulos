import csv

dados = [['nome', 'idade'], ['Alice', 30], ['Bob', 25]]

# PARTE 1
with open('pessoas.csv', 'w', newline = '') as arq_csv:
    escrita = csv.writer(arq_csv)
    escrita.writerows(dados)

# PARTE 2  
with open('pessoas.csv', 'r') as file_csv:
    file = csv.reader(file_csv)
    for linha in file:
        print(linha)