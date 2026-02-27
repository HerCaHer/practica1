'''Crear un programa que genera ID a partir de los valores:
Nombre : solo usar las 2 primeras letras y convertirlas a mayusculas
apellido: las dos primeras letras y convertirlas a mayusculas
año de nacimiento: los dos ultimos digitos
generar 4 digitos aleatorios con la funcion randint '''


print("***Generador de ID***")



import random
from random import randint


nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))  
numero_aleatorio =randint(1111,9999)
# Generar ID
print(f"Hola {nombre} {apellido},")

id_usuario =nombre.strip().upper() [0:2] +apellido.upper()[0:2]+str(año_nacimiento)[2:4]+str(numero_aleatorio)
print(f"\t Tu número de identifacion ID generado por el sistema es:\n\t {id_usuario} \n\tFelicitaciones!!!\n")
