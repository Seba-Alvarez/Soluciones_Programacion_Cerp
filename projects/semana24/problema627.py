#627
#Escribe una función que reciba como parámetro una lista de enteros la ordene utilizando bubble sort.


#se pide que sean números específicamente porque no está hecha para caracteres
print("insertar lista de números enteros separada por espacios")
#aca se pasan los caracteres ingresados a valores numéricos
num_list = list(map(int, input().split()))

#Me lo robé de w3shcool
# https://www.w3schools.com/dsa/dsa_algo_bubblesort.php

#se le asigna n el valor del largo de la lista ingresada
n = len(num_list)
#recorre la lista empezando por el primer valor hasta el ante último
for i in range(n-1):
    #condición bool para que salga del for cuando termine de ordenar
    swapped = False
    #recorre los números para poder compararlos
    for j in range(n-i-1):
        #compara dos números para ver cuál es mayor
        if num_list[j] > num_list[j+1]:
            #si el primer número es mayor al segundo los cambia de lugar
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            swapped = True
    #si ya los ordenó todos sale del bucle
    if not swapped:
        break

#imprime la lista ordenada
print("Lista ordenada:", num_list)