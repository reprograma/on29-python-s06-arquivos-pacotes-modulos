


from datetime import datetime
def calculo_idade ():
    from datetime import date
    from datetime import datetime
    input_data_nascimento = input("Insira sua data de nascimento: ")
    data_nascimento = datetime.strptime(input_data_nascimento, "%d/%m/%Y")
    data_atual = datetime.today()  
    data_formatada = datetime.strftime(data_atual, "%d/%m/%Y")
    data_final = datetime.strptime(data_formatada, "%d/%m/%Y")   
    idade = data_final.year - data_nascimento.year
    print(f"A idade do usuário é: {idade}") 

calculo_idade()