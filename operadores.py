#OPERADORES ARITMÉTICOS
import os
os.system("cls") #limpiar pantalla en windows


a = 10
b = 5   
suma = a + b
resta = a - b
multiplicacion = a * b       
division = a / b
division_entera = a // b
modulo = a % b
exponete =a ** b

print   ("Suma:", suma)
print   ("Resta:", resta)       
print   ("Multiplicación:", multiplicacion)
print   (f"División: {division:.2f}")
print   ("División entera:", division_entera)
print   ("Módulo:", modulo)
print   ("Exponente:", exponete)    

#OPERADORES DE ASIGNACIÓN

print("\n Valor de asignación:")
numero = 5
print("el valor es:", numero)


#ASIGNACION MULTIPLE
x, y, z = "hola", 2, 3.14

print(f"Valor de x: {x}, de y: {y}, de z: {z} ")

#VARIOS VALORES RECIBIDOS DE UN INPUT Y ASIGNADOS A VARIAS VARIABLES
nombre, apellido, edad = input("Ingrese su nombre y edad separados por : ").split(",")
print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")



#OPERADORES DE ASIGNACIÓN COMBINADOS
a,b = 10, 5
a += b
print(f"Valor de a después de operar a += b: {a}") #a se incrementa en el valor de b, es decir, a = a + b
a -= b
print(f"Valor de a después de operar  a -= b: {a}") #a se decrementa en el valor de b, es decir, a = a - b
a *= b
print(f"Valor de a después de  operar a *= b: {a}") #a se multiplica por el valor de b, es decir, a = a * b
a /= b
print(f"Valor de a después de operar a /= b: {a}") #a se divide por el valor de b, es decir, a = a / b


 
