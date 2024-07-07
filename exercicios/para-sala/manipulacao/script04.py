import csv

#parte 1
dados = [['nome', 'idade'], ['Alice', 30], ['bob', 25]]

with open('pessoas.csv', 'w', newline='') as arq_csv: #aqui eu faço a abertura
    escrita = csv.writer(arq_csv) #aqui eu passo o nome desse arquivo para dentro desse método (csv.writer)
    escrita.writerows(dados) #persiste a informação, faz a escrita de fato, adiciona os dados da nossa lista ao arquivo csv

#parte 2 - exibir os dados
with open('pessoas.csv', 'r') as file_csv:
    file = csv.reader(file_csv)
    for linha in file:
        print(linha)