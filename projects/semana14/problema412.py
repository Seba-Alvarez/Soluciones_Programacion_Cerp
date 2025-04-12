#412
#Escribe un programa que calcule la media aritmética de una lista de enteros.



#se importa el módulo statistics de Python
import statistics


print("ingresar valores para calcular la média aritmética")

#se piden los valores por parametro
num_ing = input()

#se crea la lista y se cambian los valores de num_ing a int
#el .split() es para los espacios
num_list = list(map(int, num_ing.split()))

#se usa el módulo .mean(), que significa la média aritmética y se le pasa la lista creada por parámetros
med_ari = statistics.mean(num_list)


#se muestra el número por pantalla
print(f"La media aritmética de la lista ingresada es: {med_ari}")