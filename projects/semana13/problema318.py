#Escribe un programa que combine dos listas de enteros en orden ascendente.


#se crea la función y se le pasan dos listas por parametro
def ord_lis(lis_1, lis_2):
    #se unen las dos listas en una sola
    lis_comb = lis_1 + lis_2
    #se ordenan de forma ascendente con .sort()
    lis_comb.sort()
    #se retorna la lista ordenada
    return lis_comb


print("ingresar los números de la primera lista")

#se piden los valores por parametro
num_ing_1 = input()

#se crea la lista y se cambian los valores de num_ing_1 a int
#el .split() es para los espacios
num_list_1 = list(map(int, num_ing_1.split()))

print("ingresar los números de la segunda lista")

#se piden los valores por parametro
num_ing_2 = input()

#se crea la lista y se cambian los valores de num_ing_2 a int
#el .split() es para los espacios
num_list_2 = list(map(int, num_ing_2.split()))

num_list_3 = ord_lis(num_list_1, num_list_2)

print(f"la lista combinada y ordenada es: {num_list_3}")