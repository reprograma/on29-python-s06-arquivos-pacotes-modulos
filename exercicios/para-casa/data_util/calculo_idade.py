# Importando os módulos datetime e date da biblioteca datetime
from datetime import datetime, date

# Criação da função para calcular idade
def calcular_idade(data_nascimento):
    data_atual = date.today()
    data_nasc = datetime.strptime(data_nascimento, '%d/%m/%Y')
    idade = data_atual.year - data_nasc.year - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day))
    return f"Você tem {idade} anos de idade."