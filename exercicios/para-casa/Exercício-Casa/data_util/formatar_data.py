from datetime import datetime
from datetime import timedelta
from datetime import date

def formatar_data():

    data_nascimento_input = input("Informe a sua data de aniversário. Utilize o seguinte formato: dd/mm/aaaa: ")
    data_nascimento = datetime.strptime(data_nascimento_input, "%d/%m/%Y")
    print(data_nascimento.strftime("%Y/%m/%d"))
