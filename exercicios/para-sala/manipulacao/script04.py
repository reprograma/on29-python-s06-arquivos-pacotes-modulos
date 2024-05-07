import csv

dados = [['nome', 'idade'], ['alice', 30], ['bob', 25]]

with open('pessoas.csv', 'w', newline='') as arq_csv: #abrindo o arquivo csv para escrita, adicionando aspas vazias ao final (boa prática)
    escrita = csv.writer(arq_csv) #criando um escritor dentro do arquivo csv
    escrita.writerows(dados) #escrevendo de vez os dados no arquivo csv

with open('pessoas.csv', 'r') as file_csv:
    file = csv.reader(file_csv)
    for linha in file:
        print(linha)