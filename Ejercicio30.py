"""En un comercio se venden tres modelos de frascos codificados uno, dos y tres. Ingresando un código, se quiere imprimir la descripción según detalle:\\\\
1 -chico. 2- mediano. 3- grande."""
eleccion=int(input("Bienvenido, hay disponible 3 modelos de fracos codificados \n1. Modelo uno \n2. Modelo dos\n3. Modelo tres\nElija una opcion: "))
if eleccion == 1:
    print("El modelo elegido es el chico")
elif eleccion == 2:
    print("El modelo elegido es el mediano")
elif eleccion == 3:
    print("EL modelo elegido es el grande")
else:
     print("Codigo invalido")
