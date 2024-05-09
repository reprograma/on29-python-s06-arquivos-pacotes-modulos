from conversao import celsius_fahrenheit, km_milhas, metros_pes


def menu():
    print("Escolha a conversão que deseja utilizar: ")
    print("1 - Metros para Pés")
    print("2 - Quilometros para Milhas")
    print("3 - Celsius para Fahrenheit")
    print("0 - Sair")


def main():
    while True:
        menu()
        opt = int(input("Digite um número: "))

        if opt == 1:
            metros = float(input("Digite a quantidade de metros: "))
            pes = metros_pes.metro_pes(metros)
            print(metros, "metro é igual a ", pes, "pés.")
        elif opt == 2:
            quilometros = float(input("Digite a quantidade de quilometros: "))
            milhas = km_milhas.km_milhas(quilometros)
            print(quilometros, "quilometros é igual a ", milhas, "milhas.")
        elif opt == 3:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_fahrenheit.c_f(celsius)
            print(celsius, "º Celsius é igual a ", fahrenheit, "º fahrenheit.")
        elif opt == 0:
            print("Saindo do programa.")
            break
        else:
            print("Digite uma opção válida.")


main()
