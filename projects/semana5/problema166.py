#166
#Escribir un programa en Python que determine si un año es bisiesto.

#Se pregunta al usuario ingresar un año
print("ingrese el año que desea chequear si es bisiesto")
#Se chequea que el número ingresado sea divisible por 4
yearCheck = int(input()) % 4
#Si la condición anterior se cumple ya se imprime por pantalla, además se pregunta si el año es divisible por 100
if yearCheck == 0 or yearCheck % 100:
    #Verificar si el año es divisible por 100 y por 400
    if yearCheck == 0 and yearCheck % 400 == 0:
        #Si el año seleccionado es bisiesto se imprime por pantalla
        print("el año seleccionado es bisiesto")
    else:
        # Si el año seleccionado no bisiesto se termina el programa
        print("el año no es bisiesto")