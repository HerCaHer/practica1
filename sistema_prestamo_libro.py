#aplicando el operador logico OR para determinar si un usuario puede obtener un préstamo de libro en una biblioteca.

print("Sistema de préstamo de libros \n")
nombre_usuario = input("Ingrese su nombre: ")
tiene_credencial = input(f"¿Tienes credencial de estudiante? (si/no): ")
distancia_biblioteca = float(input("Ingrese la distancia a la biblioteca en kilómetros: "))
distancia_maxima = 3.0
se_puede_prestar = (tiene_credencial.strip().lower() == 'si' or distancia_biblioteca <= distancia_maxima)
print(f'''Hola {nombre_usuario},
      De acuerdo a la información proporcionada es  {se_puede_prestar} el prestamo del libro''')

