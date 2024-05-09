import json

dados = {'nome': 'Alice', 'Idade': 30, 'Estado': 'Acre'}

with open("dados.json", "w") as JsonFile:
    json.dump(dados, JsonFile)

with open("dados.json", "r") as JasonFile:
    dados = json.load(JasonFile)  