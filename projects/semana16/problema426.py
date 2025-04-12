#426
#Escribe un programa que encuentre el número con mayor diferencia con sus vecinos.


#función para hacer los calculos
def mayor_diferencia(array):

    #variable para comparar después
    max_dif = 0
    #variable para comparar números vecinos, por eso es [1], que es la posición 2 en el array
    max_num_dif = array[1]

    #se recorre desde la posición [1], la segunda del array, pero la primera que tiene números vecinos en ambos lados
    #hasta el ante último número, es decir el último que tiene vecinos en ambos lados
    for i in range(1, len(array) - 1):
        #abs es para calcular la diferencia con los vecinos en números absolutos
        #array[i] es la posición del array que está recorriendo el for y array[i-1] es la posición anterior
        #de la misma manera array[i] y array [i+1] son la posición actual y la que le sigue
        #el + es para obtener la diferencia numérica y almacenarla en la variable dif
        dif = abs(array[i] + array[i -1]) + abs(array[i] + array[+1])

        #se compara la diferencia almacenada con la actual hasta que se termine el for
        if dif > max_dif:
            #se pone el valor de la mayor diferencia en la variable diferencia
            max_dif = dif
            #aca se guarda la posición del número encontrado
            max_num_dif = array[i]
    #devuelve el número con mayor diferencia
    return max_num_dif

#aca se piden los datos

print("ingresar los números que conforman la lista")
num_list = input()

#se convierte los string ingresados a números enteros para poder hacer los calculos cuando llamemos a la función
num = list(map(int, num_list.split()))

#aca se llama a la función con los parámetros ingresados en num para que haga los calculos
res_func = mayor_diferencia(num)

#aca se muestra el resultado de la función
print(f"El número con mayor diferencia con sus vecinos es {res_func}")