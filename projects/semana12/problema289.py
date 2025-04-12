#289
#Escribe una función en Python que convierta un número entero a binario.


#se define la función
def conv_bin():

    print("Ingrese un número para convertir")
    num_dev = int(input())
    #Use esta variable vacía para poder concatenar los valores
    #se podría haber hecho una lista, pero al ser un solo número, decidi hacerlo asi
    binario = ""

    #Si el número ingresado es 0, simplemente se devuelve 0
    if num_dev == 0:
        print("el binario de 0 es 0")
        return

    while num_dev > 0:
        #Aca se calcula el binario
        #El str() es para pasar el número a string para poder concatenarlo
        #El + binario es para concatenar el siguiente número de la cuenta
        binario = str(num_dev % 2) + binario
        # // es para hacer una división que redondee hacia abajo
        num_dev = num_dev // 2

    print("el binario de", num_dev, "es", binario)

conv_bin()
