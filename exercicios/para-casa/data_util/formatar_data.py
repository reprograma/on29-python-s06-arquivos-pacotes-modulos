

def formatar_data():
    import datetime
    ano = input("Digite um ano no formato dd/mm/aaaa: ")
    ano1 = datetime.strptime(ano, '%d/%m/%Y')
    ano_formatado = ano1.strftime('%Y/%m/%d')
    print(ano_formatado)

formatar_data()
