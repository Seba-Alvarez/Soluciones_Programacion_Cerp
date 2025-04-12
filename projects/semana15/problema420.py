#420
#Escribe un programa que muestre el número que aparece más veces en una lista.


#se importa la función Counter para contar
from collections import Counter

#la función donde se le pasa una lista por parámetros para que cuente el elemento que mas aparece
def cual_apa_mas(lista_num):
    #se guarda el contador el la variable
    cont = Counter(lista_num)
    #num_sel recibe el número más frecuente
    #num_veces recibe el conteo del counter
    # most_common devuelve una lista de tuplas con el número mas frecuente y cuantas veces aparece.
    #esto se guarda en las variables
    #el (1) es para guardar el que mas se repite
    #el [0] es la posición en la que se va a guardar el número en la lista
    num_sel, num_veces = cont.most_common(1)[0]
    #retorna el número
    return num_sel

#se pide el número
num = input()

#se crea la lista y se pasa el input a int
num_list = list(map(int, num.split()))

#se llama la función con la lista creada
resul_num = cual_apa_mas(num_list)

#se muestra el número que mas aparece por pantalla con un f-string
print(f"el número que mas aparece en la lista es {resul_num}")