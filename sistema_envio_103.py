'''
sistema de envio
costo nacional =$10 x kg
costo internacional = 20 x kg
solicitar: destino (nacional o internacional)
peso : kg del paquete
imprimir costo del envio
'''

print("***SISTTEMA DE ENVIO***")

costo_nacional = 10
costo_internacional = 20

destino =input ("¿Tu envio es nacional o internacional ?:   ")
peso = float(input("¿Cuántos kg vs a enviar?:   "))

destino_seleccionado = destino .strip() .lower() =="nacional" 

if destino_seleccionado:
    costo_envio =  costo_nacional * peso
    
    print(f"Su envio es de $ {costo_envio} por enviar {peso} ")
else:
   
    costo_envio = costo_internacional * peso
    print(f"Su envio es de $ {costo_envio} por enviar {peso} ")



    
    



