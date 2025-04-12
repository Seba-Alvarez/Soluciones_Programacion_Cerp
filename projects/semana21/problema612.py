#612
#Crea una clase llamada «»Fecha»» que contenga los campos día, mes y año.
# Luego, crea una función que reciba una Fecha y verifique si la fecha es válida o no.


#se importa datetime de la libreria de python
import datetime

#se cra la clase fecha con el validador incluido
class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia = int(dia)
        self.mes = int(mes)
        self.anio = int(anio)
        self.fecha_valida = self.validar_fecha()

    def validar_fecha(self):
        try:
            datetime.datetime(self.anio, self.mes, self.dia)
            return True
        except ValueError:
            return False

    #para verificar si la fecha es válida y para definir el formato
    def __str__(self):
        if self.fecha_valida:
            es_val = "(la fecha ingresada es válida)"
        else:
            es_val = "(la fecha ingresada no es válida)"
        return f"Fecha: {self.dia:02d}-{self.mes:02d}-{self.anio} {es_val}"

#se crea la lista de fechas
class ListaF:
    def __init__(self):
        self.fechas = []

    #alta de fechas
    def agregar_fechas(self, dia, mes, anio):
        fecha = Fecha(dia, mes, anio)
        self.fechas.append(fecha)

    #mostrar fechas
    def mostrar_fechas(self):
        if not self.fechas:
            print("No hay fechas ingresadas.")
            return

        for fecha in self.fechas:
            print(fecha)

# menu simple
def menu_fechas():
    lista_fechas = ListaF()

    while True:
        print("\n1. Agregar fechas")
        print("2. Mostrar fechas")
        print("3. Salir")

        nav_menu = input("Ingresar número del 1 al 3 para operar el menú: ")

        #pasar los datos por parámetro a la función alta
        if nav_menu == "1":
            dia = input("Ingresar día: ")
            mes = input("Ingresar mes: ")
            anio = input("Ingresar año: ")
            lista_fechas.agregar_fechas(dia, mes, anio)

        #llamar a la función mostrar
        elif nav_menu == "2":
            lista_fechas.mostrar_fechas()

        #para salir del menu
        elif nav_menu == "3":
            print("Saliendo")
            break

        #por si se ingresa algo distinto que 1, 2 o 3
        else:
            print("Ingresar número 1, 2 o 3")

#para correr el programa
if __name__ == "__main__":
    menu_fechas()