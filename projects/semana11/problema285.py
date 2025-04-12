#285
#Crea una función en Python que reciba una cadena y devuelva cuántas veces aparece cada letra.


#Esto importa la función de contador de Python
from collections import Counter

def contar_letras():

    print("ingresar una frase")
    cant_letra = input()

    #.replace es para remplazar espacios vacios a la hora de contar las letras
    cant_letra = cant_letra.replace(" " , "")

    contador = Counter(cant_letra)

    print("ingresar letra para saber cuantas veces se repite")
    bus_letra = input()

    #si la letra ingresada está en la frase, te muestra las veces que se repite
    #contador[bus_letra] es para acceder al número de repeticiones directamente
    if bus_letra in contador:
        print(f"la letra {bus_letra} se repite {contador[bus_letra]} veces")
    else:
        print(f"la letra {bus_letra} no se encuentra en el texto")

contar_letras()
