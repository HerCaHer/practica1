'''Nombre empresa: Global mentoring
Extension del dominio: .com.mx
Dominio de email normalizado:@globalmentoring.com.mx

Email final genrado: herlinda.castillo.hernandez@globalmentorin.com.mx
'''


def generar_email(nombre_usuario, nombre_empresa, extension):
    """
    Genera un email a partir del nombre del usuario y la empresa.

    Devuelve un diccionario con:
    - nombre_empresa
    - extension
    - dominio_normalizado
    - email_final
    """

    # Normalizar nombre del usuario
    usuario_normalizado = nombre_usuario.strip().replace(" ", ".").lower()
    
    # Normalizar nombre de la empresa
    empresa_normalizada = nombre_empresa.strip().replace(" ", "").lower()
    
    # Crear dominio
    dominio = "@" + empresa_normalizada + extension
    
    # Crear email final
    email = usuario_normalizado + dominio
    
    # Devolver todos los datos en un diccionario
    return {
        "nombre_empresa": nombre_empresa,
        "extension": extension,
        "dominio_normalizado": dominio,
        "email_final": email
    }

# Llamamos a la función y guardamos el resultado
resultado = generar_email(
    "Herlinda Castillo Hernandez",
    "Global mentoring",
    ".com.mx"
)

# Ahora podemos imprimir todo de forma ordenada
print(f"Nombre empresa: {resultado['nombre_empresa']}")
print(f"Extension del dominio: {resultado['extension']}")
print(f"Dominio de email normalizado: {resultado['dominio_normalizado']}\n")
print(f"Email final generado: {resultado['email_final']}")