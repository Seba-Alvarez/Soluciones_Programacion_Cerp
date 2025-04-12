#519
#Crea una función que valide si una fecha representada por una clase es válida.


import datetime

class Persona:
    def __init__(self, nombre, apellido, fecha_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.fecha_valida = None

    def __str__(self):
        if self.fecha_valida:
            es_val = "(la fecha ingresada es válida)"
        else:
            es_val = "(la fecha ingresada no es válida)"
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha de nacimiento: {self.fecha_nac} {es_val}"

class ListaP:
    def __init__(self, ran_fec_ini, ran_fec_fin):
        self.ran_fec_ini = ran_fec_ini
        self.ran_fec_fin = ran_fec_fin
        self.personas = [
            Persona("ramon", "ramirez", "12,10,2000"),
            Persona("hernan", "hernandez", "01/01/2023"),
            Persona("gonzalo", "gonzalez", "12,12,2200"),
            Persona("benito", "benitez", "01,01,1909")
        ]

    def validar_fecha(self, fecha_str):
        try:
            fecha = datetime.datetime.strptime(fecha_str, "%d,%m,%Y")

            if fecha > self.ran_fec_fin:
                return False
            if fecha < self.ran_fec_ini or fecha == self.ran_fec_ini:
                return False
            return True
        except ValueError:
            return False

    def mostrar_personas(self):
        for persona in self.personas:
            persona.fecha_valida = self.validar_fecha(persona.fecha_nac)
            print(persona)

def menu_personas():
    fec_ini = datetime.datetime(1910, 1, 1)
    fec_fin = datetime.datetime.now()
    persona = ListaP(fec_ini, fec_fin)

    while True:
        print("\n1. Mostrar Personas")
        print("2. Salir")

        nav_menu = input("Ingresar número 1 o 2 para operar el menú: ")

        if nav_menu == "1":
            persona.mostrar_personas()

        elif nav_menu == "2":
            print("Saliendo...")
            break

        else:
            print("Ingresar número 1 o 2")

# Para que corra el programa
if __name__ == "__main__":
    menu_personas()