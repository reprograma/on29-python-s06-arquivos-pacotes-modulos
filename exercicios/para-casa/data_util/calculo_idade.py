from datetime import datetime


def calc_idade(data_nascimento):
    data_atual = datetime.now()
    return data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))
    

