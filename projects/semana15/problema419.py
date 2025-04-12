#419
#Escribe una función que una dos listas y devuelva una lista sin duplicados.


#función para juntar las listas
# El metodo set de python no permite que existan duplicados
def dev_sin_dup(lista1, lista2):
    #se juntan las dos listas
    list_sin_dup = list(set(lista1 + lista2))
    #retorna la lista
    return list_sin_dup

#se pide los valores de la primera lista
num_1 = input()

#se crea la primera lista
num_list_1 = list(map(int, num_1.split()))

#se pide los valores de la segunda lista
num_2 = input()

#se crea la segunda lista
num_list_2 = list(map(int, num_2.split()))

#se llama a la función con los valores de las listas ingresadas
nueva_lista = dev_sin_dup(num_list_1, num_list_2)

#se muestra por consola las lista sin duplicados
print("La lista sin duplicados es:", nueva_lista)

