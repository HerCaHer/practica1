print("Sistema de descuento VIP \n")

num_articulos_comprados = int(input("Ingrese el número de artículos que has comprado : "))
tiene_membresia = input(f"¿Tienes membresía VIP? (si/no): ")
max_productos = 10

#codigo ternario cuando se utiliza varias funciones apuntando a una misma variable
candidato_descuento = (num_articulos_comprados >= max_productos and tiene_membresia.strip().lower() == 'si')
print(f"¿Eres elegible para el descuento VIP? {candidato_descuento}")

