from datetime import date
from datetime import datetime


def calcular_idade():
        
    data_atual = date.today()
    # print(data_atual.year)

    data_nascimento = input("Digite sua data de nascimento ex:08/02/2005: ")
    data = datetime.strptime(data_nascimento, "%d/%m/%Y")
    # print(data_atual.year - data.year)

    if data_atual.month < data.month:
        idade = data_atual.year - data.year - 1
        print(idade)
    elif data_atual.month == data.month:
        if data_atual.day < data.day:
            idade = data_atual.year - data.year - 1
            print(idade)
        else:
            idade = data_atual.year - data.year
            print(idade)
            
    else:
        idade = data_atual.year - data.year
        print(idade)