#613
#Escribir una función que reciba un arreglo de enteros y devuelva el valor máximo.


#función para buscar el número máximo
def val_max(lista):
    #se asigna una variable a la primera posición de la lista
    maxi = lista[0]

    #esto se llama slicing, en este caso lo usa para que recorra toda la lista
    for i in lista[1:]:
        #si encuentra un número más grande que el primero de la lista lo asigna a la variable
        if i > maxi:
            maxi = i
    #retorno la variable con el número mas grande
    return maxi

#pido la lista por consola
num_list = list(map(int, input().split()))
#llamo a la función
num_max = val_max(num_list)

print(f"Ingresar una lista de números")
#muestro por pantalla
print(f"El mayor número ingresado es {num_max}")
