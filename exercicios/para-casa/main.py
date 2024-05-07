from data_util import calculo_idade, ano_bissexto, formatar_data

def menu():
    while True: 
        print("+-------------------------------------+")
        print("+        Manipulação de datas         +")
        print("+-------------------------------------+")
        print("+ 1 - Calcular idade                  +")
        print("+ 2 - Verificar se é ano bissexto     +")
        print("+ 3 - Formatar data                   +")
        print("+ 0 - Encerrar                        +")
        print("+-------------------------------------+")

        opt = input("+ Insira o número correspondente a opção desejada: ")

        print("+-------------------------------------+")

        if opt == "1": 
            data_nascimento = input("+ Insira sua data de nascimento (dd/mm/aaaa): ")
            print(calculo_idade.calcular_idade(data_nascimento))
        
        elif opt == "2":
            ano = int(input("+ Insira o ano que deseja saber se é bissexto: "))
            if ano_bissexto.eh_ano_bissexto(ano):
                print(f"O ano {ano} é bissexto.")
            else:
                print(f"O ano {ano} não é bissexto.")
        
        elif opt == "3":
            data = input("+ Insira a data que deseja formatar (dd/mm/aaaa): ")
            print(formatar_data.formatar_data(data))
        
        elif opt == "0":
            break

        elif opt not in ["1", "2", "3", "0"]:
            print("Opção inválida, tente novamente.")

menu()