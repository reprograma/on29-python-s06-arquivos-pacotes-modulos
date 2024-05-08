from datetime import datetime

def formatar_data(data):
    data_extraida = datetime.strptime(data, "%d/%m/%Y")
    data_novo_formato = data_extraida.date()
         
    return data_novo_formato