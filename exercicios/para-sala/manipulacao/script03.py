# Crie um dicionário Python com alguns dados e
# escreva-o em um arquivo JSON chamado "dados.json".
# Em seguida, leia o arquivo JSON e exiba os dados lidos.

import json

dados = {"semana": "6", "aula": "01",
         "modulo": "2", "professora": "Leticia"}

with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json)

with open("dados.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
