from conversao import metro_para_pes, celsius_para_Fahrenheit, quilometro_para_milha

def menu():
    print("Escolha a conversão que deseja realizar: ")
    print("1. Metros para Pés")
    print("2. Quilometros para Milhas")
    print("3. Celsius para Fahrenheit")
    print("0. Sair")


def main():
    while True:
        menu()
        opcao = input("Digite um número: ")

        if opcao == '1':
            metros = float(input("Digite a quantidade de metros: "))
            pes = metro_para_pes.metro_pes(metros)
            print(metros, "metros é igual a", pes, "pés.")
        elif opcao == '2':
            quilometros = float(input("Digite a quantidade de quilômetros: "))
            milhas = quilometro_para_milha.quilometro_milha(quilometros)
            print(quilometros, "Quilômetros é igual a", milhas, "Milhas.")
        elif opcao == '3':
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_para_Fahrenheit.c_f(celsius)
            print(celsius, "Graus Celsius é igual a", fahrenheit, "Graus Fahrenheit.")
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção invalida.")
main()
