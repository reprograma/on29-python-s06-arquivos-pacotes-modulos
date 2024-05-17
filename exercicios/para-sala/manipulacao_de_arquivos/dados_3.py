import csv

dados = [['nome','idade'],['Andrea',30],['marcos', 40 ]]

with open ('pessoas.csv','w',newline ='') as arq_csv:
    escrita = csv.writer (arq_csv)
    escrita.writerows(dados)
    

with open ('pessoas.csv','r') as file_csv:
    file = csv.reader(file_csv)
    for linha in file:
        print(linha)