tarifacompleta= 150.0 #Tarifa completa, dato sacado del enunciado
"""Menores de 4 años pasan gratis
Menores de 12 pagan 1/3 de tarifa
Menores de 18 pagan media tarifa
Adultos hasta 60 años pagan tarifa completa
Adultos mayores y jubilados pagan media tarifa"""
edad=int(input("Ingrese la edad: "))
if edad < 4:
    tarifa=0
elif edad < 12:
    tarifa=tarifacompleta/3
elif edad < 18 or edad > 60:
    tarifa=tarifacompleta/2
else:
    tarifa=tarifacompleta
print(f"el precio a pagar es de $ {tarifa}")






