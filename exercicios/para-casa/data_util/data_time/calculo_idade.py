from datetime import datetime

def calcular_idade(data_nascimento):
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    data_atual = datetime.now()
    diferenca = data_atual - data_nascimento
    idade = diferenca.days // 365
    return calcular_idade

data_nascimento = input("Por favor, insira sua data de nascimento no formato dd/mm/aaaa: ")
idade = calcular_idade(data_nascimento)
print("Sua idade é:", idade)
