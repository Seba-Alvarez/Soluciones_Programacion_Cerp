#217
"""Escriba un programa en C para mostrar los n términos de la serie armónica y su suma."""


print("Ingrese el número de términos: ")
#Se piden los números
serArm = int(input())

#Se inicializa una variable para guardar la suma
suma = 0

#se hace un búcle for para hacer la série armónica
#el rango se inicia en 1, porque es el inicio de la serie y termina
# en lo que se ponga en pantalla + 1 para incluirla
for i in range(1, serArm+1):
    #f"1/{i}, es un f-string para incluir valores dentro del string de texto
    # {i} es el valor del i del for
    print(f"1/{i}")
    #Se hace la suma
    suma += 1/i
#se muestra la suma en pantalla
print("la suma de la série seleccionada es =", suma)