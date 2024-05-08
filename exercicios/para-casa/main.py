from data_util import calculo_idade, ano_bissexto, formatar_data
from datetime import datetime

def menu():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    while True:
        print("______________________________________________")
        print("\nEscolha a opção desejada do menu a seguir:")
        print("______________________________________________")
        
        print("\n1 - Para calcular sua idade.")
        print("2 - Para saber se o ano atual é bissexto.")
        print("3 - Para transformar uma data no formato dd/mm/aaaa para o formato aaaa-mm-dd.")
        print("0 - Para sair do menu.")
        
        opcao = input("\nDigite aqui a opção desejada: ")
        
        if opcao == "1":
            data_nascimento = input("Insira sua data de nascimento (dd/mm/aaaa): ")
            idade = calculo_idade.calcular_idade(data_nascimento)
            print(f"\nVocê possui {idade} anos de idade.")

        elif opcao == "2":
            ano = datetime.now().year
            ano_eh_bissexto = ano_bissexto.eh_ano_bissexto(ano)
            if ano_eh_bissexto:
                print(f"\nO ano de {ano} é bissexto.")
            else: 
                print(f"\nO ano de {ano} não é bissexto.")
             
            
        elif opcao == "3":
            data = input("Insira a data no formato dd/mm/aaaa: ")
            data_novo_formato = formatar_data.formatar_data(data)
            print(f"\nData no formato aaaa-mm-dd: {data_novo_formato}")
        
        elif opcao == "0":
            print("\nMenu encerrado.\n")
            break
        
        else:
            print("\nInsira uma opção válida.\n")
            continue
        
menu()