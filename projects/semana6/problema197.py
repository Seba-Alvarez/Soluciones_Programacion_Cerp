#197
"""Escribir un programa en Python que calcule el promedio de calificaciones de un estudiante,
leyendo la cantidad de materias y las calificaciones correspondientes."""


#Se cra un diccionario llamado materias y se le pide al usuario que ingrese el nombre y las notas de c/u
Materias = dict( materia1 = input(),
                 nota1 = int(input()),
                 materia2 = input(),
                 nota2 = int(input()),
                 materia3 = input(),
                 nota3 = int(input())
                 )
#Se hace el promedio, llamando a las variables en el diccionario
promedio = (Materias["nota1"] + Materias["nota2"] + Materias["nota3"]) / 2

#Se imprime el diccionario con todas las materias y notas
print(Materias)
#Se imprime el resultado
print("el promedio del alumno es", promedio)