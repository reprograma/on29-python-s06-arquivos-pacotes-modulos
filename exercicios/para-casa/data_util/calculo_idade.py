from datetime import datetime

def calcular_idade(data_nascimento):
    data_atual = datetime.now()
    diferenca = data_atual - data_nascimento

    dias = diferenca.days
    idade = dias//365

    print(f"Você tem {idade} anos.")