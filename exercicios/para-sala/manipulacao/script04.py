import csv

# parte 1
dados = [['nome', 'idade'], ['Alice', 33], ['bob', 25]]

with open('pessoas.csv', 'w', newline='') as arq_csv:
    escrita = csv.writer(arq_csv)
    escrita.writerows(dados)
    
# parte 2 - exibir os dados
with open('pessoas.csv', 'r') as file_csv:
    file = csv.reader(file_csv)
    for linha in file:
        print(linha)