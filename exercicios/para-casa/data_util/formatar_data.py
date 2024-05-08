from datetime import datetime

def formatar_data(data):
    #data = input('Digite uma data aqui: ')
    data = datetime.strptime(data, "%d/%m/%Y")
    return data.date()

