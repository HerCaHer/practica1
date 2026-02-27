import os
os.system("cls")



print("Aplicación de Salud Fitneess \n \n")
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = .04
nombre =input("¿Cuál es tu nombre? ")
pasos_caminados = int(input("¿cuantos pasos has dado?  "))
meta= pasos_caminados >= META_PASOS_DIARIOS
meta_alcanzada = "SI  :)" if meta else "No :( )"

calorias= pasos_caminados*CALORIAS_POR_PASO
print(f"Nombre:  {nombre}")
print(f"Camino:  {pasos_caminados} " )
print (f"Calorias quemandas:  {calorias}  kcalorias")
print(f"¿Alcanzaste la meta? {meta_alcanzada}")