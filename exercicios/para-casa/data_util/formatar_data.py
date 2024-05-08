# `formatar_data.py`: Contém uma função formatar_data(data) que recebe uma data no formato "dd/mm/aaaa" e a formata como "aaaa-mm-dd".

from datetime import datetime

def formatar_data(data):
    data = datetime.strptime(data, "%d/%m/%Y")

    return data.strftime("%Y-%m-%d")
    