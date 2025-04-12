#178

#Escribir un programa en Python que determine si un número es capicúa.

print("ingrese un número")
cadNum = input()
#[::-1] sirve para invertir cadenas de caracteres, los input si no se les especifica son strings
#Aca se esta invirtiendo
cadNumInv = cadNum[::-1]
#Se chequea si los números se leen iguales de izquierda a derecha y viceversa
if cadNum == cadNumInv:
    #Si es capicúa se imprime
    print("El número", cadNum, "es capicúa")
else:
    print("El número", cadNum, "no es capicúa")