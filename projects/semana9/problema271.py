# 271
# Define una función en Python que calcule el promedio de una lista de números.



def calc_pro():
    print("ingresar números separados por espacios")
    num_usuario = input()

    #se crea una lista y se corre el for adentro
    #se transforma en float(decimales) los números de la lista para poder hacer el promedio
    lista_num = [float(numero) for numero in num_usuario.split()]

    #se hace el promedio
    promedio = sum(lista_num) / len(lista_num)

    #se muestra el promedio por pantalla en un f-string
    print(f"el promedio de los números ingresados es {promedio}")

calc_pro()