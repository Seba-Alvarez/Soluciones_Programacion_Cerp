# 515
# Crea una clase Vehículo y cuenta cuántos vehículos de un modelo específico hay.


#se crea la clase
class Vehiculo:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio

    #se elige como se va a mostrar
    def __str__(self):
        return f"Modelo {self.modelo}, Precio {self.precio}"

#se crea la lista con valores predefinidos
class Catalogo:
    def __init__(self):
        self.productos = [
            Vehiculo("volkswagen polo", 10000),
            Vehiculo("volkswagen polo", 20000),
            Vehiculo("volkswagen polo", 15000),
            Vehiculo("volkswagen polo", 12500),
            Vehiculo("toyota corolla", 20000),
            Vehiculo("toyota corolla", 25000),
            Vehiculo("toyota corolla", 30000),
            Vehiculo("toyota corolla", 35000),
            Vehiculo("kawasaki ninja", 40000),
            Vehiculo("kawasaki ninja", 45000),
        ]
    #función para contar las veces que se repite algún modelo
    def contar_veh(self, modelo):
        #variable para contar en el for
        cont = 0
        for producto in self.productos:
            #para que se pueda escribir en mayúsculas o minúsculas
            if producto.modelo.lower() == modelo.lower():
                cont += 1
        #retorna el número final del contador
        return cont

#menu simple
def menu_productos():
    catalogo = Catalogo()

    while True:
        print("\n1. Mostrar cuantas veces se repite un vehículo")
        print("2. Salir")

        print("Ingresar 1 o 2 para operar el menu")
        nav_menu = input()

        #aca se le pasa el input al buscador
        if nav_menu == "1":
            print("Ingresar el nombre del vehiculo")
            nombre = input()
            #aca se llama a la función de la clase con el input por parámetro
            con = catalogo.contar_veh(nombre)
            print(f"El modelo:{nombre} aparece {con} veces")

        elif nav_menu == "2":
            print("saliendo")
            break

        else:
            print("Ingresar número del 1 al 2")

#para que corra el programa
if __name__ == "__main__":
    menu_productos()
