from manipulacao_string import contar_palavras, inverter_string, remover_espacos

print("Selecione a opção desejada")
print("contar palavras, digite 1")
print("inverter palavra, digite 2")

opt = input("digite a opção desejada")

if opt == "1":
    return contar_palavras
elif opt == "2":
    return inverter_string
else:
    return remover_espacos

