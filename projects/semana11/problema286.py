#286
#Escribe una función en Python que determine si un número es primo.

#Este import es para poder hacer operaciones matemáticas como raíz cuadrada
import math

def es_primo():

    print("Ingresar un número para verificar si es primo")
    num_usuario = int(input())

    if num_usuario <= 1:
        print("los números menores o iguales a 1, no pueden ser primos")
        return

    #Esta variable es para imprimir por pantalla
    num_es_primo = True

    #math.sqrt() es para hacer la raíz cuadrada del número ingresado
    #El +1 es para incluir el número seleccionado
    for i in range(2, int(math.sqrt(num_usuario)) + 1):
        #Si el número ingresado es divisible por otro número además de 1 o sí mismo, no es primo
        if num_usuario % i == 0:
            num_es_primo = False
            #Se termina el loop
            break
    if num_es_primo:
        print(num_usuario, "es primo")
    else:
        print(num_usuario, "no es primo")

es_primo()
