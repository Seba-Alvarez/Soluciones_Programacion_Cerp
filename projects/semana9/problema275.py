#275
#Escribe una función en Python que calcule el factorial de un número entero positivo.


def calcular_fact():
    print("ingresar un número para calcular el factorial")
    num_calc = int(input())

    #Esto es solo para las anticipaciones de ingresar 0 y 1
    if num_calc == 0 or num_calc == 1:
        print("el factorial de", num_calc, "es 1")
        #este return es para que no muestre lo mismo 2 veces
        return 1

    #Variable para calcular el factorial
    res_fact = 1

    #Se arranca en 2, por lo mencionado en el if de más arriba y se usa el +1 para incluir el número seleccionado
    for i in range(2, num_calc + 1):
        #multplica e iguala a al número actual del búcle
        res_fact *= i
    #muestra el resultado
    print("el factorial de", num_calc, "es", res_fact)

calcular_fact()