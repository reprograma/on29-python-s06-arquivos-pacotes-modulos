# formatar_data.py
def formatar_data(data):
    dia, mes, ano = data.split('/')
    return f"{ano}-{mes}-{dia}"

