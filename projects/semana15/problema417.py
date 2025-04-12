#417
#Escribe una función que devuelva el índice de la primera ocurrencia de un número en una lista.


#función para detectar la ocurrencia de los números
def pri_ocu_num(lista, num):
    #try sirve para ver si el bloque de código tiene errores
    try:
        #retorna la posición del índice
        #en caso de querer buscar la primera repetición de un número se pone un +1 luego del lista.index(num)
        #esto es porque se está pidiendo que devuelva la posición del índice y luego sumarle 1 posición mas antes de devolverlo
        return lista.index(num)
    #except te permite controlar el error
    #ValueError es una exepción de Python
    except ValueError:
        return print("número no encontrado")


print("ingresar una lista de números")

#se piden los valores por parametro
num_ing = input()

#se crea la lista y se cambian los valores de num_ing a int
#el .split() es para los espacios
num_list = list(map(int, num_ing.split()))

print("ingresar el número que se desea buscar")

num_bus = int(input())

#se llama a la función y se le pasa por parametro los valores necesarios
bus_num_en_lis = pri_ocu_num(num_list, num_bus)

#se muestra el resultado con un f-string
print(f"La posición de la primera ocurrencia en la lista es {bus_num_en_lis}")