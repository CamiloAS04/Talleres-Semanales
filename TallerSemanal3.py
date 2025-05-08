# Inventario de productos (clave = nombre del producto, valor = (precio, cantidad))
inventario = {}

# Función para agregar un producto al inventario
def agregar_producto(inventario, nombre, precio, cantidad):
    nombre = nombre.lower()
    if nombre in inventario:
        print("El producto ya existe.")
        opcion = input("¿Deseas actualizar la cantidad? (s/n): ").strip().lower()
        while opcion not in ('s', 'n'):
            opcion = input("Por favor, responde con 's' o 'n': ").strip().lower()
        if opcion == 's':
            precio_actual, cantidad_actual = inventario[nombre]
            inventario[nombre] = (precio, cantidad_actual + cantidad)
            print(f"Cantidad del producto '{nombre}' actualizada a {cantidad_actual + cantidad}.")
        else:
            print("No se realizaron cambios.")
    else:
        inventario[nombre] = (precio, cantidad)
        print(f"Producto '{nombre}' agregado exitosamente.")

# Función para buscar un producto
def buscar_producto(inventario, nombre):
    nombre = nombre.lower()
    producto = inventario.get(nombre)
    if producto:
        print(f"Producto: {nombre} | Precio: ${producto[0]} | Cantidad: {producto[1]}")
    else:
        print("Producto no encontrado en el inventario.")

# Función para actualizar el precio de un producto
def actualizar_precio(inventario, nombre, nuevo_precio):
    nombre = nombre.lower()
    if nombre in inventario:
        _, cantidad = inventario[nombre]
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f"Precio del producto '{nombre}' actualizado a ${nuevo_precio}.")
    else:
        print("Producto no encontrado.")

# Función para eliminar un producto
def eliminar_producto(inventario, nombre):
    nombre = nombre.lower()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print("Producto no encontrado.")

# Función para calcular el valor total del inventario
def calcular_valor_total(inventario):
    total = sum(map(lambda item: item[0] * item[1], inventario.values()))
    print(f"Valor total del inventario: ${total:.2f}")

# Función para mostrar todos los productos
def mostrar_todos(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- LISTA DE PRODUCTOS ---")
        for nombre, (precio, cantidad) in inventario.items():
            print(f"- {nombre.capitalize()}: Precio = ${precio}, Cantidad = {cantidad}")

# Función para validar entrada de número
def solicitar_numero(mensaje, es_entero=False):
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if valor < 0:
                print("El número no puede ser negativo.")
                continue
            return int(valor) if es_entero else valor
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Menú interactivo
def menu():
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Ver todos los productos")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            while not nombre:
                nombre = input("Nombre del producto (no puede estar vacío): ").strip()
            precio = solicitar_numero("Precio del producto: ")
            cantidad = solicitar_numero("Cantidad disponible: ", es_entero=True)
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            nombre = input("Nombre del producto a consultar: ").strip()
            buscar_producto(inventario, nombre)

        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ").strip()
            nuevo_precio = solicitar_numero("Nuevo precio: ")
            actualizar_precio(inventario, nombre, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(inventario, nombre)

        elif opcion == "5":
            calcular_valor_total(inventario)

        elif opcion == "6":
            mostrar_todos(inventario)

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()

