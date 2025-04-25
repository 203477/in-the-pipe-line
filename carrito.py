class Carrito:
    def __init__(self):
        self.productos = {}
        self.cantidad = 0
        self.total = 0
        self.cap_max = 10

    def agregar_producto(self, nombre, precio, cantidad=1):
        if self.cantidad + cantidad > self.cap_max:
            print(f"No se pueden agregar {cantidad} unidades. Carrito lleno :( )")
            return
        if nombre in self.productos:
            self.productos[nombre]['cantidad'] += cantidad
        else:
            self.productos[nombre] = {'precio': precio, 'cantidad': cantidad}

        self.cantidad += cantidad
        self.total += precio * cantidad

    def modificar_producto(self, nombre, nueva_cantidad):          
        if nombre in self.productos:
            producto = self.productos[nombre]
            diferencia = nueva_cantidad - producto['cantidad']
            if self.cantidad + diferencia > self.cap_max:
                print(f"No se pueden agregar {diferencia} unidades. Carrito lleno :( )")
                return
            self.cantidad += diferencia
            self.total += diferencia * producto['precio']
            if nueva_cantidad == 0:
                del self.productos[nombre]
            else:
                producto['cantidad'] = nueva_cantidad
        else:
            print(f"El producto '{nombre}' no está en el carrito.")

    
    def mostrar(self):
        print("\n==== CARRITO ====")
        print(self.productos)
        print(f"Total de productos: {self.cantidad} - Total a pagar: ${self.total}")

    def pagar(self):
        print("\nOpciones de pago:")
        print("1. Tarjeta (3% de comisión)")
        print("2. Efectivo (sin comisión)")
        metodo_pago = input("Seleccione el método de pago: ")

        if metodo_pago == "1":
            comision = self.total * 0.03
            self.total += comision
            print(f"Se agregó una comisión del 3% (${comision:.2f}) por pagar con tarjeta.")
        elif metodo_pago == "2":
            print("Pago en efectivo seleccionado. No se aplica comisión.")
        else:
            print("Método de pago no válido. Intente de nuevo.")
            return self.pagar()                                                        # Volver a preguntar por el método de pago

        print(f"\nTotal a pagar: ${self.total:.2f}")
        print("Gracias por su compra!")
        self.productos = {}
        self.cantidad = 0
        self.total = 0


 #   def aplicar_descuento(self, porcentaje):
  #      descuento = self.total * (porcentaje / 100)
   #     self.total -= descuento
    #    print(f"Se aplicó un descuento del {porcentaje}%. Total a pagar: ${self.total:.2f}")


1
carrito = Carrito()

productos_disponibles = {
    "Leche": 35,
    "Pan": 20,
    "Huevo": 50,
    "Verduras": 40,
    "Fruta": 30,
    "Arroz": 25,
    "Azúcar": 15
}

while True:
    print("\nProductos disponibles:")
    for producto, precio in productos_disponibles.items():
        print(f"{producto} - ${precio}")

    print("\nOpciones:")
    print("1. Agregar producto al carrito")
    print("2. Modificar cantidad de un producto")
    print("3. Mostrar carrito")
    print("4. Pagar y salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in productos_disponibles:
            cantidad = int(input("Ingrese la cantidad: "))
            carrito.agregar_producto(nombre, productos_disponibles[nombre], cantidad)
        else:
            print("Producto no disponible.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto a modificar: ")
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        carrito.modificar_producto(nombre, nueva_cantidad)
    elif opcion == "3":
        carrito.mostrar()
    elif opcion == "4":
        carrito.pagar()
        break
    else:
        print("Opción no válida. Intente de nuevo.")