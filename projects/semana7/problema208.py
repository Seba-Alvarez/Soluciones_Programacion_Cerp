#208

"""Se desea escribir un programa en C que permita calcular la suma de
'n' números pares a partir de un número entero m."""


#Se piden los valores a usar
print("ingresar el número de inicio ")
numero1 = int(input())
print("ingresar la cantidad de números pares a sumar ")
numero2 = int(input())


#Se declaran variables numéricas para hacer la posterior suma
sumaPares = 0

#bucle para sumar los números pares la cantidad de veces elegidas en el segundo número
for i in range(numero2):
    #hace que el valor de la suma, sea el del primer número par
    sumaPares += numero1
    #suma 2 para continuar el bucle
    numero1 += 2

print("la suma de", numero1, "números pares a partir de", numero2, "es", sumaPares)