#521
#Crea una clase Producto y permite agregar, modificar y mostrar productos.


#se crea la clase y se elige un nombre
class Producto:
    #se define los parámetros de la clase
    #__init__ es una función nativa de python que permite asignar valores a las propiedades de los objetos
    #self es un parametro que hace referencia a la instancia actual de una clase
    #se suele usar self, es una convención, se puede poner el nombre que se quiera
    #independientemente del nombre, tiene que ser el primer parametro en las funciones de la clase
    def __init__(self, nombre, precio, cantidad):
        #aca se están asignando los valores que se pasan como argumentos a los parámetros a los atributos de la instancia miproducto
        self.nombre = nombre
        #miproducto es instancia de la clase producto
        #miproducto.precio es el atributo del objeto de la clase
        #precio es el parametro que se le va a pasar a la clase cuando sea instanciada
        self.precio = precio
        self.cantidad = cantidad

    #aca se está usando la función __str__ que sirve para controlar lo que se retorna cuando los objetos de la clase
    #se muestran como string
    def __str__(self):
        #este f-string muestra los valores de las instancias de la clase producto
        return f"Producto {self.nombre}, Precio {self.precio}, Cantidad {self.cantidad}"

class Catalogo:
    def __init__(self):
        #aca se está creando el catálogo al inicio esta vacia la lista
        #cuando se ingresen productos, los datos van a estar en esta lista
        self.productos = []

    #recordar que Producto, producto y productos son cosas diferentes
    #Producto, es la clase
    #producto, es el parametro que se le pasa a la función
    #productos, es una lista de instancias de la clase Producto (que esta adentro de la clase catálogo)
    #alta o create es ingresar, es también una convención
    def alta_producto(self, producto):
        self.productos.append(producto)
        print(f"El producto '{producto.nombre}' fue ingresado correctamente ")


    #modificar o update, es (sorpresa) otra convención
    #al poner new_parametro=None permite que el cambio sea opcional, si no se modifica queda igual con los otros cambios hechos
    #se pide el nombre para poder buscar
    def modificar_producto(self, nombre, new_nombre=None, new_precio=None, new_cantidad=None):
        #se recorren los productos en la lista del catalogo
        for producto in self.productos:
            #si se encuentra el nombre de un producto ingresado
            if producto.nombre == nombre:
                #si se decide cambiar el nombre del producto
                if new_nombre:
                    #se cambia el nombre del producto con el ingresado
                    producto.nombre = new_nombre
                #si se ingresa un precio nuevo, aca se cambia el precio viejo al ingresado
                if new_precio is not None:
                    producto.precio = new_precio
                if new_cantidad is not None:
                    producto.cantidad = new_cantidad

                print(f"El producto {nombre} fue modificado correctamente")
                return

            # en caso de no encontrarse el nombre
            print(f"El producto '{nombre}' no se encontró")
            return

    def mostrar_productos(self):
        #se verifica que existan productos guardados
        if not self.productos:
            print("No hay productos guardados")
        else:
            print("El catalogo:")
            #este producto es una variable para que el for recorra la lista de productos y para poder mostrar los productos de la lista
            for producto in self.productos:
                #se muestran los productos
                print(producto)

    # un menu para mostrar los contenidos de forma mas amigable a la vista
def menu_productos():
    catalogo = Catalogo()

    # aca se definen las entradas del menu.
    while True:
        # \n1 es para generar una línea antes de mostrar el contenido del print
        print("\n1. Alta Producto")
        print("2. Modificar Producto")
        print("3. Mostrar Productos")
        print("4. Salir")

        # se pide al usuario que ponga un número del 1 al 7 para que acceda a los contenidos del menu.
        print("Ingresar número del 1 al 7 para operar el menu")
        nav_menu = input()

        # aca es donde se determina como entrar al menu y lo que hace cada parte
        if nav_menu == "1":
            # esta es el alta, donde se pide al usuario ingresar un nuevo producto
            print("Ingresar los datos del producto. Estos son Nombre, Precio y Cantidad")
            nombre = input()
            # se convierten los datos ingresados en números
            precio = float(input())
            cantidad = int(input())
            # aca se le esta diciendo que los parámetros ingresados van a los parámetros de la clase
            producto = Producto(nombre, precio, cantidad)
            # aca se llama a la función con los parámetros ingresados
            catalogo.alta_producto(producto)

        elif nav_menu == "2":
            print("Ingresar el nombre del producto que se desea modificar")
            nombre = input()
            print("Ingresar los datos que se desea modificar")
            nuevo_nombre = input()
            nuevo_precio = input()
            nueva_cantidad = input()

            #esto permite que se dejen campos en blanco y no se cambien los valores
            #si no se ingresa un nuevo valor, no se cambia
            nuevo_nombre = nuevo_nombre if nuevo_nombre else None
            #lo mismo que en la linea de arriba, pero también se cambian los dátos ingresados a números
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

            #se llama a la función con los parametros ingresados
            catalogo.modificar_producto( nombre, nuevo_nombre, nuevo_precio, nueva_cantidad)

        elif nav_menu == "3":
            #simplemente se llama a la función
            catalogo.mostrar_productos()

        elif nav_menu == "4":
            #se sale del programa
            print("saliendo")
            break

        else:
            print("Ingresar número del 1 al 4")

#esta función define el punto de entrada al programa
if __name__ == "__main__":
    #se muestra el menu
    menu_productos()