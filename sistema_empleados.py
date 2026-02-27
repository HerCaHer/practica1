#crea un programa para solicitar la informacion de un empleado,  con los datos:
#nombre empleado:
#dad del empleado: (convertir a entero)
#salario del empleado: (convertir a flotante)
#es jefe de departamento (si/no)  





print("***Sistema de Empleados***\n")
nombre_empleado = input("Ingresa el nombre del empleado: ")
edad_empleado = int(input("Ingresa la edad del empleado: "))    
salario_empleado = float(input("Ingresa el salario del empleado: "))
es_jefe_departamento = input("¿Es jefe de departamento? (si/no): ")

#covertir a tipo bool si es jefe de departamento es true si no es false
es_jefe_departamento = es_jefe_departamento.lower() == "si"
print()
print(f"Nombre del empleado: {nombre_empleado}")
print(f"Edad del empleado: {edad_empleado}")
print(f"Salario del empleado: ${salario_empleado:.2f}")
print(f"Es jefe de departamento: {es_jefe_departamento}")



