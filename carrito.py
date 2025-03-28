class Carrito:
    def __init__(self):
        self.productos = {}
        self.cantidad = 0
        self.total = 0
        self.cap_max = 10

    def agregar_producto(self, nombre, precio, cantidad=1):
        if self.cantidad + cantidad > self.cap_max:
            print(f"No se pueden agregar {cantidad} unidades. Carrito lleno :( )")
            return                                                                               #programa se corta, como si escribieramos un else:                         
        if nombre in self.productos:
            self.productos[nombre]['cantidad'] += cantidad
        else:
            self.productos[nombre] = {'precio': precio, 'cantidad': cantidad}

        self.cantidad += cantidad
        self.total += precio * cantidad

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]

    def mostrar(self):
        print("\n==== CARRITO ====")
        print(self.productos)
        print(f"Total de productos: {self.cantidad} - Total a pagar: ${self.total}")


carrito = Carrito()
carrito.agregar_producto("Leche", 35)
carrito.mostrar()
carrito.agregar_producto ("Leche", 35, 40)
carrito.mostrar()


#arreglar eliminar producto
#una funcion extra, calculo de iva, descuentos