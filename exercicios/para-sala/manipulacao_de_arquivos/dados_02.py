import json

dic =  {'nome': 'Pamella','Sobrenome': 'Fernandes'}

with open('dic.json', 'w') as arq:
    json.dump (dic, arq)

with open ('dic.json','r') as arq:
    dic = json.load(arq)
    print(dic)
