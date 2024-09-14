#Ingresar por teclado los precios correspondientes a cinco artículos y las cantidades vendidas de cada uno de ellos.
#Calcular e imprimir el importe total de ventas de cada uno y un importe total de lo vendido \
producto1=input("ingrese el primer producto: ")
venta1=int(input("ingrese el numero de ventas del producto: "))
precio1=float(input("Ingrese el precio del producto: "))

producto2=input("ingrese el segundo producto: ")
venta2=int(input("Ingrese el numero de ventas del producto: "))
precio2=float(input("ingrese el precio del producto: "))

producto3=input("ingrese el tercer producto: ")
venta3=int(input("Ingrese el numero de ventas producto: "))
precio3=float(input("ingrese el precio del producto: "))

producto4=input("ingrese el cuarto producto: ")
venta4=int(input("Ingrese el numero de ventas producto: "))
precio4=float(input("ingrese el precio del producto: "))

producto5=input("ingrese el quinto producto: ")
venta5=int(input("Ingrese el numero de ventas producto: "))
precio5=float(input("ingrese el precio del producto: "))

ventatotal= (venta1*precio1)+(venta2*precio2)+(venta3*precio3)+(venta4*precio4)+(venta5*precio5)

print ("Ventas","\n", producto1, venta1*precio1,"\n",  producto2, venta2*precio2,"\n",  producto3, venta3*precio3, "\n",  producto4, venta4*precio4, "\n",  producto5, venta5*precio5,"\n"f"Importe total de lo vendido: {ventatotal}")