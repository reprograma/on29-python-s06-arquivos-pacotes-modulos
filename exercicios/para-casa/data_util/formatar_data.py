def formatar_data():

    data_atual = date.today()

    data_nascimento = input("digite sua data de nascimento nesse formato: dd/mm/aaaa")
    data = datetime.strptime(data_nascimento,"%d/%m/%Y")
    print(data)