#Ingresar como dato el perímetro de un cuadrado. Calcular e imprimir el volumen del cubo que tiene como lado el cuadrado antes mencionado
perimetro=float(input("Ingrese el perimetro del cuadrado en cm: "))
lado = perimetro/4
print(f"el volumen del cubo es {lado**3}cm")