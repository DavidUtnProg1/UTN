"""Un bar tiene la posibilidad de dividir la cuenta automáticamente desde su app web. Para ello el usuario ingresa a la web, allí ve el monto a pagar y puede ingresar
la cantidad de personas del grupo.
Se pide realizar un programa que permita el ingreso del total, luego la cantidad de personas, y como salida el monto a pagar en el siguiente formato: $ 450.5
Además, como el usuario puede ingresar accidentalmente un 0, se pide manejar la excepcion donde en caso de ocurrir se imprima el siguiente mensaje:
"Debe ingresar más de un integrate de grupo"."""

try:
    #realizar un programa que permita el ingreso del total, luego la cantidad de personas
 total=float(input("Ingrese el total a pagar: "))
 personas=int(input("Ingrese la cantidad de personas a pagar: "))
    #como salida el monto a pagar
 cuenta=total/personas
 print(f"El total a pagar es de {cuenta:.1f}")
    #como el usuario puede ingresar accidentalmente un 0, se pide manejar la excepcion
except ZeroDivisionError:
    print("Debe ingresar más de un integrate de grupo")