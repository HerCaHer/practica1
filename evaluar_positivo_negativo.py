#evaluar si el numero es positoo, negativo o cero

import os
os.system("cls")

print(" *** Evaluar si un número es positivo, negativo o cero *** \n")
numero = float(input("Ingrese un número: "))
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print(f"El número {numero} es cero.")
