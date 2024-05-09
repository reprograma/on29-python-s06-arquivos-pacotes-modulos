'''
Contém uma função calcular_idade(data_nascimento) que recebe uma data de nascimento como argumento e retorna a idade da pessoa.
'''
from datetime import datetime


def calculo_idade(data_nascimento_str):
    hoje = datetime.now()
    ano_usuario = data_nascimento_str.year
    ano = hoje.year
    idade = ano - ano_usuario

    if (data_nascimento_str.month, data_nascimento_str.day) > (hoje.month, hoje.day):
        idade -= 1
    return idade


data_nascimento_str = input("Digite sua data de nascimento: ")
data_nascimento_str = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

idade = calculo_idade(data_nascimento_str)
print(idade, "anos.")
