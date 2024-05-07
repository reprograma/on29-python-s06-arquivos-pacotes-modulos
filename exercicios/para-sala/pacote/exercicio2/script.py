from conversao import metros_pes, km_milhas, fahrenheit_celsius

def menu():
    print("Escolha a conversão:")
    print("1. Metros para pés")
    print("2. Quilômetros para milhas")
    print("3. Celsius para Fahrenheit")

def main():
    menu()
    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        metros = float(input("Digite a quantidade em metros: "))
        print(f"Pés: {metros_pes.metros_para_pes(metros)}.")
    elif escolha == 2:
        quilometros = float(input("Digite a quantidade em quilômetros: "))
        print(f"Milhas: {km_milhas.quilometros_para_milhas(quilometros)}.")
    elif escolha == 3:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        print(f"Fahrenheit: {fahrenheit_celsius.celsius_para_fahrenheit(celsius)}.")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
