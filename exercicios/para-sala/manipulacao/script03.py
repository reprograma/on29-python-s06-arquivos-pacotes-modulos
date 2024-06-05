import json

dados = {"nome": "Carlinha", "idade": 30, "aprendizado": "medio"}

with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json)

with open ("dados.json", "r") as arquivo_json:
    dados =  json.load(arquivo_json)
