
#Crie um arquivo CSV chamado "alunos.csv" com informações fictícias de alunos, como nome, idade e nota. Escreva um programa em Python 
# que leia o arquivo CSV, calcule a média das notas e exiba-a na tela.

# criar o arquivo:

import csv


notas = [['nome','nota1','nota2','nota3'],['pamella', 10, 8, 9],['caio', 7, 5,3]]

with open ('media.csv','w', newline = '') as arq_csv:
    escrita = csv.writer(arq_csv)
    # gravar os dados das notas no arquivo:
    escrita.writerows(notas)


with open ('media.csv','r') as file_csv:
    file = csv.DictReader(file_csv)

# como vamos fazer operações devemos criar uma variavel para guardar os valores:
    notas_pamella = []
    notas_caio = []

    for linha in file:
        if linha['nome'] == 'pamella':
            notas_pamella.extend([int(linha['nota1']), int(linha['nota2']), int(linha['nota3'])])
        elif linha ['nome'] == 'caio':
            notas_caio.extend([int(linha['nota1']), int(linha['nota2']), int(linha['nota3'])])
        
    media_pamella = sum(notas_pamella)/len(notas_pamella)
    media_caio = sum(notas_caio)/len(notas_caio)

    print('Pamella:', media_pamella)
    print('Caio:', media_caio)
    