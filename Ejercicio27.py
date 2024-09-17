#Leer dos números e imprimir el mayor, suponer que son distintos
num1=float(input("Ingrese el primer valor numerico: "))
num2=float(input("Ingrese el segundo valor numerico: "))
if num1 < num2:
    print(f"El numero mayor es el segundo numero; {num2}")
else:
    print(f"El numero mayor es el primer numero; {num1}")