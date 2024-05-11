from datetime import date
from datetime import datetime

def calcular_idade():
    
    data_hoje = date.today()

    data_nascimento = input("Digite sua data de nascimento: ")

    data = datetime.strptime(data_nascimento,"%d/%m/%Y")

    return data_hoje.year - data.year
