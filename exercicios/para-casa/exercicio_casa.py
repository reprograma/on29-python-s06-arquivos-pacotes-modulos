

def menu():
    print("Escolha a conversão que deseja utilizar: ")
    print("1 - Calcular idade")
    print("2 - Verificar ano bissexto")
    print("3 - Formatar data")
    print("0 - Sair")


def main():

    while True:
        menu()
        opt = int(input("Digite um número: "))

        if opt == 1:
            from data_util.calculo_idade import calculo_idade
            data_nascimento_str = input("Digite sua data de nascimento: ")
            idade = calculo_idade(data_nascimento_str)
            print(idade, "anos.")
        elif opt == 2:
            from data_util.ano_bissexto import verificar_ano_bissexto
            ano = int(input("Digite o ano que deseja verificar: "))
            resultado = verificar_ano_bissexto(ano)
            print(resultado)
        elif opt == 3:
            from data_util.formatar_data import formatar_data
            data_str = input("Digite a data desejada: ")
            nova_data = formatar_data(data_str)
            print("Data formatada: ", nova_data)
        elif opt == 0:
            print("Saindo do programa.")
            break
        else:
            print("Digite uma opção válida.")


main()
