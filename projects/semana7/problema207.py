#207
"""Un triplete de Pitágoras es un conjunto de tres números naturales, x < y < z, para los cuales,
x² + y² = z². Existe exactamente un triplete de Pitágoras para el cual x + y + z = 1000.
Escribir un programa en Python para encontrar el producto xyz."""


#se inicia el for y se chequea que el rango de x incluya el 1 y el 1000
for x in range (1, 1000):
    #en este for se busca el segundo número del triplete, donde se inicia desde x no repetir el valor
    #porque x & y no pueden ser iguales
    for y in range (x, 1000):
        #z es la diferencia entre x + y
        z= 1000 - x - y
        #este if se pone a esta altura, porque esta actuando sobre si los tres números sumados dan 1000
        #x**2 es x²
        if x**2 + y**2 == z**2:
            #cuando encuentre los valores correctos de x, y & z los va a imprimir por pantalla
            print("El triplete de Pitágoras para el cual x + y + z = 1000 es", "x=",x, "y=", y, "z=", z)
            #Si encuentra la combinación correcta antes de recorrer todos los números, el break hace que
            #el búcle termine.
            break