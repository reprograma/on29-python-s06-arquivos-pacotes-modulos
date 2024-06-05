from data_time.calculo_idade import calcular_idade
from data_time.ano_bissexto import eh_ano_bissexto
from data_time.formatar_data import formatar_data
from datetime import datetime


data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
idade = calcular_idade(data_nascimento)
print(f"Você tem {idade} anos.")


ano_atual = datetime.today().year
if eh_ano_bissexto(ano_atual):
    print(f"O ano {ano_atual} é bissexto.")
else:
    print(f"O ano {ano_atual} não é bissexto.")


data = input("Digite uma data (dd/mm/aaaa): ")
data_formatada = formatar_data(data)
print(f"A data formatada é: {data_formatada}")
