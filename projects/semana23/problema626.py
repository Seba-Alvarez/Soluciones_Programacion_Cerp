# 626
# Crea una clase llamada Alumno que contenga el nombre, edad y promedio de un alumno.
# Crea un programa que permita ingresar la información de varios alumnos y los ordene con la función sorted() o el metodo sort().


#se crea la clase
class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    #asi se van a mostrar los datos
    def __str__(self):
        return f"Estudiante {self.nombre}, Edad {self.edad}, Promedio {self.promedio}"

#se crea la lista de estudiante
class LisEstudiantes:
    def __init__(self):
        self.estudiantes = []

    #se ingresan los datos de los estudiantes
    def alta_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"El estudiante '{estudiante.nombre}' fue ingresado correctamente ")

    #se muestran los estudiantes
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            print("No hay estudiantes guardados")
        else:
            print("El catálogo de estudiantes:")
            for estudiante in self.estudiantes:
                print(estudiante)

    #se ordenan los estudiantes por promedio
    def ordenar_por_promedio(self):
        self.estudiantes.sort(key=lambda estudiante: estudiante.promedio, reverse=True)
        print("Estudiantes ordenados por promedio:")

#menu simple
def menu_estudiantes():
    lista_estudiantes = LisEstudiantes()

    while True:
        print("\n1. Alta Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Ordenar Estudiantes por Promedio")
        print("4. Salir")

        print("Ingresar número del 1 al 4 para operar el menú")
        nav_menu = input()

        #se piden los datos para ingresarle a la función alta
        if nav_menu == "1":
            print("Ingresar los datos del estudiante. Estos son Nombre, Edad y Promedio")
            nombre = input("nombre: ")
            edad = int(input("edad: "))
            promedio = float(input("promedio: "))
            estudiante = Estudiante(nombre, edad, promedio)
            lista_estudiantes.alta_estudiante(estudiante)

        #se llama a la función mostrar
        elif nav_menu == "2":
            lista_estudiantes.mostrar_estudiantes()

        #se llama a la función ordenar primero y mostrar después
        elif nav_menu == "3":
            lista_estudiantes.ordenar_por_promedio()
            lista_estudiantes.mostrar_estudiantes()

        #para salir
        elif nav_menu == "4":
            print("Saliendo")
            break

        #por si se ingresa algo mas que un número del 1 al 4
        else:
            print("Ingresar número del 1 al 4")

#para correr el programa
if __name__ == "__main__":
    menu_estudiantes()