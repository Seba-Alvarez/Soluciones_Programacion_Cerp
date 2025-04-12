#414
#Escribe un programa que encuentre el segundo número más grande de una lista.


#Se pide la lista de números
num_entrada = input()

#se crea la lista
#map() va a guardar en la lista los inputs y va a ejecutar una función, en este caso convertir los string a int
# split es para los espacios
lista_num = list(map(int, num_entrada.split()))

#Este es un metodo de python, .sort, la cual los ordena de forma ascendente automáticamente
#reverse = True es para que los ordene de forma descendente, por lo cual el mayor número va a estar en la posición 0
lista_num.sort(reverse = True)

#Se imprime la posición 1, que es el segundo mayor
seg_num_mayor = lista_num[1]

print("el segundo mayor número ingresado", seg_num_mayor)