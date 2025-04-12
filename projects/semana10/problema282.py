#282
#Crea una función en Python que reciba un número entero y devuelva su reverso.


#Se define la función
def dev_rev_num (num_a_dev):
    #num_neg es para permitirme preguntar si el numero ingresado es negativo
    num_neg = num_a_dev < 0
    # abs() se usa para devolver el valor absoluto del número
    num_a_dev = abs(num_a_dev)

    #[::-1] se usa para invertir la cadena de texto ingresada
    rev_numero = int(str(num_a_dev)[::-1])

    if num_neg:
        #Al ingresar -número, se conserva el símbolo de negativo
        #Esta línea es para conservar el símbolo del número negativo
        return -rev_numero
    #si no es negativo, simplemente devuelve el número
    else:
        return rev_numero

print("ingrese un número")
num_usuario = int(input())

#se usa un f-string para devolver el número inverso usando la función.
print(f"El reverso del número es: {dev_rev_num(num_usuario)}")
