# 618
# Crea una clase llamada Empleado que contenga los atributos nombre, salario y edad.
# Luego, crea una función que verifique si el empleado es mayor de edad y si su salario supera cierto valor.


#se crea la clase
class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    #se define como se van a mostrar los datos
    def __str__(self):
        return f"Nombre {self.nombre}, Edad {self.edad}, Salario {self.salario}"
#se crea la lista
class ListaEmp:
    def __init__(self):
        self.empleados = []

    #alta de empleados, la cual te advierte si se ingresa un empleado menor de edad y si su sueldo supera los 100k
    def alta_emp(self, empleado):
        self.empleados.append(empleado)
        print(f"El producto '{empleado.nombre}' fue ingresado correctamente ")
        if empleado.edad < 18:
            print("Advertencia: El empleado es menor de edad")
        if empleado.salario > 100000:
            print("Advertencia: El sueldo del empleado supera los 100k")

    #función para mostrar empleados
    def mostrar_emp(self):
        #verificar si hay empleados
        if not self.empleados:
            print("No hay empleados guardados")
        else:
            #en caso de haber empleados se recorre la lista y se muestran todos los empleados
            print("Lista de empleados:")
            for empleado in self.empleados:
                print(empleado)
#menu simple
def menu_empleados():
    emp_lis = ListaEmp()

    while True:
        print("\n1. Alta Empleado")
        print("2. Mostrar Empleados")
        print("3. Salir")

        #se define los inputs en una variable para usar el menu
        print("Ingresar número del 1 al 3 para operar el menu")
        nav_menu = input()

        #se piden los datos del empleado por parametro y se los pasa a la función alta
        if nav_menu == "1":
            print("Ingresar los datos del empleado. Estos son Nombre, Edad y Salario")
            nombre = input()
            edad = int(input())
            salario = int(input())
            empleado = Empleado(nombre, edad, salario)
            emp_lis.alta_emp(empleado)

        #se llama a la función que ingresa empleados
        elif nav_menu == "2":
            emp_lis.mostrar_emp()

        #para salir del menu
        elif nav_menu == "3":
            print("saliendo")
            break

        #por si se ingresa algo que no sea 1, 2 o 3
        else:
            print("Ingresar número del 1 al 3")

#para que corra el programa
if __name__ == "__main__":
    menu_empleados()