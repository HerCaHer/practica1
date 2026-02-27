'''
si el cliente ha comprdo mas de $1000, y es miembro de la tienda  tiene descuento de 10%  
si solo es miembro de la tienda tiene descuento de 5%
y sino es miembre ni compro mas de $1000 no tiene descuento
'''

import os
os.system("cls")

print(" *** Descuento en tienda *** \n")
total_compra = float(input("Ingrese el total de la compra: "))
es_miembro = input("¿Es miembro de la tienda? (si/no): ").lower() == "si"
if total_compra >=1000 and es_miembro:
    descuento = total_compra * 0.10
    print(f"Tu descuento es de {descuento:.2f} y tu monto a pagar es de {total_compra - descuento:.2f}")
elif es_miembro:
    descuento = total_compra * 0.05
    print(f"Tu descuento es de {descuento:.2f} y tu monto a pagar es de {total_compra - descuento:.2f}")
else:
    descuento = 0   
    print(f"No tienes descuento, tu monto a pagar es de {total_compra:.2f}, te invitamos a ser miembro de la tienda para obtener descuentos en tus compras futuras.")


