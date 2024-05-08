import csv

dados = [['Nome', 'Idade'], ['Fernanda', 34], ['Bobby', 25]]

#abre a pasta pessoas.csv; 
#newline='' deixar uma linha vazia no final do programa  --  BOA PRÁTICA
with open('pessoas.csv', 'w', newline='') as arq_csv:
    #configura o nome do arquivo
    escrita = csv.writer(arq_csv)
    #insere a informação
    escrita.writerows (dados)

#para fazer a leitura
with open('pessoas.csv', 'r') as file_csv:
    file = csv.reader(file_csv)
    for linha in file:
        print(linha)