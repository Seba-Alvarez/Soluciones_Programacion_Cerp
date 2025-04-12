#514
#Crea una clase Alumno con materias y notas. Calcula el promedio de un alumno específico.


#se crea la clase alumno
class Alumno:
    #materia_dic es un diccionario
    def __init__(self, nombre, materia_dic=None):
        if materia_dic is None:
            #aca se crea el diccionario
            materia_dic = {}
        self.nombre = nombre
        #aca es para poder instanciar el atributo de la clase
        self.materia_dic = materia_dic

    def __str__(self):
        return f"Alumno {self.nombre} Materias {self.materia_dic}"

    #esto me lo robé de gpt
    def calcular_promedio(self):
        #se definen como 0 para poder hacer el promedio
        notas=0
        cant_notas = 0
        #calif es calificaciones
        #se recorren las notas ingresadas
        for calif in self.materia_dic.values():
            #aca se hace el promedio
            #se suman las calificaciones
            notas += sum(calif)
            #se dividen la cantidad de calificaciones len(), por la suma de las notas
            cant_notas += len(calif)
        return notas / cant_notas if cant_notas > 0 else 0

#se crea la lista de alumnos
class ListaAlumnos:
    def __init__(self):
        #en este caso los ingrese yo, para no tener que hacer el alta
        self.alumnos = [
            Alumno("Ramiro Ramirez", materia_dic={
                "matemáticas": [7],
                "física": [6],
                "historia": [8],
                "geografía": [8],
                "gimnasia": [6]
            } ),
            Alumno("Hernán Hernandez", materia_dic={
                "matemáticas": [10],
                "física": [10],
                "historia": [9],
                "geografía": [9],
                "gimnasia": [8]
            }),
            Alumno("Martín Martinez", materia_dic={
                "matemáticas": [4],
                "física": [3],
                "historia": [5],
                "geografía": [5],
                "gimnasia": [10]
            }),
            Alumno("Gonzalo Gonzalez", materia_dic={
                "matemáticas": [2],
                "física": [3],
                "historia": [3],
                "geografía": [2],
                "gimnasia": [1]
            }),
            Alumno("Esteban Estévez", materia_dic={
                "matemáticas": [10],
                "física": [10],
                "historia": [10],
                "geografía": [9],
                "gimnasia": [9]
            })]

    #aca se hace una función para mostrar
    def buscar_alumno_promedio(self, nombre):
        for alumno in self.alumnos:
            #si el nombre del alumno es igual al ingresado por consola
            if alumno.nombre.lower() == nombre.lower():
                #aca se llama a la función
                promedio = alumno.calcular_promedio()
                #se imprime por pantalla
                print(f"Alumno {alumno.nombre}, Promedio {promedio:.2f}")


#un menu simple
def menu_alumno():
    #para llamar a la lista de alumnos
    men_al = ListaAlumnos()

    #las dos opciones
    while True:
        print("\n1. Buscar alumno")
        print("2. Salir")

        print("Ingresar 1 o 2 para operar el menu")
        nav_menu = input()

        if nav_menu == "1":
            print("Ingresar el nombre del alumno")
            #se ingresa el nombre a buscar
            nombre = input()
            #se llama a la función que tiene el promedio y el mostrar en la misma
            men_al.buscar_alumno_promedio(nombre)

        elif nav_menu == "2":
            print("saliendo")
        break

#para entrar al menu
if __name__ == "__main__":
    #se muestra el menu
    menu_alumno()