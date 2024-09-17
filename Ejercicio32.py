#Se leen el sueldo y la categoría de un empleado
sueldobasico=float(input("Ingrese el sueldo basico: "))
categoria=int(input("Ingrese la categoria que pertenece: "))
#Para calcular el sueldo neto se efectúan los siguientes descuentos:
#Categoría 1: 30%
#Categoría 2: 25%
#Categoría 3: 25%
#Categoría 4: 10%
if categoria == 1:
    descuento = 0.30
elif categoria == 2:
    descuento = 0.25
elif categoria == 3:
    descuento = 0.25
elif categoria == 4:
    descuento = 0.10
#Para otras Categorías no hay descuentos
else:
    descuento = 0.00
sueldoneto = sueldobasico-(sueldobasico*descuento)
#Imprimir el sueldo neto básico y Categoría
print(f"su sueldo basico es de: {sueldobasico}\n su categoria es {categoria}\n su sueldo neto es de: {sueldoneto}")

