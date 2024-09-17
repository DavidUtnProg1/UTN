#leer monto total de la venta y el tipo de cliente
montoventa=float(input("Ingrese el monto de la venta: "))
tipocliente=int(input("tipo de cliente:\n1. Estudiante \n2. Docente \n3. Resto \n ingrese la opcion correcta: "))
#estudiantes reciben 10% de descuento, docente se le anota en su cuenta, resto de personas paga el monto total
if tipocliente == 1:
    descuento=montoventa*0.10
    montodescuento= montoventa-descuento
    print(f"El importe es ${montoventa}, se le descuentan ${descuento}. Debe pagar ${montodescuento}")
elif tipocliente == 2:
    print(f"Se agrego ${montoventa} a su cuenta")
elif  tipocliente == 3:
    print(f"Debe pagar ${montoventa}")
else:
    print("El número ingresado no corresponde a un tipo de cliente válido ")