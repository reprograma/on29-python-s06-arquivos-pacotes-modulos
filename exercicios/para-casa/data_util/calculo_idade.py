#Função para calcular idade do usuário
from datetime import datetime
def calculo_idade ():
    from datetime import date
    input_data_nascimento = input("Insira sua data de nascimento: ")
    data_nascimento = date.strptime(input_data_nascimento, "%d/%m/%Y")
    data_atual = date.today()  
    data_formatada = date.strptime(data_atual, "%d/%m/%Y")   
    idade = data_formatada - data_nascimento
    print(f"A idade do usuário é: {idade}") 

calculo_idade()