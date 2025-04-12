#270
#Define una función en Python que calcule el área de un círculo usando parámetros.


#Importe math para no definir pi
import math

def radio_circulo():

    print("ingresar el valór del radio")

    #paso el input del user a float
    radio = float(input())

    #el área de un círculo es π r², donde math.pi es π y (radio ** 2) es r²
    area_circ = math.pi * (radio ** 2)

    #se muestra con un f-string
    print(f"el área del círculo cuyo rádio es {radio}, es {area_circ}")

radio_circulo()

