# 413
# Escribe una función que cuente cuántas veces aparece un carácter en una cadena.


from itertools import count

def cont_str():

    #se pide la frase para buscar
    print("ingresar una cadena de caracteres")
    cad_con = input()

    #se pide la letra que se quiere buscar
    print("ingresar el caracter que se desea buscar")
    car_con = input()

    #se inicializa una variable contador, donde usando .count() cuenta las veces que se repite la letra a buscar
    cont = cad_con.count(car_con)

    #un f-string para mostrar el resultado
    print(f"el caracter {car_con} se repite {cont} veces")

cont_str()