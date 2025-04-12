#620
#Crea una función que reciba como parámetro una lista de números enteros y retorne el valor máximo y mínimo de la lista.


print("ingresar una lista de números enteros para ver el valor máximo y minimo")

#se define la función
def min_maxing (lista):
    #se usan las funciones min y max de python
    val_max = max(lista)
    val_min = min(lista)
    #se retornan los valores
    return  val_min,val_max

#se piden los números
num_lis = list(map(int, input().split()))
#se llama a la función
mini, maxi = min_maxing(num_lis)

#se muestran los resultados por pantalla
print(f"La lista ingresada: {num_lis}")
print(f"el valor máximo: {maxi}")
print(f"el valor minimo: {mini}")