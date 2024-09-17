#Leer tres números
num1=float(input("Ingrese el primer valor: "))
num2=float(input("Ingrese el segundo valor: "))
num3=float(input("Ingrese el tercer valor: "))
#si el primero es uno,sumar el segundo y el tercero
if num1 == 1:
    print(f"la suma del segundo numero y tercero es: {num2+num3}")
# si es dos multiplicarlos
elif num1 == 2:
    print(f"El producto del segundo numero y el tercero es: {num2*num3} ")
#si es tres dividirlos
elif num1 == 3:
    if num2 == 0 or num3 == 0:
        print("No se puede dividir por 0")
    else:
          print(f"El cociente del segundo numero y el tercero es: {num2/num3}")
#si es cuatro,la raíz cuadrada de la suma de sus cuadrados
elif num1 == 4:
    suma= (num2**2)+(num3**2)
    raizcuadrada= suma**0.5
    print(f"La raiz cuadrada de la suma de los cuadrados del segundo numero y el tercero es: {raizcuadrada}")
#cualquier otro valor indicar que se trata de un error
else:
    print("Error, introduzca un valor del 1 a 4")


