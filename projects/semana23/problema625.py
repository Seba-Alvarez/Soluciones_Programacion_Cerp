# 625
# Escribir una función que reciba una clase que contenga información sobre un producto en una tienda
# incluyendo su nombre, precio y cantidad en stock.
# La función debe aumentar la cantidad en stock del producto en una cierta cantidad determinada por el usuario.


#creo la clase
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    #asi se va a mostrar los daots
    def __str__(self):
        return f"Producto {self.nombre}, Precio {self.precio}, Cantidad {self.cantidad}"

#lista para guardar los productos
class Catalogo:
    def __init__(self):
        self.productos = []

    #ingresar productos
    def alta_producto(self, producto):
        self.productos.append(producto)
        print(f"El producto '{producto.nombre}' fue ingresado correctamente ")

    #muestra los productos
    def mostrar_productos(self):
        #si no hay productos avisa
        if not self.productos:
            print("No hay productos guardados")
        else:
            #muestra los productos con un búcle
            print("El catalogo:")
            for producto in self.productos:
                print(producto)

    #para modificar el stock
    def modificar_producto(self, nombre, new_cantidad=None):
        for producto in self.productos:
            #se busca el producto por nombre
            if producto.nombre == nombre:
                #si se ingresa algo se cambia el nuevo stock
                if new_cantidad is not None:
                    producto.cantidad = new_cantidad

                print(f"El producto {nombre} fue modificado correctamente")
                return

        print(f"El producto '{nombre}' no se encontró")
        return

#menu simple
def menu_productos():
    catalogo = Catalogo()

    while True:
        print("\n1. Alta Producto")
        print("2. Mostrar Productos")
        print("3. Modificar Stock")
        print("4. Salir")

        #para controlar el menú
        print("Ingresar número del 1 al 4 para operar el menu")
        nav_menu = input()

        #pide los datos necesarios para ingresar un nuevo producto
        if nav_menu == "1":
            print("Ingresar los datos del producto. Estos son Nombre, Precio y Cantidad")
            nombre = input()
            precio = float(input())
            cantidad = int(input())
            producto = Producto(nombre, precio, cantidad)
            catalogo.alta_producto(producto)

        #llama a la función para mostrar productos
        elif nav_menu == "2":
            catalogo.mostrar_productos()

        #pide el nombre del producto a modificar y lo modifica
        elif nav_menu == "3":
            print("Ingresar el nombre del producto que se desea modificar")
            nombre = input()
            print("Ingresar el nuevo stock")
            nueva_cantidad = input()

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

            catalogo.modificar_producto( nombre, nueva_cantidad)

        #para salir del menu
        elif nav_menu == "4":
            print("saliendo")
            break

        #por si se ingresa algo que no sea 1,2,3 o 4
        else:
            print("Ingresar número del 1 al 4")

#para correr el programa
if __name__ == "__main__":
    menu_productos()