#619
#Escribir una función que reciba una cadena de caracteres y devuelva la cadena invertida.


#función para invertir caracteres el número máximo
def inv_char(invertir):
    #da vuelta lo que vas escribiendo palabra por palabra, para eso es el -1, le dice a python que vaya para atrás
    return [i [::-1] for i in invertir]

#pido la lista por consola
a_list = input().split()
#llamo a la función
inv_list = inv_char(a_list)

print(f"Ingresar una lista")
#muestro por pantalla
print(f"Lista ingresada: {a_list}")
print(f"La lista invertida es: {inv_list}")
