import manipulacao_string

def main():
    string = input("Digite uma string: ")

    print(f"String invertida: {manipulacao_string.inverter_string(string)}")
    print(f"Número de palavras na string: {manipulacao_string.contar_palavras(string)}")
    
    if manipulacao_string.verificar_palindromo(string):
        print(f"A string '{string}' é um palíndromo.")
    else:
        print(f"A string '{string}' não é um palíndromo.")

main()