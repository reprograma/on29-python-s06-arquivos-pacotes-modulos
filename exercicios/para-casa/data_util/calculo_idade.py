from datetime import datetime

def calcular_idade(data_nascimento):
    nascimento_usuario = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()

    idade_usuario = hoje - nascimento_usuario
    idade_usuario_em_anos = int(idade_usuario.days / 365.25)
    
    return idade_usuario_em_anos
    