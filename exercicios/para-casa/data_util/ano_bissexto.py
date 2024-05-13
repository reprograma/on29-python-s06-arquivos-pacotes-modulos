#`ano_bissexto.py`: Contém uma função eh_ano_bissexto(ano) que verifica se um ano é bissexto e retorna True ou False.

ano = int(input("Digite o ano atual: "))

def verificar_ano_bissexto(ano):
    if (ano % 4) == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print(f'O ano atual inserido, {ano}, é bissexto, portanto têm 366 dias.')
    else:
        print(f'O ano atual inserido, {ano}, não é ano bissexto, portanto têm 365 dias.')


verificar_ano_bissexto(ano)
