#509
#Crea una clase Estudiante con nombre, edad y promedio. Permite ingresar estudiantes y ordenarlos por nota.


#se crea la clase
class Estudiante:
    #se definen los atributos de la clase
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    #se define lo que se va a mostrar en el string
    def __str__(self):
        return f"Estudiante {self.nombre}, Edad {self.edad}, Promedio {self.promedio}"

#se crea la clase lista para guardar los estudiantes
class ListaEstudiante:
    def __init__(self):
        #aca se crea la lista
        self.estudiantes = []

    #se ingresan los estudiantes
    def alta_estudiante(self, estudiante):
        #aca se agrega a la lista
        self.estudiantes.append(estudiante)
        #se avisa que el estudiante fue ingresado con exito
        print(f"El estudiante '{estudiante.nombre}' fue ingresado correctamente ")

    #función para mostrar los estudiantes
    def mostrar_estudiantes(self):
        #se verifica que existan estudiantes
        if not self.estudiantes:
            print("No hay estudiantes ingresados")
        else:
            #si hay estudiantes se muestran
            print("Lista de estudiantes:")
            #se recorre la lista de estudiantes en la clase
            for estudiante in self.estudiantes:
                #se muestran los estudiantes
                print(estudiante)

    #se ordenan los estudiantes
    def ordenar_por_nota(self):
        #se usa el .sort para ordenarlos y el reverse=True para mostrarlos de mayor a menor
        self.estudiantes.sort(key=lambda estudiante: estudiante.promedio, reverse=True)
        print("Estudiantes ordenados por nota:")

#menu para manejar el programa
def menu_estudiantes():
    #se llama a la clase lista
    estudiantes = ListaEstudiante()

    #menu simple
    while True:
        print("\n1. Alta Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Ordenar Estudiantes")
        print("4. Salir")

        #se le pide al usuario inputs para usar el programa
        print("Ingresar número del 1 al 4 para operar el menu")
        nav_menu = input()

        if nav_menu == "1":
            print("Ingresar los datos del Estudiante. Estos son Nombre, Edad y Nota")
            nombre = input()
            #se pasan los input a la clase de datos correctos
            edad = int(input())
            nota = float(input())
            #aca se llama a la clase y se le pasan los parámetros ingresados
            estudiante = Estudiante(nombre, edad, nota)
            #aca se llama a la función para agregar, con los parámetros ingresados
            estudiantes.alta_estudiante(estudiante)

        elif nav_menu == "2":
            #se llama a la función mostrar
            estudiantes.mostrar_estudiantes()

        elif nav_menu == "3":
            #se llama a la función de ordenar primero y luego a la de mostrar
            #esto porque el mostrar, en este caso, es estático
            estudiantes.ordenar_por_nota()
            estudiantes.mostrar_estudiantes()

        #para salir del programa
        elif nav_menu == "4":
            print("saliendo")
            break

        #por si se escribe otra cosa
        else:
            print("Ingresar número del 1 al 4")

#para correr el programa
if __name__ == "__main__":
    menu_estudiantes()
