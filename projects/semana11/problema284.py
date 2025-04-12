#284
#Define una función en Python que calcule la media geométrica de una lista de números.

def med_geometrica():

    print("ingrese números para conocer su media")
    #Aunque se van a pedir números, solo con input() devolvería string
    num_entrada = input()
    #aca se hace que los números ingresados se pasen a decimales para mayor precisión, ademas de cargarlos en la lista
    lista_num = [float(i) for i in num_entrada.split()]
    #Elegi iniciar num_prod en 1, porque si fuera 0, toda multiplicación por 0 es 0
    num_prod = 1
    #Se recorren los números ingresados
    for i in lista_num:
        #Se cambia el producto por el número que esta recorriendo
        # *= quiere decir que multiplica y que hace que num_prod = i
        num_prod *= i
    #Restorna el resultado del número de lista al cuadrado
    #Ademas se divide la cantidad de elementos de la lista dividido 1 (es parte de la fórmula)
    #Se divide por uno porque la raíz de un número es igual a elevarlo a la potencia de 1
    return num_prod ** (1/ len(lista_num))

#Se guardan los resultados de la función en la lista
res_lista = med_geometrica()

#Se llama directamente a la lista
print(f"La media geométrica de los números ingresados es : {res_lista}")
