'''
meses de 1 -12 

1,2,12 --> invierno
3,4,5 --> primavera
6,7,8 --> verano
9,10,11 --> otoño
Cualquier otro valor == estación desconocida 
'''
import os
os.system("cls" )


print ("**** Estación del año*****")

mes =int(input("Proporciona el número del mes (1 12):   "))

if mes == 1 or mes == 2 or mes ==12:
    estacion ="invierno"
    print(f"La estación del año es {estacion} en el mes {mes}")
    
elif  mes == 3 or mes == 4 or mes ==4:
    estacion = "primavera"
    print(f"La estación del año es  {estacion} en el mes {mes}")
    
elif mes == 6 or mes == 7 or mes ==8:
    estacion = "verano"
    print(f"La estación del año es  {estacion} en el mes {mes}")

elif mes == 9 or mes == 10 or mes ==11:
    estacion = "otoño"
    print(f"La estación del año es  {estacion} en el mes {mes}")

else:
    print("ESTACIÓN DESCONOCIDA")

    

    print ()