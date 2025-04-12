#525
#Crea una clase Paciente y permite buscar por número de habitación.


#se crea la clase paciente
class Paciente:
    def __init__(self, nombre, apellido, nro_hab):
        self.nombre = nombre
        self.apellido = apellido
        self.nro_hab = nro_hab

    #se define como se va a mostrar
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Número de Habitación: {self.nro_hab}"

#se crea la lista con datos predefinidos
class LisPacientes:
    def __init__(self):
        self.pacientes = [
            Paciente("ramon", "ramirez", 201),
            Paciente("hernan", "hernandez", 100),
            Paciente("martin", "martinez", 149),
            Paciente("gonzalo", "gonzalez", 190)
        ]

    #se busca los pacientes por número de cuarto
    def bus_por_nro_hab(self, nro_hab):
        #se recorren los pacientes ingresados
        for pac_nom in self.pacientes:
            #si verifica que el paciente este ingresado y se retorna el valor
            if pac_nom.nro_hab == nro_hab:
                return str(pac_nom)
        else:
            return print("paciente no encontrado")

#menu simple
def menu_pac():
    men_pac = LisPacientes()

    while True:
        print("\n1. Buscar paciente por númer de cuarto")
        print("2. Salir")

        print("Ingresar 1 o 2 para operar el menu")
        nav_menu = input()

        if nav_menu == "1":
            print("Ingresar número del cuarto")
            #se pide un número de cuarto
            num_hab = int(input())
            #se llama a la variable y se le pasa el número de cuarto por parametro
            hab_hos = men_pac.bus_por_nro_hab(num_hab)
            #se muestra por pantalla
            print(hab_hos)

        elif nav_menu == "2":
            print("saliendo")
            break

        else:
            print("Ingresar número del 1 al 7")

if __name__ == "__main__":
    menu_pac()
