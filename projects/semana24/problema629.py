#629
#Escribe una función que reciba como parámetro una lista de enteros y elimine los elementos duplicados.


#función para eliminar duplicados, se le pasa una lista de números por parametro
def eliminar_dupes(lista):
    #se crea una lista vacía
    resul = []
    #set no permite que se entren duplicados
    dup = set()
    #se recorre la lista
    for i in lista:
        #se agregan los datos a la lista si no están duplicados
        if i not in dup:
            resul.append(i)
            dup.add(i)
    #retorna la lista
    return resul

#se pide la lista
print("ingresar una lista de números separados por espacios")
num_list = list(map(int, input().split()))

#se llama a la función
sin_dupes = eliminar_dupes(num_list)

#se muestran las listas
print(f"Lista ingresada: {num_list}")
print(f"Lista sin duplicados: {sin_dupes}")
