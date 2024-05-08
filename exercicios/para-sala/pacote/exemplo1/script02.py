from conversao import metros, celsius, quilometros

def menu():
    print('---- MENU ----')
    print('1 - Metros para Pés')
    print('2 - Quilômetros para Milhas')
    print('3 - Celsius para Fahrenheit')
    print('0 - Sair')

    
def main():
    while True:
        print('')
        medida = int(input('Qual é o tipo de medida que você quer converter? '))
    
        if medida == 1:
            metro = float(input('Digite a medida em metros: '))
            print(metro)
            pes = metros.metro_pes(metro)
            print(f'O valor é: {pes} pés.')

        elif medida == 2:
            km = float(input('Digite a medida em quilômetros: '))
            milha = quilometros.km_milhas(km)
            print(f'O valor é: {milha} milhas.')

        elif medida == 3:
            graus = float(input('Digite a temperatura em Celsius: '))
            fahr = celsius.celsius_fahreinheit(graus)
            print(f'O valor é: {fahr} graus Fahrenheit.')

        elif medida == 0:
            print('Obrigada por usar nosso programa.')
            break

        else:
            print('Não é uma opção válida, tente novamente.')

menu()
main()