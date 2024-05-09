# perguntar qual é o ano
# calcular quantos dias tem um ano
# Fala se é bissexto ou não
ano_atual = int(input("Digite o ano que deseja verificar se é bissexto: "))

def calculo_bissexto(ano):
    # descobrindo se é divisível por 4 para saber se é bissexto
    divisao_4 = ano % 4 == 0
    if divisao_4:
        divisao_100 = ano % 100 == 0
        if divisao_100:
                divisao_400 = ano % 400 == 0
                if divisao_400:
                    resultado_final = True
                else:
                    resultado_final = False
        else:
                resultado_final = True  # Ano bissexto
    else:
            resultado_final = False  # Não é bissexto
    return resultado_final

if calculo_bissexto(ano_atual):
    print(f"{ano_atual} é um ano bissexto.")
    dias = 366  # Ano bissexto
else:
    print(f"{ano_atual} não é um ano bissexto.")
    dias = 365  # Ano não bissexto

print(f"O ano de {ano_atual} tem {dias} dias.")

