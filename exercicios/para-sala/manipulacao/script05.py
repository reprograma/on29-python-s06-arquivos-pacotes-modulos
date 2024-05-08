import csv

dados = [["Lorena", 10], ["Roberta", 8]]

with open("alunos.csv", "w", newline= "") as aluno_csv:
    escritor_csv = csv.writer(aluno_csv)
    escritor_csv.writerows(dados)
    
with open("alunos.csv") as aluno_file:
    leitor_csv = csv.reader(aluno_file)
    notas = []
    
    for coluna in leitor_csv:
        nota = int(coluna[1])
        notas.append(nota)
        
print(sum(notas)/len(notas))

