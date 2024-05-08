
from datetime import date
from datetime import datetime

def calculo_idade():
    data_atual = date.today()
    nasc = input('Digite aqui sua data de nascimento no formato dd/mm/aaaa: ')
    data_nasc = datetime.strptime(nasc, "%d/%m/%Y")

    if data_atual.month < data_nasc.month:
        idade = data_atual.year - data_nasc.year - 1
        return idade 
    elif data_atual.month == data_nasc.month:
        if data_atual.day < data_nasc.day:
            idade = data_atual.year - data_nasc.year - 1
            return idade
        else:
            idade = data_atual.year - data_nasc.year
            return idade
    else:
        idade = data_atual.year - data_nasc.year
        return idade
