#Leer tres números, si el segundo es negativo, calcular la raíz cuadrada de la suma de los restantes; en caso contrario imprimir un mensaje de error
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
if num2 < 0 : #verificacion si es negativo
    suma=num1+num3
    raizcuadrada= suma**0.5 #raizcuadrada
    print(f"la raiz cuadrada de la suma de los restantes; {suma} es: {raizcuadrada}")
else:
    print("Error, el segundo numero no es negativo")