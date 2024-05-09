from datetime import datetime
from datetime import timedelta
from datetime import date

def eh_ano_bissexto():
    data_atual = date.today()
    resposta = 0

    if((data_atual.year % 4 == 0) and (data_atual.year % 100 != 0)):
        resposta = "True" 
    elif((data_atual.year % 4 == 0) and (data_atual.year % 100 == 0) and (data_atual.year % 400 == 0)):
        resposta = "True" 
    else:
        resposta = "False" 

    print(data_atual.year, "é bissexto?", resposta)



