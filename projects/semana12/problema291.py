#291
# Crea una función en Python que devuelva el mínimo común múltiplo entre dos enteros.

#fundamental
import math

def mcm_ent():
    print("ingresar el primer número")
    num1 = int(input())
    print("ingresar el segundo número")
    num2 = int(input())

    # gcd() es una función de python que da el máximo común divisor
    max_c_d = math.gcd(num1, num2)

    # abs() da el valor absoluto del número
    #// es una división que redondea para abajo
    min_c_m = abs(num1 * num2) // max_c_d

    print(f"el mínimo común denominador de {num1} y {num2} es {min_c_m}")

mcm_ent()
