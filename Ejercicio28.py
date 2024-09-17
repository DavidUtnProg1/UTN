#Leer tres números distintos e imprimir el mayor
print("Escriba 3 numeros con valores distintos")
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
if num1 > num2 and num1 > num3: #verificar que el primero numero sea mayor a los restantes
    print(f"El numero mayor es el primero; {num1}")
elif num2 > num1 and num2 > num3: #verificar que el segundo numero sea mayor a los restantes
    print(f"El numero mayor es el segundo; {num2}")
else:
    print(f"El numero mayor es el tercero; {num3}")

