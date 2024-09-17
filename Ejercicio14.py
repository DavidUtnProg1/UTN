# Ingresar por teclado un lado y la hipotenusa de un triángulo rectángulo
# calcular e imprimir el lado restante, la superficie y los ángulos de dicho triángulo
import math
lado1=float(input("ingrese el valor del lado del triangulo: "))
hipotenusa=float(input("Ingrese el valor de la hipotenusa"))
print(f"lado restante: {hipotenusa**2-lado1**2}")
print(f"superficie: {((hipotenusa**2-lado1**2)*lado1)/2}")
print(f"angulo")