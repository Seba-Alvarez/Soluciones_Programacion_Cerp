#511
#Crea una clase Libro con título, autor y año. Ordena libros por título.


class Libro:
    def __init__(self, titulo, autor, fec_publi):
        self.titulo = titulo
        self.autor = autor
        self.fec_publi = fec_publi

    #se define como se van a mostrar los libros
    #los \n son para que haga que hago salto de línea
    def __str__(self):
        return f" \n-Titulo: {self.titulo} \n-Autor: {self.autor} \n-Fecha de publicación: {self.fec_publi}"


class ListaLibro:
    def __init__(self):
        #lista de libros ingresada por mi
        self.lista_de_libros = [
            Libro("como cocinar tortas de jamon","mario baracus jr","20/10/2020"),
            Libro("rellenando paredes", "ramon valdez", "10/10/1910"),
            Libro("como imprimir en word", "rosita earnst", "1/1/2005"),
            Libro("origen de las especies de marte", "elaine muskeira", "20/2/2025"),
            Libro("lo que tus heces dicen de ti", "tom stuart", "20/10/2")
        ]

    #se ordenan y se muestran los libros
    def ordenar_libro(self):
        #aca se queja porque se usa la variable libro tanto en la clase como en la función
        #pero como es un programa chico no pasa nada
        self.lista_de_libros.sort(key=lambda libro: libro.titulo)
        print("Libros ordenados por titulo")
        #se recorren y se imprimen los libros
        for libro in self.lista_de_libros:
            print(libro)
#menu simple
def menu_libros():
    catalogo = ListaLibro()

    while True:
        print("\n1. Mostrar libros ordenados")
        print("2. Salir")

        print("Ingresar número entre el 1 y el 2 para operar el menu")
        nav_menu = input()

        if nav_menu == "1":
            catalogo.ordenar_libro()

        elif nav_menu == "2":
            break

        else:
            print("ingresar numero entre el 1 y el 2")

#para que corra el programa
if __name__ == "__main__":
    menu_libros()