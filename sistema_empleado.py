import os
os.system("cls")

print(" ***Sistema de empleados*** \n")
noombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
salario = float(input("Ingrese el salario del empleado "))
es_jefe = input ("¿El empleado es jefe? (si/no): ").lower() == "si"

print(f"Nombre del empleado: {noombre}")
print(f"Edad del empleado: {edad}")
print(f"Salario del empleado: {salario:.2f}")
print(f"¿Es jefe?: {es_jefe}   ")
    