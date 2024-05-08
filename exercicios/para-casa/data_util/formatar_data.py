from datetime import datetime

def formatar_data(data):
    while True:
        try:
            entrada = datetime.strptime(data, "%d/%m/%Y")
            data_formatada = entrada.strftime("%Y-%m-%d")
            return data_formatada
        except ValueError:
            print("Formato Inválido. Tente novamente")
            data = input("\nInsira uma data no formato dd/mm/aaaa:")
            continue



