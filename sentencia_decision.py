#SENTENCIA IF

import os
os.system("cls")

edad =10
if edad >=18:
    print(f"Eres mayor de edad con {edad} años")
else:
    print(f"Eres menor de edad con {edad} años")


#con dato de entrada de la edad del usuario

edad2 = int(input("Ingrese su edad: "))
if edad2 >=18:  
    print(f"Eres mayor de edad con {edad2} años")
else:       
    print(f"Eres menor de edad con {edad2} años")


#uso de elif
edad3 = int(input("Ingrese su edad: "))
if edad3 >= 18:
    print(f"Eres adulto con {edad3} años")
elif  13 <= edad3  < 18:
    print(f"Eres adolescente con {edad3} años")
else:
    print(f"Eres menor de edad con {edad3} años")