'''Crear un program para validad el usuario y contrasena porporcionado por el usuario,
-crear 2 constantes con los valores correctos y posteriormente comparar que el 
usuario y contraseña porporcionados por el usuario sean válidos. 

Debe solicitar el usuario  la contraseña al usuario y si son iguales que los valores correctos 
almacenados en las constantes debe imprimir True, de lo contario debe imprimir False.'''

import os
os.system("cls") #limpiar pantalla en windows

USUARIO = "admin"
CONTRASENA = "1234"
usuario = input("¿cuál es tu usuario? ")
contrasena = input("¿cuál es tu contraseña? ")
validacion_usuario = (usuario == USUARIO and contrasena == CONTRASENA) #se evalúa si el usuario y contraseña ingresados por el usuario son iguales a los valores correctos almacenados en las constantes, 
print(f"Datos correctos ?   {validacion_usuario}" )   
