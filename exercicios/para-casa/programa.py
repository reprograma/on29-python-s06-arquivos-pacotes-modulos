'''

Crie um programa principal fora do diretório "data_util" para testar o pacote.

Importe os módulos do pacote "data_util" e use as funções para realizar as seguintes tarefas:

Solicite ao usuário que insira sua data de nascimento no formato "dd/mm/aaaa" e use a função do módulo `calculo_idade.py` para calcular a idade da pessoa.

Verifique se o ano atual é bissexto ou não usando a função do módulo `ano_bissexto.py`.

Solicite ao usuário que insira uma data no formato "dd/mm/aaaa" e use a função do módulo formatar_data.py para exibir a data no formato "aaaa-mm-dd".

'''
# verificando ano bissexto
from data_util import ano_bissexto

ano = input("Digite o ano que voce gostaria de verificar:")
ehAnoBissexto = ano_bissexto.eh_ano_bissexto(int(ano))

if ehAnoBissexto == True:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto. Tente outro")

# verificando a idade
from data_util import calculo_idade

data_nascimento = input("Digite sua data de nascimento (exemplo: 08/02/2001):")
idade = calculo_idade.calcular_idade(data_nascimento)
print(f"Sua idade é {idade}")

# formatando a data
from data_util import formatar_data

data = input("Digite data desejada (exemplo: 27/11/1997):")
formato_data = formatar_data.formatar_data(data)
print(f"novo formato de data {formato_data}")


