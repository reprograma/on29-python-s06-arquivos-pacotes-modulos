
def formatando_data(data):
    dia, mes, ano = data.split('/')
    data_invertida = f"{ano}-{mes}-{dia}"
    print(f"A data formatada é: {data_invertida}")

data_input = input("Digite uma data no formato 'dd/mm/aaaa': ")

formatando_data(data_input)
