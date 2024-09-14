#Hacer un programa que ingresando como datos:
#a. Kms. recorridos por un vehículo.
#b. Precio del combustible por litro.
#c. Kms. recorridos por cada litro
#i. La cantidad de litros consumidos
#ii. Importe gastado en combustible.
#iii. Imprimir los resultados
#iv. Ejemplificar y realizar la prueba de escritorio

km=float(input("Ingrese la cantidad de km reccoridos por el vehiculo: "))
kmp=float(input("Ingrese el precio del combustible por litro: "))
kmr=float(input("Ingrese la cantidad de kms por litro consumidos: "))

print(f"la cantidad de litros consumidos: {kmr*km} ")
print(f"importe gastado en combustible: {kmp*kmr}")

