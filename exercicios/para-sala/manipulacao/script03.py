import json

infos = {
    'nome': 'maria eduarda',
    'idade': 19,
    'cidade': 'santo andre'
}

with open('dados.json', 'w') as arquivo: #escrevendo no arquivo .json (assim como o write, o dump reescreve o arquivo)
    json.dump(infos, arquivo)
    
with open('dados.json', 'r') as arquivo: #lendo (e imprimindo) o arquivo json
    dados = json.load(arquivo)
    print(dados)

#quando tentamos escrever algo em um arquivo que não existe, o arquivo será criado automaticamente!