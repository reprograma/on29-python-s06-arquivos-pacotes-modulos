from datetime import date
from datetime import datetime


data_atual = date.today()
    #print(data_atual.year)

data_inserida = input("Digite a data que deseja no formato (ano / mẽs / dia): ")
data = datetime.strptime(data_inserida, "%Y/%m/%d")


print(data)