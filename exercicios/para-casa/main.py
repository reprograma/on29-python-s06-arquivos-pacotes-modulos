#Programa principal para testar a importação de módulos que estão na pasta "data_util"
#Tudo que está na pasta data_util é o pacote
#o comando from serve para dizer de qual local vc está importando o modulo e o comando import importa a fução requerida

from data_util.calculo_idade import calcular_idade
from data_util.ano_bissexto import eh_ano_bissexto
from data_util.formatar_data import formatar_data

def main():
    while True:
        #Parte I - calcular idade importando do módulo "calculo_idade.py" a função "calcular_idade()" com o argumento "data_nascimento"
        data_nascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")
        idade = calcular_idade(data_nascimento)

        #Parte II - verificar se o ano é bissexto ou não
        ano = int(input("Digite o ano no formato AAAA: "))
        if eh_ano_bissexto(ano):
            print(f"Sim, {ano} é um ano bissexto.")
        else:
            print(f"{ano} NÃO é um ano bissexto.")
        #Parte III - formata a data informada pelo usuário no formato dd/mm/aaaa
        data = input("Insira uma data no formato (dd/mm/aaaa): ")
        data_formatada = formatar_data(data)
        print("A data formatada para aaaa-mm-dd é:", data_formatada)
        #Continuar
        continuar = input("Deseja continuar? Digite a tecla 1 para SIM:")
        if continuar != "1":
            return data_nascimento

main()

