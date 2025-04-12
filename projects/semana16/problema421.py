#421
#Escribe un programa que ordene una lista de enteros usando selección.


print("ingrese una lista de números")
#list es para crear la lista
#map(int) es para convertir todos los números ingresados a int
#input().split() hace que se puedan ingresar los números separados por espacios
#se usa una , en lugar de () para convertir a int lo ingresado por consola
list_num = list(map(int, input().split()))

#este código lo saque de aca https://www.w3schools.com/dsa/dsa_algo_selectionsort.php
#se define x como el largo de la lista
x = len(list_num)
#este for busca, desde la posición 0 de la lista busca el elemento mas pequeño
for i in range(x):
    #esta variable es para igualar i con el menor número de i, que es a su vez el número que esta recorriendo el for en este momento
    index_min = i
    #este for busca el siguiente número mas pequeño dentro del recorrido del primer for
    for y in range(i+1, x):
        #este if es para comparar el número encontrado en el segundo for, para saber si es menor que el buscado en el primer for
        if list_num[y] < list_num[index_min]:
            #si el número encontrado es mas pequeño, se guarda, sino, el bucle sigue hasta encontrarlo
            min_index = y
    #list_num[i] es el número i (el que se recorre en el primer for)
    #list_num[index_min] es el número mas chico a partir de la posición del número i
    #el = es para realizar el "intercambio" de números que define el algoritmo
    #donde list_num[i] toma el valor de list_num[index_min]
    #y list_num[index_min] toma el valor de list_num[i]
    list_num[i], list_num[index_min] = list_num[index_min], list_num[i]

print("Los números ingresados, ordenados quedan asi:", list_num)