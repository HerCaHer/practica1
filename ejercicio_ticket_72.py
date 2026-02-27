#Generacion de tickets de venta
import os

os.system("cls") #limpiar pantalla en windows

'''comprar varios articulos, y queremos obtener el ticket de venta total incuyendo impuestos, 
se solicita el precio de cada producto y el usuario debera incluir su precio (decimales), 
el sistema debe realizar la suma de cada producto, calcular el impuesto  y finallmente inprimir el total de la compra'''

print(" *** Generación de ticket de venta ***")

precio_leche = float(input("Ingrese el precio de la leche: "))
precio_pan = float(input("Ingrese el precio del pan: "))
precio_lechuga = float(input("Ingrese el precio de la lechuga: "))
precio_platanos = float(input("Ingrese el precio de los plátanos: "))
descuento=int(input("Ingrese el porcentaje de descuento: que desea aplicar: (%)  "))

subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos
total_con_descuento = subtotal - (subtotal * descuento / 100)
impuesto = total_con_descuento * 0.16 #suponiendo un impuesto del 16%
total_con_impuesto = total_con_descuento + impuesto

print(f'''
      

      subtotal: {subtotal:.2f}
      descuento: {subtotal * descuento / 100:.2f}
      impuesto: {impuesto:.2f}
      Total a pagar: {total_con_impuesto:.2f}


Gracias por su compra!


''')

