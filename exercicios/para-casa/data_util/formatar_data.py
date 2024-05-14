'''
Contém uma função formatar_data(data) que recebe uma data no formato "dd/mm/aaaa" e a formata como "aaaa-mm-dd"
'''
from datetime import datetime

def format_data(data):
    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    data_formatada_dois = data_formatada.date()
    return data_formatada_dois

