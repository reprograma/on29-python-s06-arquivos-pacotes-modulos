from datetime import date
from datetime import datetime

data_atual = date.today()

data_nascimento = input("Digite a data nascimento. Ex:(xx/xx/xxxx)")
data = datetime.strftime (data_nascimento, "%d/%m/%Y")
if data_atual.month < data.month:
    idade = data_atual.year - data.year -1
    print (idade)

elif data_atual.month == data.month:
    if data_atual.day < data.day:
        idade = data_atual.year - data.year -1 
        print(idade)
    else:
        idade = data_atual.year - data.year
        print (idade)
    