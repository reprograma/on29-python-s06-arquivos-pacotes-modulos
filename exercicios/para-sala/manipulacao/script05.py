import csv

dados = [['Maria', 8], ['João', 6], ['Julia', 9], ['Mateus', 5]]

with open('alunos.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

with open('alunos.csv', 'r') as file_csv:
    file = csv.reader(file_csv)

    notas = []
    for linha in file:
        notas.append(int(linha[1]))

    print(f"A média das notas da turma é igual a {sum(notas)/len(notas)}.")