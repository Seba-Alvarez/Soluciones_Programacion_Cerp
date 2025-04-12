# 616
# Crea una clase llamada Rectángulo que contenga los atributos ancho y alto.
# Luego, crea una función que calcule el área de un rectángulo.


#se crea la clase
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    #se define como se va a mostrar los datos
    def __str__(self):
        return f"El área del rectángulo de ancho {self.ancho} y de alto {self.alto}, es:"

    #se calcula el área
    def area(self):
        return self.ancho * self.alto

#se crea una lista para guardar rectángulos
class Rectangulorium:
    def __init__(self):
        self.rectangulos = []

    #para ingresar rectángulos
    def alta_rectangulos(self, rectangulo):
        self.rectangulos.append(rectangulo)

    #función para mostrar los rectangulos y también se llama a la función para calcular el área
    def mostrar_rectangulos(self):
        print("Lista de rectángulos:")
        for rectangulo in self.rectangulos:
            print(f"{rectangulo} {rectangulo.area()}")


#menu simpple
def menu_rectangulos():
    rec_lis = Rectangulorium()

    while True:
        print("\n1. Alta rectángulos")
        print("2. Mostrar rectángulos")
        print("3. Salir")

        print("Ingresar número del 1 al 3 para operar el menu")
        nav_menu = input()

        #se piden los datos del rectángulo por consola
        if nav_menu == "1":
            print("Ingresar los datos del rectángulo")
            alto = float(input())
            ancho = float(input())
            rectangulo = Rectangulo(ancho, alto)
            rec_lis.alta_rectangulos(rectangulo)

        #llama a la función para mostrar rectángulos
        elif nav_menu == "2":
            rec_lis.mostrar_rectangulos()

        #para salir del menu
        elif nav_menu == "3":
            print("saliendo")
            break

        #por si se ingresa algo que no sea un número del 1 al 3
        else:
            print("Ingresar número del 1 al 3")

#para correr el programa
if __name__ == "__main__":
    menu_rectangulos()
