from datetime import date
from datetime import datetime

def calcular_idade():
    data_atual = date.today()
    nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
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

calcular_idade()  