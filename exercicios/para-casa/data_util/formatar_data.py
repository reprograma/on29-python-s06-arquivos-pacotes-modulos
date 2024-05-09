'''Contém uma função formatar_data(data) que recebe uma data no formato "dd/mm/aaaa" e a formata como "aaaa-mm-dd
'''
from datetime import datetime


def formatar_data(data_str):
    data = datetime.strptime(data_str, "%d/%m/%Y")
    nova_data = data.strftime("%Y-%m-%d")
    return nova_data


data_str = input("Digite a data desejada: ")
nova_data = formatar_data(data_str)
print("Data formatada: ", nova_data)
