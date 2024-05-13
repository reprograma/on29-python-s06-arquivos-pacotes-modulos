#`formatar_data.py`: Contém uma função formatar_data(data) que recebe uma data no formato "dd/mm/aaaa" e a formata como "aaaa-mm-dd".

def formatar_data(date_str):
    dia, mes, ano = date_str.split('/')
    nova_data = f'{ano}-{mes}-{dia}'
    return nova_data

data = input('Digite a data no formato dd/mm/yyyy: ')

formatado = formatar_data(data)

print(formatado)
