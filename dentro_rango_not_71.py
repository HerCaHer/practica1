#revisar si una valiable se encuentra dentro de un rango de 1 y 10


import os
os.system("cls") #limpiar pantalla en windows

numero = int(input("ingresa un número entre 1 y 10: "))
rango = 1<= numero <=10 # se evalúa si el número ingresado se encuentra dentro del rango de 1 a 10, el resultado es un valor booleano (True o False)
print(f"El número {numero} se encuentra dentro del rango de 1 a 10: {rango}")


numero2 = int(input("ingresa un número entre 1 y 10: "))
rango2 = not (1<= numero2 <=10) # se evalúa si el número ingresado NO se encuentra dentro del rango de 1 a 10, el resultado es un valor booleano (True o False)
print(f"El número {numero2} NO se encuentra dentro del rango de 1 a 10: {rango2}")

