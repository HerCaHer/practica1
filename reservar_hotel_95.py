'''
Reservar Hotel:
datos solicitados: 
nombre cliente, dias de estancia, cuarto con vista al mar

tarifas:
con vista al mar= 190.50
sin  vista al mar = 150.50

calcular el costo de la estadia

'''
import os
os.system("cls")
print("***Sistema de Rserva de Hotel ***\n\n")

VISTA_MAR = 190.50
SIN_VISTA_MAR = 150.50

cliente =input("Nombre del cliente:  ").strip()
dias_estancia =int(input("Días de estancia: "))
tipo_habitacion = input("Habitación con vista al mar (si/no)")
"cambia a tipo boleano"
tip_habitacion =tipo_habitacion.strip().lower() =="si"

if tip_habitacion:
    costo_final = dias_estancia*VISTA_MAR
else:
    costo_final =dias_estancia*SIN_VISTA_MAR

print("-------------Detalls de la Reservación------------")
print(f"Ciente:  {cliente}" )
print(f"Días de estadia: {dias_estancia}")
print(f"Costo total: {costo_final}")
print(f"Habitación con vista al mar:  {tipo_habitacion}")
