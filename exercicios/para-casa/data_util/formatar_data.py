from datetime import datetime

def formatar_data(data):

    data_validar = datetime.strptime(data, "%d/%m/%Y")

    data_formatada = datetime.strftime("%Y-%m-%d")