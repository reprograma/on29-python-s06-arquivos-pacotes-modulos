from conversao import celsius_fahrenheit, km_milhas, metros_pes

print("Escolha a conversão que deseja realizar: ")
print("1: Celsius para Fahrenheit")
print("2: Km para milhas")
print("3: Metros para pés")

escolha = ""

while escolha != "1" and escolha != "2" and escolha != "3":
    escolha = input("Insira o número válido de acordo com sua escolha: ")

if escolha == "1":
    temp = int(input("Insira o valor da temperatura em Celsius: "))
    print(f"{celsius_fahrenheit.converter(temp)}K")
elif escolha == "2":
    dist = int(input("Insira o valor da distância em km: "))
    print(f"{km_milhas.converter(dist)} milhas")
elif escolha == "3":
    dist = int(input("Insira o valor da distância em km: "))
    print(f"{metros_pes.converter(dist)} pés.")