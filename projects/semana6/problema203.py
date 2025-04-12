#203
"""Escribir un programa en Python que calcule la suma de números pares en una secuencia de números
leídos del usuario, utilizando un ciclo for."""


#Se piden los números
print("ingrese un número para calcular la suma de números pares")

#Se ingresan los números
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
numero5 = int(input())

#Se declaran variables numéricas para hacer la posterior suma
sumaPares = 0

#Se hace un búcle para recorrer los números
for i in (numero1, numero2, numero3, numero4, numero5):
    #Si el número es par se hace la suma
    if i % 2 == 0:
        sumaPares = sumaPares + i

#Se imprimen las sumas por pantalla
print("La suma de números pares es", sumaPares)