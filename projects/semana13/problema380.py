#380
#Define un Enum TiposVehiculo y un programa que reciba un tipo de vehículo y muestre su precio promedio.

#se importa de la libreria de python
from enum import Enum

#se genera una lista en blanco para guardar los enums
info_veh = []

print("ingresar la cantidad de vehiculos que desea ingresar")
#variable para indicar la cantidad de enums a crear
cant_veh = int(input())

#se piden los datos para los enum
print("ingresar los datos de los enum")
print("")

#el rango es el ingresado por parametro
for i in range(cant_veh):
    #se ingresa un tipo de vehiculo
    print("ingrese el tipo de vehiculo")
    nom_veh = input()
    #se ingresa el precio
    print("ingrese el precio del vehiculo")
    valor_veh = int(input())
    #se guarda entre 2 paréntesis porque es una tupla
    #las tuplas se usan para guardar multiples items en una sola variable
    info_veh.append((nom_veh, valor_veh))

#\n es para hacer una linea nueva
print("\n Vehículos ingresados")

#este for es para mostrar todos los enum ingresados
#se recorren los vehículos ingresados en el enum y se muestra la información de los mismos
#la información se guarda en info_veh, en específico, en la línea 29
for i, vehiculo in enumerate(info_veh, start=1):
    #vehículo{i} es el vehículo en la posición que esta recorriendo el for actualmente
    #{vehículo[0} y vehículo{1} muestra la información en esas posiciones de la lista.
    #en el siguiente paso del búcle {vehículo[0} y vehículo{1} pasan a ser {vehículo[2} y vehículo{3} hasta que recorra todo
    print(f"Vehiculo {i}: {vehiculo[0]} - Precio: {vehiculo[1]}")

