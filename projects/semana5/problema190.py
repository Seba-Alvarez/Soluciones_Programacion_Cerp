#190
#Escribir un programa en Python que calcule la suma de los números pares e impares en un rango dado por el usuario.

#Se piden los números
print("ingrese 2 números para calcular la suma de números pares e impares dentro del rango")

#Se ingresan los números
numero1 = int(input())
numero2 = int(input())

#Se declaran variables numéricas para hacer la posterior suma
sumaPares = 0
sumaImpares = 0

#Se hace un búcle para recorrer los números
for i in range(numero1, numero2):
    #Si el número es par se agrega la suma de los números por el for y se suman con las variables suma par
    if i % 2 == 0:
        sumaPares = sumaPares + i
    #Si el número es impar se agrega la suma de los números por el for y se suman con las variables suma impar
    elif i % 2 != 0:
        sumaImpares = sumaImpares + i
#Se imprimen las sumas por pantalla
print("La suma de pares entre", numero1, "y", numero2, "es", sumaPares)
print("La suma de impares entre", numero1, "y", numero2, "es", sumaImpares)
