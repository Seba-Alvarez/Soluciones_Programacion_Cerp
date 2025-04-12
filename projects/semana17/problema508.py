#508
#Crea una clase Fecha y determina cuál de dos fechas ingresadas es más reciente.


import datetime

class Fecha:
    def __init__(self, fecha_str):
        #convierte el string a un objeto datetime
        self.fecha = datetime.datetime.strptime(fecha_str, "%d,%m,%Y")

    def __str__(self):
        #convierte el objeto datetime a un string
        return self.fecha.strftime("%d,%m,%Y")

#se piden las fechas
print("ingresar fecha 1")
fec_1 = input()
print("ingresar fecha 2")
fec_2 = input()

#aca se crean las instancias a la clase fecha y se pasan las fechas ingresadas por parámetro
fecha_1 = Fecha(fec_1)
fecha_2 = Fecha(fec_2)

#se comparan e imprimen las fechas
if fecha_1.fecha > fecha_2.fecha:
    print(f"la fecha {fecha_1} es mayor")
elif fecha_1.fecha < fecha_2.fecha:
    print(f"la fecha {fecha_2} es mayor")
else:
    print("las fechas son iguales")