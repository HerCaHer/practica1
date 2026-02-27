''' crear un prograama para generar un email a partir de los siguentes datos:
Nombre usuario:  Herlinda Castillo Hernández
Nombre usuario normalizado: herlinda.castillo.hernandez


Nombre empresa: Global mentoring
Extension del dominio: .com.mx
Dominio de email normalizado:@globalmentoring.com.mx

Email final genrado: herlinda.castillo.hernandez@globalmentorin.com.mx
'''


nombre = "Herlinda Castillo Hernandez"
def normalizar(nombre):
    return nombre.strip().replace(" ", ".").lower()
nombre_normalizado = normalizar(nombre)
print(f"Nombre usuario normalizado:  {nombre_normalizado}")

print("\n")

#crear una lista de nombres  para utlizar la función de normalización
lista_nombres = [
    "Herlinda Castillo Hernandez",
    "Juan Perez Lopez",
    "Maria Fernanda Ruiz"
]

#crear la funcion normalizar_nombre que recibe un nombre y devuelve el nombre normalizado 
# con los parametros de quitar los espacios en blanco al inicio y final de la cadena .strip(),
#  reemplazar los espacios por puntos .replace() 
# y convertir a minusculas con el metodo .lower()
def normalizar_nombre(nombre):

    # el return 
    return nombre.strip().replace(" ", ".").lower()

#el for lo que hace es iterar sobre cada nombre en la lista de nombres y llamar a la función normalizar_nombre "
 #para cada nombre, imprimiendo el resultado

for nombre in lista_nombres:
    print(f"Nombre normalizado: {normalizar_nombre(nombre)}")


# Lista original
nombres = [
    "Herlinda Castillo Hernandez",
    "Juan Perez Lopez",
    "Maria Fernanda Ruiz"
]




