#292
#Escribe una función en Python que cuente la cantidad de palabras en una cadena.


def cont_pal(cadena_tex):

    #strip() se usa para eliminar los posibles espacios al principio y al final
    #split() se usa para separar strings
    pal = cadena_tex.strip().split()

    #len() se usa para retornar el número de items en un objeto, como palabras en una lista en este caso
    cant_pal = len(pal)

    return cant_pal

print("ingresar una frase para contar la cantidad de palabras")
pal_usuario = input()

#Esto es para que la función cuente las palabras ingresadas por el usuario
res_cont_pal = cont_pal(pal_usuario)

print(f"la cantidad de palabras ingresadas es {res_cont_pal}")
