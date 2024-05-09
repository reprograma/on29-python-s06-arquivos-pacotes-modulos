

def formatar_data():
    from datetime import datetime
    ano = input("Digite um ano no formato dd/mm/aaaa: ")
    ano_formatado = datetime.strptime(ano, "%d/%m/%Y")
    ano_final = datetime.strftime(ano_formatado, "%Y/%m/%d")
    print(ano_final)

formatar_data()
