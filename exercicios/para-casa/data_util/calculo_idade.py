#Contém uma função calcular_idade(data_nascimento) que recebe uma data de nascimento como argumento e retorna a idade da pessoa.

from datetime import datetime

def obter_data_nascimento():
    while True:
        data_nascimento = input("Por favor, insira sua data de nascimento no formato dd/mm/aaaa: ")
        try:
            dia, mes, ano = map(int, data_nascimento.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0:
                return dia, mes, ano
            else:
                print("Por favor, insura uma data válida.")
        except ValueError:
            print("Formato inválido. Certifique-se de inserir a data no formato correto.")

dia, mes, ano = obter_data_nascimento()

def calcular_idade(dia, mes, ano):
    data_agora = datetime.now()
    nascimento = datetime(ano, mes, dia)
    diferenca =  data_agora - nascimento
    idade = diferenca.days // 365
    return idade

idade = calcular_idade(dia, mes, ano)

print(f"Sua idade é de {idade} anos.")