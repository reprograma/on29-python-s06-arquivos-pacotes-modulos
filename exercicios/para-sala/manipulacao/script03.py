import json

dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}



with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)
    

with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
    