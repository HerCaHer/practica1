print("***Sistema Generador de Email***")

nombre=input("Ingresa el nombre  ")
apellido=input("Ingresa el apellido  ")
empresa=input("Ingresa el nombre de la empresa  ")
extension=input("Ingresa la extension del dominio (ej: .com.mx)  ") 

nombre_normalizado =nombre.strip().lower().replace(" ", ".")
apellido_normalizado =apellido.strip().lower().replace(" ", ".")    
empresa_normalizada =empresa.strip().lower().replace(" ", "")
dominio = "@" + empresa_normalizada + extension.strip().lower()

print(f''' 
      El resultado es:
      {nombre_normalizado}{apellido_normalizado}{dominio}
      Felicidades!!!!
      
    ''')