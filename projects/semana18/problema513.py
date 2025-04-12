#513
#Crea una clase Contacto y busca por nombre en una lista de contactos.


#se crea la clase
class Contacto:
    def __init__(self, nombre, tel):
        self.nombre = nombre
        self.tel = tel

    #se define como se va a mostrar en el string
    def __str__(self):
        return f" Nombre {self.nombre} Teléfono {self.tel}"

#se crea la lista
class ListaContacto:
    def __init__(self):
        self.contactos = [
            #lista prefinida por mi
            Contacto("juan", "096667307"),
            Contacto("ramón", "096937584"),
            Contacto("esteban", "096692837"),
            Contacto("ramiro", "091740973"),
            Contacto("martin", "094951667")
        ]

    #funcion para buscar
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            #cuando se ingresa un nombre
            if contacto.nombre.lower() == nombre.lower():
                #se devuelve el teléfono de la persona
                print(f"Contacto fue encontrado con éxito : {contacto.tel}")

#menu simple
def menu_contacto():
    contacto = ListaContacto()

    while True:
        print("\n1. Buscar Contacto")
        print("2. Salir")

        print("Ingresar número 1 o 2 para operar el menu")
        nav_menu = input()

        if nav_menu == "1":
            print("Ingresar nombre")
            #se pide el nombre por pantalla
            nom_con = input()
            #se llama a la función
            contacto.buscar_contacto(nom_con)

        elif nav_menu == "2":
            print("saliendo")
            break

        else:
            print("Ingresar número 1 o 2")

if __name__ == "__main__":
    menu_contacto()