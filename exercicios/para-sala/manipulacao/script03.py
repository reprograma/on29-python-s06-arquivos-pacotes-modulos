import json

# with open("dados.json", "r") as f:
#     dados = f.read()
    
# print(dados)

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)