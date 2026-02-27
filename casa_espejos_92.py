'''
casa de los espejos: 
1. debe tener mas de 10 años
no debe tener miedo a la obscuridad
utilizar not
'''

import os
os.system("cls")

edad = int(input("¿Cuál es tu edad? "))
miedo = input("¿tienes miedo a la obscuridad (si/no)?  ").lower().strip() =="si"


if not  miedo  and edad >=10:
    print(f"puedes entrar a la casa de los espejos porque tienes {edad} años y tu miedo a la obscuridad es {miedo}")    

else:
    print("no puedes entrar a la casa por que no cumples los requsitos")


#CON EL OPERDOR TERNARIO: que es una forma compacta de agregar una codncion.

edad3 = int(input("ingresa tu edad"))

#se lee, si la edad3 es >= a 18 regresa si, de lo contrario no 
es_aduto ="si" if edad3 >= 18 else "no"
print(f"¿es un adulto? {es_aduto}")
