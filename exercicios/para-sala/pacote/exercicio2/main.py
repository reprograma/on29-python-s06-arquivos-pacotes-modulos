from conversao import cel_fahr, kms_milhas, metros_pes

 
def menu():
    while True:
        print("\n======== VOCÊ ESTÁ NO SISTEMA DE CONVERSÃO DE MEDIDAS ========")

        print("\n1 - Para converter uma temperatura de Celsius para Fahrenheit.")
        print("2 - Para converter uma medida de quilômetros para milhas.")
        print("3 - Para converter uma medida de metros para pés.")
        print("0 - Para encerrar a consulta.")

        opcao = input("\nDigite a opção desejada: ")
        
        if opcao == "1":
            temp_celsius = float(input("Digite a temperatura em °C: "))    
            temp_fahrenheit = cel_fahr.celsius_fahrenheit(temp_celsius)
            print (f"A temperatura de {temp_celsius}°C corresponde a {temp_fahrenheit}°F.\n")
            
        elif opcao == "2":
            medida_km = float(input("Digite a medida em Km: ")) 
            medida_milhas = kms_milhas.kms_milhas(medida_km)
            print (f"A medida de {medida_km}km corresponde a {medida_milhas}mi.\n")
            
        elif opcao == "3":
            medida_metros = float(input("Digite a medida em metros: ")) 
            medida_pes = metros_pes.metros_pes(medida_metros)
            print (f"A medida de {medida_metros}m corresponde a {medida_pes}pés.\n")
                        
        elif opcao == "0":
            print("\nFim da consulta.\n")
            break
        
        else:
            print("\nInsira uma opção válida.\n")
            continue
        
menu()

