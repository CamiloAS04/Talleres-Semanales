# Sistema de cálculo de costo total de la compra

print("Bienvenido al sistema de compra")

# Lista para guardar los productos
productos = []

# Función para validar entradas numéricas
def solicitar_numero(mensaje, tipo=float, min_val=None, max_val=None):
    while True:
        try:
            valor = tipo(input(mensaje))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print(f"El valor debe estar entre {min_val} y {max_val}.")
                continue
            return valor
        except ValueError:
            print("Ingrese un número válido.")

# Bucle para ingresar productos
while True:
    # Paso 1: Entrada y validación de datos
    while True:
        producto = input("\nIngrese nombre del producto: ").strip()
        if producto:
            break
        print("El nombre del producto no puede estar vacío.")

    precio_unitario = solicitar_numero("Ingrese precio unitario del producto: $", float, min_val=0.01)
    cantidad_producto = solicitar_numero("Ingrese la cantidad de producto: ", int, min_val=1)
    descuento = solicitar_numero("Ingrese el descuento del producto (0-100): ", float, 0, 100)

    # Paso 2: Cálculo de costos
    costo_sin_descuento = precio_unitario * cantidad_producto
    monto_descuento = (descuento / 100) * costo_sin_descuento
    costo_total = round(costo_sin_descuento - monto_descuento, 2)

    # Guardar producto
    productos.append({
        "nombre": producto.title(),
        "cantidad": cantidad_producto,
        "precio_unitario": precio_unitario,
        "descuento": descuento,
        "costo_sin_descuento": costo_sin_descuento,
        "costo_total": costo_total
    })

    # Preguntar si se desea agregar otro producto
    while True:
        otra = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        if otra in ['s', 'n']:
            break
        else:
            print("Por favor, ingrese 's' para sí o 'n' para no.")
    if otra != 's':
        break

# Paso 3: Mostrar resultados
print("\n--- RESUMEN DE LA COMPRA ---")
total_general = 0
for idx, p in enumerate(productos, start=1):
    print(f"\nProducto #{idx}")
    print(f"Nombre: {p['nombre']}")
    print(f"Cantidad: {p['cantidad']}")
    print(f"Precio unitario: ${p['precio_unitario']:.2f}")
    print(f"Subtotal sin descuento: ${p['costo_sin_descuento']:.2f}")
    print(f"Descuento aplicado: {p['descuento']:.2f}%")
    print(f"Costo total del producto: ${p['costo_total']:.2f}")
    total_general += p['costo_total']

print(f"\nTOTAL GENERAL A PAGAR: ${total_general:.2f}")
