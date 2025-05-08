# Paso 1: Ingreso de calificación individual
while True:
    try:
        nota = float(input("Ingresa una calificación individual (0 a 100): "))
        if 0 <= nota <= 100:
            break
        else:
            print("Calificación fuera del rango. Intenta de nuevo.")
    except ValueError:
        print("Entrada inválida. Intenta de nuevo.")

# Evaluar estado de aprobación
estado = "Aprobado" if nota >= 60 else "Reprobado"
print(f"Estado: {estado}")

# Paso 2: Ingreso de lista de calificaciones
entrada = input("\nIngresa varias calificaciones separadas por comas (0 a 100): ")
lista_calificaciones = []

# Procesar entradas y validar cada calificación
for valor in entrada.split(','):
    try:
        cal = float(valor.strip())
        if 0 <= cal <= 100:
            lista_calificaciones.append(cal)
        else:
            print(f"Ignorada calificación fuera de rango: {cal}")
    except ValueError:
        print(f"Ignorada entrada inválida: {valor.strip()}")

# Mostrar lista de calificaciones válidas
print(f"\nLista de calificaciones válidas ({len(lista_calificaciones)}): {lista_calificaciones}")

# Calcular promedio
if lista_calificaciones:
    promedio = sum(lista_calificaciones) / len(lista_calificaciones)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones válidas.")

# Paso 3: Contar cuántas calificaciones son mayores que un valor específico
while True:
    try:
        valor_comparar = float(input("\nIngresa un valor para comparar (0 a 100): "))
        if 0 <= valor_comparar <= 100:
            break
        else:
            print("El valor debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Intenta de nuevo.")

# Contar usando bucle while
contador_mayores = 0
i = 0
while i < len(lista_calificaciones):
    if lista_calificaciones[i] > valor_comparar:
        contador_mayores += 1
    i += 1

print(f"Número de calificaciones mayores que {valor_comparar}: {contador_mayores}")

# Paso 4: Verificar y contar una calificación específica
while True:
    try:
        calificacion_especifica = float(input("\nIngresa una calificación específica a buscar: "))
        if 0 <= calificacion_especifica <= 100:
            break
        else:
            print("La calificación debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Intenta de nuevo.")

# Conteo de ocurrencias
conteo = 0
for cal in lista_calificaciones:
    if cal == calificacion_especifica:
        conteo += 1

if conteo > 0:
    print(f"La calificación {calificacion_especifica} aparece {conteo} veces en la lista.")
else:
    print(f"La calificación {calificacion_especifica} no se encuentra en la lista.")