# Importando o módulo datetime da biblioteca datetime
from datetime import datetime

# Criação da função para formatar a data
def formatar_data(data):
    data_inserida = datetime.strptime(data, '%d/%m/%Y')

    data_formatada = data_inserida.strftime('%Y-%m-%d')
    
    return f"A sua data no novo formato é: {data_formatada}."