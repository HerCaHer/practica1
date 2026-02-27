'''
calcular el área y perímetro de un rectángulo


'''

import os
os.system("cls") #limpiar pantalla en windows

print(" *** Cálculo de área y perímetro de un rectángulo *** \n")
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: ")) 
area = base * altura
perimetro = 2 * (base + altura)
print(f"El área del rectángulo es: {area:.2f}")
print(f"El perímetro del rectángulo es: {perimetro:.2f}")