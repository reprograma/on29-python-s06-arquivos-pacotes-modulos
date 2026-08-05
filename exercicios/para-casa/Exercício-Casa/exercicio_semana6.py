from data_util import calculo_idade
from data_util import ano_bissexto
from data_util import formatar_data


def menu():
    while True:

        print("------ MENU -----")
        print("Calcular idade - 1")
        print("Conferir ano bissexto - 2")
        print("Formatar data - 3")
        print("Finalizar programa - 0")

        selection = int(input("Digite a opção desejada: "))

        if selection == 1:
            calculo_idade.calcular_idade()
        elif selection == 2:
            ano_bissexto.eh_ano_bissexto()
        elif selection == 3:
            formatar_data.formatar_data()
        elif selection == 0:
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida.")
        
        continue

menu()