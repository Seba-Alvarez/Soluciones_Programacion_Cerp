#523
#Crea una clase Estudiante y permite buscar por matrícula y mostrar sus notas.


#se crea la clase
class Estudiante:
    #se definen los atributos de la clase
    def __init__(self, matricula, nombre, nota):
        self.matricula = matricula
        self.nombre = nombre
        self.nota = nota

    #se define lo que se va a mostrar en el string
    def __str__(self):
        return f"Matricula: {self.matricula}, Nombre: {self.nombre}, Nota: {self.nota}"

#se crea la clase lista para guardar los estudiantes
class ListaEstudiante:
    def __init__(self):
        #aca se crea la lista
        #datos de estudiantes predefinidos
        self.estudiantes = [
            Estudiante("ab12", "Ramiro Ramirez", 10.0),
            Estudiante("ba12", "Hernán Hernandez", 1.0),
            Estudiante("aa12", "Martín Martinez", 8.0),
            Estudiante("bb12", "Gonzalo Gonzalez", 4.0),
            Estudiante("ac12", "Esteban Estévez", 7.0)
        ]


    def buscar_estudiantes(self, matricula):
        #se recorren los estudiantes
        for estudiante in self.estudiantes:
            #si se encuentra el nombre del estudiante
            #el .lower es para que sea en minúscula, esto es para controlar excepciones
            if estudiante.matricula.lower() == matricula.lower():
                #se muestra el producto
                print(f"Estudiante fue encontrado con éxito : {estudiante}")

def menu_estudiantes():
    estudiante = ListaEstudiante()

    #aca se definen las entradas del menu.
    while True:
        #\n1 es para generar una línea antes de mostrar el contenido del print
        print("\n1. Buscar Estudiante")
        print("2. Salir")

        print("Ingresar número 1 o 2 para operar el menu")
        nav_menu = input()


        if nav_menu == "1":
            print("Ingresar la matricula del alumno")
            #se pide el nombre para buscar
            matricula = input()
            #se llama a la función con el parametro ingresado
            estudiante.buscar_estudiantes(matricula)

        elif nav_menu == "2":
            #se sale del programa
            print("saliendo")
            break

        else:
            print("Ingresar número 1 o 2")

#esta función define el punto de entrada al programa
if __name__ == "__main__":
    #se muestra el menu
    menu_estudiantes()