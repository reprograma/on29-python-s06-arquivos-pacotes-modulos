#Modo de fazer 1: importando o módulo
# import area_circulo

# raio = 5
# area = area_circulo.calcular_area(raio)
# print(f"A área do círculo de raio {raio} é {area}.")


#Modo de fazer 2: importação de funções/estruturas específicas
from area_circulo import calcular_area

raio = 5
area = calcular_area(raio)
print(f"A área do círculo de raio {raio} é {area}.")