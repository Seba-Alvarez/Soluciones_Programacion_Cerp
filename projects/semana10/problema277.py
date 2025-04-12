#277
#Escribe una función que devuelva el número máximo en una lista de números.

#Se define la función
def function_max_num():
    print("ingrese números para ver cual es el mayor de los ingresados")
    #Se piden los números, al pedirlos como string hay que pasarlos a int
    user_num = input()
    #Se forma la lista y se usa map() para mandar los números ingresados a parámetros de la función
    # .split() se usa para generar espacios cuando se muestra por pantalla y aceptar los espacios al ingresarlos
    list_user_num = list(map(int, user_num.split()))

    #[0] quiere decir el primer elemento de la lista, pues estas arrancan desde la posición 0
    #Se inicializa una variable para poder comparar los números y saber cual es el mayor.
    max_num = list_user_num[0]

    #Bucle para recorrer los números de la lista
    for i in list_user_num:
        #Si pregunta si el número actual es mayor a max_num
        if i > max_num:
            #Si se cumple lo anterior, max_num pasa a ser i
            max_num = i
    print("el número mas grande de los ingresados es", max_num)
#Se llama a la función para que se ejecute
function_max_num()
