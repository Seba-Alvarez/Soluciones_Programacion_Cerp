#216

"""Escriba un programa en C para hacer un patrón como una pirámide con números aumentados en 1"""

print("numero para iniciar")
numInicio = int(input())
print("numero de pisos deseados (ej: 10 creara una pirámide de 10 pisos)")
numPisos = int(input())
#Se inicia en 1, en vez de en 0, para que cuente el numInicio
numDisp = 1

#Se hace un for para que agregue una columna mas cada vez
for i in range (numPisos + 1):
    #Otro for para hacer que numInicio se sume, en vez de imprimir siempre el mismo
    for ii in range (i):
        #end es una función de print(), esta agrega un salto de línea al final de cada número
        #Cuando imprime el salto de línea depende de la cantidad de pisos seleccionados
        print(numInicio, end="")
        numInicio = numInicio + 1
    print()