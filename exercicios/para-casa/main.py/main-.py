from data_util.calculo_idade import calcular_idade
from data_util.ano_bissexto import eh_ano_bissexto
from data_util.formatar_data import formatar_data
from datetime import datetime

def main():
    # Solicitar data de nascimento e calcular idade
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    idade = calcular_idade(data_nascimento)
    print(f"Sua idade é: {idade} anos")

    # Verificar se o ano atual é bissexto
    ano_atual = datetime.today().year
    if eh_ano_bissexto(ano_atual):
        print(f"O ano {ano_atual} é bissexto.")
    else:
        print(f"O ano {ano_atual} não é bissexto.")

    # Solicitar uma data e formatá-la
    data = input("Digite uma data (dd/mm/aaaa): ")
    data_formatada = formatar_data(data)
    print(f"A data formatada é: {data_formatada}")

if __name__ == "__main__":
    main()
