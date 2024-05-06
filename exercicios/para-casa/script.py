from data_util import ano_bissexto, calculo_idade, formatar_data


ano_atual = int(input("Digite o ano atual: "))
ano = ano_bissexto.eh_ano_bissexto(ano_atual)
print(ano)

data_nascimento = input("Qual sua data de nascimento? (dd/mm/aaaa) ")
resultado = calculo_idade.calcular_idade(data_nascimento)
print(resultado)

data = input("Qual a data? (dd/mm/aaaa) ")
data_formatada = formatar_data.formatar_data(data)
print(data_formatada)