inventario = []  # lista vacía llamada inventario que almacenará todos nuestros productos.

# Función principal 
def main_menu():
    print("\nSistema de inventario")
    print("1. Agregar producto")
    print("2. Ver todos los productos")
    print("3. Buscar producto")
    print("4. Modificar producto")
    print("5. Salir")
    
    choice = input("Seleccione una opción (1-5): ")                    #Esta función muestra un menú con 5 opciones y pide al usuario que elija una.
    return choice                                                      #Devuelve la opción seleccionada como texto (por ejemplo, "1", "2", etc.).

# Función para agregar productos
def agregar():
    print("\nAgregar producto nuevo")
    name = input("Ingresa el nombre del producto: ")
    
    try: 
        price = float(input("Ingresa el precio: "))                    # "Intenta convertir lo que diga en número"
        quantity = int(input("Ingresa la cantidad: "))
        
        if price < 0 or quantity < 0:                                  #el precio o cantidad no puede ser un valor negativo
            print("Error: No se permiten valores negativos.")          #al usuario se le indica su error
            return
            
    except ValueError:                                                 #si es un error de valor, print un mensaje para saber que hizo mal el usuario
        print("Error: Debes ingresar números válidos.")                
        return                                                         #y segue con el codigo, no se queda trabado
    
    # Crear diccionario para el nuevo producto
    nuevo_producto = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventario.append(nuevo_producto)
    print(f"\n{name} ha sido agregado al inventario!")

# Función para ver todos los productos
def ver_productos():
    print("\nInventario actual")
    print("-" * 30)
    
    if not inventario:
        print("No hay productos en el inventario.")
    else:
        for index, item in enumerate(inventario, 1):
            print(f"{index}. {item['name']}")
            print(f"   Precio: ${item['price']:.2f}")
            print(f"   Cantidad: {item['quantity']}")
            print("-" * 30)

# Función para buscar productos
def busqueda():
    print("\nBuscar producto")
    busqueda = input("Ingresa el producto a buscar: ").lower()
    
    encontrados = []
    for item in inventario:
        if busqueda in item["name"].lower():
            encontrados.append(item)
    
    if encontrados:
        print("\nProductos encontrados:")
        for i, item in enumerate(encontrados, 1):
            print(f"{i}. {item['name']}")
            print(f"   Precio: ${item['price']:.2f}")
            print(f"   Cantidad: {item['quantity']}")
            print("-" * 20)
    else:
        print("\nNo se encontraron productos en la búsqueda.")

# Función para modificar productos
def modificar():
    ver_productos()
    if not inventario:
        return
    
    try:
        item_num = int(input("\nIngresa el número del producto a modificar: ")) - 1
        if 0 <= item_num < len(inventario):
            item = inventario[item_num]
            print(f"\nModificando {item['name']}")
            print("1. Cambiar nombre")
            print("2. Cambiar precio")
            print("3. Cambiar cantidad")
            print("4. Cancelar")
            
            choice = input("\n¿Qué deseas modificar? (1-4): ")
            
            if choice == "1":
                new_name = input("Ingresa nuevo nombre: ")
                item["name"] = new_name
                print("\nNombre actualizado!")
            elif choice == "2":
                try:
                    new_price = float(input("Ingresa nuevo precio: "))
                    if new_price < 0:
                        print("Error: El precio no puede ser negativo.")
                        return
                    item["price"] = new_price
                    print("\nPrecio actualizado!")
                except ValueError:
                    print("Error: Debes ingresar un número válido.")
            elif choice == "3":
                try:
                    new_quantity = int(input("Ingresa nueva cantidad: "))
                    if new_quantity < 0:
                        print("Error: La cantidad no puede ser negativa.")
                        return
                    item["quantity"] = new_quantity
                    print("\nCantidad actualizada!")
                except ValueError:
                    print("Error: Debes ingresar un número entero válido.")
            elif choice == "4":
                print("\nModificación cancelada.")
            else:
                print("\nOpción inválida.")
        else:
            print("\nNúmero de producto inválido.")
    except ValueError:
        print("\nError: Debes ingresar un número válido.")

# Función principal
def main():
    # Datos de ejemplo
    productos_ejemplo = [
        {"name": "Leche", "price": 2.99, "quantity": 10},
        {"name": "Huevos", "price": 3.49, "quantity": 12},
        {"name": "Pan", "price": 1.99, "quantity": 5}
    ]
    inventario.extend(productos_ejemplo)
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            agregar()
        elif choice == "2":
            ver_productos()
        elif choice == "3":
            busqueda()
        elif choice == "4":
            modificar()
        elif choice == "5":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Por favor intenta nuevamente.")

if __name__ == "__main__":
    main()


