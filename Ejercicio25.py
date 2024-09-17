#Dado un número entero positivo menor que cien, leído desde teclado, indicar si es primo.
# (Los números primos son aquellos que sólo son divisibles por si mismos y por uno.- En el caso del ejemplo, por ser el número leído menor que cien,
# sólo hay que comprobar que el número no sea 2 - 3 - 5 - 7 o múltiple de alguno de estos. Si se cumple esta condición, se trata entonces de un número primo
numero=int(input("Ingrese un numero mayor que 1 y menor que 100: "))
if numero in (2, 3, 5, 7):
    print("El numero ingresado es primo")
elif numero < 2 or numero%2 == 0 or numero < 3 or numero%3 == 0 or numero < 5 or numero%5 == 0 or numero < 7 or numero%7 == 0:
    print("el numero ingresado no es primo")
else:
    print("El numero ingresado es primo")