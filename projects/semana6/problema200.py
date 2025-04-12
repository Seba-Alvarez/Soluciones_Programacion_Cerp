#200
"""Escribir un programa en Python que calcule el factorial de un número leído del usuario,
utilizando un ciclo for."""


print("ingresar el numero del cual se quiere saber el factorial")
#Se pide el número al cual hacerle factorial
num_fact = int(input())
#Siendo que el factorial de 1 es 1
#El factorial de 0 es 0
#Y no se puede hacer factorial con números negativos (según google no se puede y yo le creo)
#Inicio el factorial en 1
factorial = 1

#Se hace un for entre el rango del 1 hasta el número seleccionado
for i in range(1, num_fact + 1):
    #Se hace que factorial sea, factorial(la variable creada) * cada número que va a recorrer el for
    factorial = factorial * i

print("el factorial de", num_fact, "es", factorial)