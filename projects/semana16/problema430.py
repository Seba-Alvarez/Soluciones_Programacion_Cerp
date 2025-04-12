#430
#Escribe una función que devuelva solo los elementos mayores que un número dado.


#función para hacer el cálculo
#el primer i es el valor que se va a agregar a la lista, si cumple con la condición de ser mayor que el número ingresado
#el segundo i es para que el for recorra la lista
#el tercer i es para la comparación, si el número que se esta recorriendo es mayor que el número ingresado, se agrega a la lista
def mayor_que_numero(array, num_ing):
    return [i for i in array if i>num_ing]

#se piden los datos por parametro
print("ingresar la lista de números, separado por espacios")

num_list = input()

num = list(map(int, num_list.split()))

print("ingresar el número que se desea comparar")

max_num = int(input())

#se guarda en una variable el resultado de la función con los datos ingresados para hacer las comparaciones
res_num = mayor_que_numero(num, max_num)

#se muestran los datos pedidos en un f-string
print(f"Números mayores que {max_num} son {res_num}")