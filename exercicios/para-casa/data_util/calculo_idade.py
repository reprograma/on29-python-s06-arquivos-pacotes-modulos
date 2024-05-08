from datetime import datetime
from datetime import date

def calcular_idade(data_nascimento):
    while True:
        try:
            nasc = datetime.strptime(data_nascimento, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato Inválido. Tente novamente")
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
            continue
    
    hoje = date.today()
    idade_ano = hoje.year - nasc.year
    idade_mes = hoje.month - nasc.month
    idade_dia = hoje.day - nasc.day

    if idade_dia < 0:
        idade_mes = idade_mes - 1
        idade_dia = idade_dia + 30
    if idade_mes < 0:
        idade_ano = idade_ano - 1
        idade_mes = idade_mes + 12
    
    print(f"Sua idade é {idade_ano} anos, {idade_mes} meses e {idade_dia} dias.")


