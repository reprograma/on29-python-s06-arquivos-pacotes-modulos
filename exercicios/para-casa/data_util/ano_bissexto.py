'''
`ano_bissexto.py`: Contém uma função eh_ano_bissexto(ano) que verifica se um ano é bissexto e retorna True ou False.

'''

def eh_ano_bissexto(ano):
    #Divisivel por 4 (resto da divisão por 4 é zero)
    divide_por_quatro = ano % 4 == 0

    #Divisivel por 100 (resto da divisão por 100 é zero)
    divide_por_cem = ano % 100 == 0

    if divide_por_quatro and not divide_por_cem:
        return True
    
    return False
    
    