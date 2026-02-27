'''
Soliciar al usuario un valor entre 0 y 5 e indicar si el valor se encuentra dentro del rango.
definir dos constantes VALOR_MINIMO =0 VALOR_MAXIMO =5, 
una vez comparado imprimir valor dentro de rango: TRUE o FALSE
'''

import os
os.system("cls") #limpiar pantalla en windows

print(" *** Validación de valor dentro de un rango \n ***")

VALOR_MINIMO = 0
VALOR_MAXIMO = 5
valor = float(input("Ingrese un valor entre 0 y 5: "))
rango_valor =  VALOR_MINIMO <= valor <= VALOR_MAXIMO #evaluar  valor 

print(f"El valor {valor} se encuentra dentro del rango de {VALOR_MINIMO} y {VALOR_MAXIMO}: {rango_valor}")