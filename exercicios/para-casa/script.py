from data_util import calculo_idade, ano_bissexto, formatar_data
from datetime import datetime

while True:
    print("----- OPERAÇÕES COM DATAS -----")
    print("Qual operação você deseja realizar?")
    print("Para calcular sua idade, digite 1.")
    print("Para calcular se o ano atual é bissexto, digite 2.")
    print("Para formatar a data, digite 3.")
    print("Para sair, digite 0.")
    opt = input("Insira o código da operação que deseja realizar: ")

    if opt == "0":
        break
    elif opt == "1":
        dia = int(input("Insira o dia em que você nasceu: "))
        mes = int(input("Insira o mês em que você nasceu: "))
        ano = int(input("Insira o ano em que você nasceu: "))

        data_nascimento = datetime(ano, mes, dia)

        calculo_idade.calcular_idade(data_nascimento)
    elif opt == "2":
        ano = int(input("Insira o ano que deseja saber se é bissexto: "))

        print(ano_bissexto.eh_ano_bissexto(ano))
    elif opt == "3":
        data = input("Insira uma data no formato dd/mm/aaaa: ")
        formatar_data.formatar_data(data)
    else:
        print("Insira uma opção válida!")