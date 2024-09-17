#leer un número comprendido entre uno y siete, ambos inclusive
num=int(input("Ingrese un numero del 1 al 7: "))
#Se le da un valor numerico a cada dia de la semana
if num == 1:
    dia = "Lunes"
elif num == 2:
    dia = "Martes"
elif num == 3:
    dia = "Miercoles"
elif num == 4:
    dia = "Jueves"
elif num == 5:
    dia = "Viernes"
elif num == 6:
    dia = "Sabado"
elif num == 7:
    dia = "Domingo"
else:
    dia = "No existe"
#imprimir el nombre del día de la semana correspondiente
print(f"El correspondiente de la semana es {dia}")