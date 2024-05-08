from data_util import formatar_data, ano_bissexto, calculo_idade

def menu ():
    print('--- MENU ---')
    print('1 - Quantos anos você tem?')
    print('2 - Esse ano é bissexto?')
    print('3 - Descubra como é uma data no formato internacional.')
    print('0 - Sair do programa.')

def main():
    while True:
        print('')
        opcao = int(input('Digite a opção escolhida: '))
        if opcao == 1:
            idade = calculo_idade.calculo_idade()
            print(f'Você tem {idade} anos de idade.')
        elif opcao == 2:
            ano = 2024
            ano_bi = ano_bissexto.ano_bissexto(ano)
            print(ano_bi)
        elif opcao == 3:
            data_br = input('Digite uma data no formato dd/mm/aaaa: ')
            data_int = formatar_data.formatar_data(data_br)
            print(f'O formato internacional da data é {data_int}.')
        elif opcao == 0:
            print('Obrigada por usar nosso programa.')
            break
        else:
            print('Essa opção é invalida. Escolha uma nova opção.')

menu()
main()