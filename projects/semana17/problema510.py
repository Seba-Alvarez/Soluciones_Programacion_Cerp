#510
#Crea una clase Empleado con nombre, salario y edad. Ordena empleados por salario.


#se crea la clase
class Empleado:
    def __init__(self, nombre, salario, edad):
        self.nombre = nombre
        self.salario = salario
        self.edad = edad

    #se define como se va a mostrar
    def __str__(self):
        return f"Nombre {self.nombre}, Sueldo {self.salario}, Edad {self.edad}"

#se crea la lista con datos predefinidos
class Plantilla:
    def __init__(self):
        self.empleados = [
            Empleado("ramon", 20000, 28),
            Empleado("gian", 25000, 25),
            Empleado("carlos", 40000, 31),
            Empleado("maximo cristobal valdespino", 1200000, 45)
        ]

    #funcion para ordenar los empleados
    def ordenar_por_salario(self):
        #en este caso quería que fuera de mayor a menor, por lo cual le puse el reverse
        self.empleados.sort(key=lambda empleado: empleado.salario, reverse=True)
        for empleados in self.empleados:
            print(empleados)

#menu simple
def menu_empleados():
    plantilla = Plantilla()

    while True:
        print("\n1. Mostrar libros ordenados")
        print("2. Salir")

        print("Ingresar número entre el 1 y el 2 para operar el menu")
        nav_menu = input()

        if nav_menu == "1":
            plantilla.ordenar_por_salario()

        elif nav_menu == "2":
            break

        else:
            print("ingresar numero entre el 1 y el 2")

#para que corra el programa
if __name__ == "__main__":
    menu_empleados()