from data_util import calculo_idade, formatar_data, ano_bissexto

# Aparentemente tudo tava certo, mas essa parte do testador não funciona :(

data_nascimento = input("Digite sua data de nascimento: ")
retorno_calculo = calculo_idade.calcular_idade(data_nascimento)
print(retorno_calculo)

data_inserida = input("Digite a data a ser validada (ex: dd/mm/YYYY): ")
data_formatada = formatar_data.formatar_data()
print(data_formatada)

validar_bissexto = int(input("Digite o ano a ser validado: "))
ano = ano_bissexto.ano_bissexto()
print(ano)
