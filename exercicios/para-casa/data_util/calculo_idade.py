# `calculo_idade.py`: Contém uma função calcular_idade(data_nascimento) que recebe uma data de nascimento como argumento e retorna a idade da pessoa.
from datetime import date, datetime

def calcular_idade(data_nascimento):
    data_atual = date.today()
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    idade_diferenca_ano = data_atual.year - data_nascimento.year
    idade_diferenca_mes = data_atual.month - data_nascimento.month
    idade_diferenca_dia = data_atual.day - data_nascimento.day

    idade = idade_diferenca_ano

    if idade_diferenca_mes < 0:
        idade -= 1
    elif idade_diferenca_dia < 0 and idade_diferenca_mes == 0:
        idade -= 1

    return idade
