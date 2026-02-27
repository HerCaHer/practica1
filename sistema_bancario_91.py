'''
preguntar al usuario si desea continuar dentro del sistema
ni No desea salir del sistema imprimir ...continuamos dentro del sistema
de lo contrario, imprimir ...saliendo del sistema
 utitizar  not inversor para evaluar la respuesta del usuario
'''

import os
os.system("cls")

respuesta = input("¿Desea continuar dentro del sistema? (si/no): ").lower().strip()
if not respuesta == "no":#evaluar si la respuesta es diferente a "no"
    print("Continuamos dentro del sistema.")
else:
    print("Saliendo del sistema.")  