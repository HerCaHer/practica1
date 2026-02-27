mensaje ="programar en python"
print(mensaje.upper())


# 📥 Pedir datos al usuario
nombre_usuario = input("Ingresa el nombre del usuario: ")
nombre_empresa = input("Ingresa el nombre de la empresa: ")
extension = input("Ingresa la extensión del dominio (ej: .com.mx): ")


def generar_email(nombre_usuario, nombre_empresa, extension):
    """
    Genera un email a partir del nombre del usuario y la empresa.
    Devuelve un diccionario con todos los datos.
    """
    usuario_normalizado = nombre_usuario.strip().replace(" ", ".").lower()
    empresa_normalizada = nombre_empresa.strip().replace(" ", "").lower()
    dominio = "@" + empresa_normalizada + extension
    email = usuario_normalizado + dominio
    
    return {
        "nombre_empresa": nombre_empresa,
        "extension": extension,
        "dominio_normalizado": dominio,
        "email_final": email
    }



# Generar email
resultado = generar_email(nombre_usuario, nombre_empresa, extension)

# Mostrar resultados
print("\n--- Resultado ---")
print(f"Nombre empresa: {resultado['nombre_empresa']}")
print(f"Extension del dominio: {resultado['extension']}")
print(f"Dominio de email normalizado: {resultado['dominio_normalizado']}\n")
print(f"Email final generado: {resultado['email_final']}")

