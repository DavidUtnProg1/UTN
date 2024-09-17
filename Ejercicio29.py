#Leer tres números
num1=float(input("Ingrese el primer valor numerico: "))
num2=float(input("Ingrese el segundo valor numerico: "))
num3=float(input("Ingrese el tercer valor numerico: "))
#sumarlos
suma= num1+num2+num3
#Verificar si la suma de los 3 numeros ingresados es menor que 10
if suma > 10:
    raizcuadrada= suma**0.5 # calcular la raíz cuadrada
    print(f"La raiz cuadrada de la suma de los tres numeros es: {raizcuadrada}")
else:
    print("La suma de los 3 numeros es menor que 10, ingrese 2 valores mas: ")
    # leer dos números más
    num4=float(input("Ingrese el primer valor: "))
    num5=float(input("Ingrese el segundo valor: "))
    #sumarios junto a los primeros, luego imprimir la suma
    print(f"la suma de los numero ingreaso es igual a: {num4+num5+suma}")