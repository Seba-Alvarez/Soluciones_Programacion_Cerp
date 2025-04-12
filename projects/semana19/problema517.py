# 517
# Crea una clase Empleado con nombre, salario y puesto. Muestra los datos de varios empleados.

#se crea la clase
class Empleado:
    def __init__(self, nombre, salario, puesto):
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto

    #se elige como se va a mostrar
    def __str__(self):
        return f"Nombre: {self.nombre}, Sueldo: {self.salario}, Puesto: {self.puesto}"

#se crea la lista
class Plantilla:
    def __init__(self):
        self.empleados = [
            Empleado("jaime", 10000, "peon"),
            Empleado("ramon", 20000, "torre"),
            Empleado("gian", 25000, "caballo"),
            Empleado("carlos", 40000, "alfil"),
            Empleado("maximo cristobal valdespino", 1200000, "Rey")
        ]

    #función para mostrar los empleados
    def mostrar_empleados(self):
            print("La plantilla:")
            for empleado in self.empleados:
                print(empleado)

#menu simple
def menu_empleados():
    plantilla = Plantilla()

    while True:
        print("\n1. Mostrar empleados")
        print("2. Salir")

        print("Ingresar número entre el 1 y el 2 para operar el menu")
        nav_menu = input()

        if nav_menu == "1":
            plantilla.mostrar_empleados()

        elif nav_menu == "2":
            break

        else:
            print("ingresar numero entre el 1 y el 2")

#para que corra el programa
if __name__ == "__main__":
    menu_empleados()
