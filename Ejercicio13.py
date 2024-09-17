import math
base=float(input("Ingrese la base del triangulo en cm: "))
altura=float(input("Ingrese la altura del triangulo en cm"))
angulo=math.radians(float(input("ingrese el valor del angulo: ")))

print(f"la superficie del triangulo es: {(altura*base)/2}")
print(f"base={base}    valor del primero lado={base*math.sin(angulo)}     valor del segundo lado: {base*math.cos(angulo)}")