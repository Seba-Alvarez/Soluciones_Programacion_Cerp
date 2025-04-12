#634
#Crea una función que, dada una lista de enteros devuelva la suma de todos los elementos.


#se piden los números
print("ingresar una lista de números enteros")

#se crea la función
def suma_lista():
    #se crean los inputs y se pasan a números
    num_lis = list(map(int, input().split()))
    #se usa el metodo sum para hacer la suma
    suma = sum(num_lis)
    #se retorna la variable donde se guardo el metodo
    return suma

#se llama a la función
res = suma_lista()

#se muestra el resultado por pantalla
print(f"La suma de todos los elementos es {res}")