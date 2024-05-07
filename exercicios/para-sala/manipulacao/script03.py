import json

# Dados para o dicionário
dados = {"nome": "Juliana", "idade": 27, "cidade": "Salvador"}

# Escrevendo os dados no arquivo JSON
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo)

# Lendo os dados do arquivo JSON
with open("dados.json", "r") as arquivo:
    dados_lidos = json.load(arquivo)

# Exibindo os dados lidos
print("Dados lidos do arquivo JSON:")
print(dados_lidos)