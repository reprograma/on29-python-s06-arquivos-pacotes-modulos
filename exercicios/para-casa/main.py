from data_util import calculo_idade
from data_util.ano_bissexto import eh_ano_bissexto
from datetime import datetime
from datetime import date
from data_util.formatar_data import format_data


# Calcular a idade

data_nascimento = input('Digite a sua data de nascimento no seguinte formato dd/mm/aaaa: ')
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
print(calculo_idade.calc_idade(data_nascimento))


# Verifique se o ano atual é bissexto ou não usando a função do módulo `ano_bissexto.py`.
ano_atual = date.today().year
ano = eh_ano_bissexto(ano_atual)
print(eh_ano_bissexto(ano_atual))

# Solicite ao usuário que insira uma data no formato "dd/mm/aaaa" e use a função do módulo formatar_data.py para exibir a data no formato "aaaa-mm-dd"
nova_data = input('Digite uma data no formato dd/mm/aaa: ')
data = format_data(nova_data)
print(data)
