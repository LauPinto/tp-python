productos = []


def agregar_producto():
    print("\n--- AGREGAR PRODUCTO ---")

    nombre = input("Ingrese el nombre del producto: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingrese el nombre del producto: ").strip()

    categoria = input("Ingrese la categoría del producto: ").strip()

    while categoria == "":
        print("La categoría no puede estar vacía.")
        categoria = input("Ingrese la categoría del producto: ").strip()

    precio = input("Ingrese el precio del producto (sin centavos): ").strip()

    while not precio.isdigit():
        print("Debe ingresar un número válido.")
        precio = input("Ingrese el precio del producto (sin centavos): ").strip()

    precio = int(precio)

    producto = [nombre, categoria, precio]
    productos.append(producto)

    print("Producto agregado correctamente.")


def mostrar_productos():
    print("\n--- LISTA DE PRODUCTOS ---")

    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")



def buscar_producto():
    print("\n--- BUSCAR PRODUCTO ---")

    busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()

    while busqueda == "":
        print("Debe ingresar un nombre.")
        busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()

    encontrados = False

    for i, producto in enumerate(productos, start=1):
        if busqueda in producto[0].lower():
            print(f"{i}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
            encontrados = True

    if not encontrados:
        print("No se encontraron productos.")


def eliminar_producto():
    print("\n--- ELIMINAR PRODUCTO ---")

    if len(productos) == 0:
        print("No hay productos para eliminar.")
        return

    mostrar_productos()

    posicion = input("Ingrese el número del producto a eliminar: ").strip()

    while not posicion.isdigit():
        print("Debe ingresar un número válido.")
        posicion = input("Ingrese el número del producto a eliminar: ").strip()

    posicion = int(posicion)

    if posicion >= 1 and posicion <= len(productos):
        producto_eliminado = productos.pop(posicion - 1)
        print(f"Producto '{producto_eliminado[0]}' eliminado correctamente.")
    else:
        print("Número fuera de rango.")


opcion = 0

while opcion != 5:
    print("\n===============================")
    print("Sistema de Gestión de Productos")
    print("===============================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    while not opcion.isdigit():
        print("Debe ingresar un número válido.")
        opcion = input("Seleccione una opción: ").strip()

    opcion = int(opcion)

    if opcion == 1:
        agregar_producto()

    elif opcion == 2:
        mostrar_productos()

    elif opcion == 3:
        buscar_producto()

    elif opcion == 4:
        eliminar_producto()

    elif opcion == 5:
        print("Saliendo del sistema...")

    else:
        print("Opción inválida.")