from datetime import datetime
from datetime import timedelta
from datetime import date

def calcular_idade():

    data_atual = date.today()
    data_nascimento_input = input("Informe a sua data de aniversário. Utilize o seguinte formato: dd/mm/aaaa: ")
    data_nascimento = datetime.strptime(data_nascimento_input, "%d/%m/%Y")

    if data_atual.month < data_nascimento.month:
        idade = data_atual.year - data_nascimento.year - 1
    elif data_atual.month == data_nascimento.month:
        if data_atual.day < data_nascimento.day:
            idade = data_atual.year - data_nascimento.year - 1
    else:
        idade = data_atual.year - data_nascimento.year

    print(idade)






