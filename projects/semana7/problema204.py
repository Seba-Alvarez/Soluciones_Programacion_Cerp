#204

#Escribir un programa en Python que genere una secuencia de números Fibonacci,
#leyendo la cantidad de números que se desea generar.


print("ingrese la cantidad de números que desea saber de la secuencia de Fibonacci")
numSeqFib = int(input())

#Se declaran los primeros 2 valores de la secuencia por si se selecciona 1 o 2 números de la secuencia
a = 0
b= 1

#si se selecciona 1, se muestra el 0 (el primer número de la secuencia)
if numSeqFib >= 1:
    #Puse un end, para que no entre al for
    print(a, end=" ")
if numSeqFib >=2:
    print(b, end=" ")

#Se especifica que el rango arranca en 2, hasta la cantidad seleccionada
for i in range (2, numSeqFib):
    #Asi se calcula el número de Fibonacci
    c = a + b
    print(c, end=" ")
    #Esto actualiza los valores de a y b, para que en la siguiente pasada del búcle a y b sean los valores actuales
    a, b = b, c