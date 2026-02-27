''' crear un prograama para generar un email a partir de los siguentes datos:
Nombre usuario:  Herlinda Castillo Hernández
Nombre usuario normalizado: herlinda.castillo.hernandez


Nombre empresa: Global mentoring
Extension del dominio: .com.mx
Dominio de email normalizado:@globalmentoring.com.mx

Email final genrado: herlinda.castillo.hernandez@globalmentorin.com.mx
'''


#imprime el titulo
print("***Generador de Email***")

#crear la variable para nombre
nombre_usuario = "Herlinda Castillo Hernandez"
print(f"Nombre usuario: {nombre_usuario}")

#quitar los espacios en blanco al inicio y final de la cadena .strip(), reemplazar los espacios por puntos .replace() 
# y convertir a minusculas con el metodo .lower()

nombre_usuario_normalizado = nombre_usuario.strip() .replace(" ", ".") .lower()
print(f"Nombre usuario normalizado: {nombre_usuario_normalizado}")


#crear la variable  y lo imprime 
nombre_empresa = "Global mentoring"
print(f"Nombre de la empresa: {nombre_empresa}")
ext_dominio = ".com.mx"
print(f"Extension del dominio:  {ext_dominio}"      )

#se hace una concatenación de la extension del dominio con el nombre de la empresa,
#  se convierte a minusculas y se reemplazan los espacios por nada
dominio_normalizado = "@" + nombre_empresa.lower() .replace(" ", "")
print(f"Dominio de email normalizado: {dominio_normalizado}")

#se hace una concatenación del nombre de usuario normalizado con el dominio normalizado para generar el email final
email_final=nombre_usuario_normalizado + dominio_normalizado
print(f"Email final generado: {email_final}")

print("\n  ***Fin del programa*** \n\n")

