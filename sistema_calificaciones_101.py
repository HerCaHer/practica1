
'''
Sistema de calificaciones:

if califiacion >=9 and  <=10  == A

califiacion >=8 and <=9  == B

if calificacion es >=7 and  <=8 == C

if califiacion >=6 and <=7 == D

if calificacion >=0 and <=6 == F

else:
Valor desconocido

'''

import os
os.system("cls")

print(" *****SISTEMA DE CALIFICACIONES*****")
 
 
calificacion_final=None
 
calificacion = float(input("Digita la calificación obtenida:  "))
if calificacion >=9 and calificacion <=10:
    calificacion_final ="A"
    print(f"La calificación con respecto a {calificacion} es '{calificacion_final}' ")
    
elif 8<= calificacion < 9:
    calificacion_final = "B"
    print(f"La calificación con respecto a {calificacion} es '{calificacion_final}' ")
elif calificacion >=7 and  calificacion<=8:     
    calificacion_final ="C"
    print(f"La calificación con respecto a {calificacion} es '{calificacion_final}' ")

elif calificacion >=6 and  calificacion<=7:
    calificacion_final ="D"
    print(f"La calificación con respecto a {calificacion} es '{calificacion_final}' ")

elif calificacion >0 and calificacion <=6:
    calificacion_final ="F"
    print(f"La calificación con respecto a {calificacion} es '{calificacion_final}' ")



else:
    calificacion_final="calificación incorrecta"
    print("valor desconocido")
  

