import json

dados = {'nome': 'Fernanda', 'idade': 34, 'cidade': 'poneilandia'}

with open ('dados.json', 'w') as file:
    json.dump(dados, file)
    
with open('dados.json', 'r') as file:
    dados = json.load(file)

    print(dados)