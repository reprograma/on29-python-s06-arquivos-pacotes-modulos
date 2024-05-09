from data_util.calculo_idade import calcular_idade
from data_util.ano_bissexto import verificando_ano_bissexto
from data_util.formatar_data import formatar_data

# Cálculo de idade
data_nascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")
idade = calcular_idade(data_nascimento)
print("Sua idade é:", idade)

# Verificação de ano bissexto
ano_atual = int(input("Digite o ano atual: "))
if verificando_ano_bissexto(ano_atual):
    print("O ano atual é bissexto.")
else:
    print("O ano atual não é bissexto.")

# Formatação de data
data = input("Digite uma data (dd/mm/aaaa): ")
data_formatada = formatar_data(data)
print("Data formatada:", data_formatada)