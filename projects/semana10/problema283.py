# 283
# Escribe una función en Python que devuelva el valor absoluto de un número entero.


def val_abs():

    print("ingresar un número")
    numero = int(input())

    #abs() devuelve el valor absoluto del número ingresado o especificado
    resultado = abs(numero)

    #se muestra con un f-string
    print(f"el valor absoluto de {numero} es {resultado}")

val_abs()
