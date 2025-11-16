# Actividad 1: Añadir elementos a un diccionario

# 1) Dado el diccionario precios_frutas, agrego las frutas y precios indicados.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agrego Naranja y su precio
precios_frutas['Naranja'] = 1200

# Agrego Manzana y su precio
precios_frutas['Manzana'] = 1500

# Agrego Pera y su precio
precios_frutas['Pera'] = 2300

print("--- Actividad 1 ---")
print(f"Diccionario actualizado (después de agregar): {precios_frutas}")
print("-" * 25)





# Actividad 2: Actualizar valores en un diccionario

# 2) Actualizo los precios de las siguientes frutas, usando el diccionario de la Actividad 1.

# Actualizo el precio de Banana
precios_frutas['Banana'] = 1330

# Actualizo el precio de Manzana
precios_frutas['Manzana'] = 1700

# Actualizo el precio de Melón
precios_frutas['Melón'] = 2800

print("--- Actividad 2 ---")
print(f"Diccionario actualizado (después de actualizar): {precios_frutas}")
print("-" * 25)




# Actividad 3: Crear una lista a partir de las claves de un diccionario

# 3) Creo una lista que contenga únicamente las frutas (claves) sin los precios.
# Uso el método .keys() del diccionario para obtener las claves
# y luego convierto esa vista a una lista.
lista_frutas = list(precios_frutas.keys())

print("--- Actividad 3 ---")
print(f"Lista de frutas (claves): {lista_frutas}")
print("-" * 25)




# Actividad 4: Agenda de contactos (Diccionario)

# 4) Creo un programa para almacenar y consultar números telefónicos.

contactos = {}

# 1. Cargo 5 contactos. El nombre es la clave, el número es el valor.
print("--- Actividad 4: Carga de 5 contactos ---")
for i in range(5):
    # Solicito el nombre (clave) y el número (valor) al usuario.
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")

    # Almaceno en el diccionario
    contactos[nombre] = numero

print(f"\nLista de contactos cargados: {contactos}")

# 2. Pido un nombre y muestro el número asociado, si existe.
print("\n--- Actividad 4: Consulta de contacto ---")
nombre_consultar = input("Ingrese el nombre del contacto que deseo consultar: ")

# Verifico si el nombre está en los contactos
if nombre_consultar in contactos:
    numero_asociado = contactos[nombre_consultar]
    print(f"El número de teléfono de **{nombre_consultar}** es: **{numero_asociado}**")
else:
    print(f"El contacto **{nombre_consultar}** no se encuentra en la lista.")

print("-" * 25)





# Actividad 5: Palabras únicas y recuento (Set y Diccionario)

# 5) Solicito una frase e imprimo palabras únicas (set) y recuento (diccionario).
print("--- Actividad 5 ---")
frase = input("Ingrese una frase: ")

# Convierto la frase a minúsculas y la divido en palabras para hacer un recuento consistente.
palabras = frase.lower().split()

# 1. Obtengo las palabras únicas usando un set.
palabras_unicas = set(palabras)

# 2. Obtengo un diccionario con el recuento de cada palabra.
recuento_palabras = {}
for palabra in palabras:
    # Uso .get() para incrementar el contador si la palabra ya existe,
    # o la inicializo en 1 si es nueva.
    recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1

print("\nSalida:")
print(f"Palabras únicas (set): {palabras_unicas}")
print(f"Recuento (diccionario): {recuento_palabras}")

print("-" * 25)





# Actividad 6: Promedio de notas (Tuplas y Diccionarios)

# 6) Permito ingresar 3 alumnos con una tupla de 3 notas, luego muestro el promedio.

alumnos_notas = {}
num_alumnos = 3

print("--- Actividad 6: Carga de notas ---")
for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")

    # Solicito las 3 notas.
    try:
        nota1 = int(input("  Ingrese la nota 1: "))
        nota2 = int(input("  Ingrese la nota 2: "))
        nota3 = int(input("  Ingrese la nota 3: "))

        # Almaceno las notas como una tupla (estructura inmutable) en el diccionario.
        alumnos_notas[nombre] = (nota1, nota2, nota3)
    except ValueError:
        print("Error: Las notas deben ser números enteros. Omito este alumno.")

print(f"\nAlumnos y notas cargadas: {alumnos_notas}")

# Muestro el promedio de cada alumno.
print("\n--- Actividad 6: Promedios ---")
for nombre, notas in alumnos_notas.items():
    # 'notas' es una tupla, uso sum() y len() para calcular el promedio.
    promedio = sum(notas) / len(notas)
    print(f"El promedio de **{nombre}** es: **{promedio:.2f}**")

print("-" * 25)





# Actividad 7: Operaciones con Sets

# 7) Realizo operaciones con dos sets de estudiantes aprobados.

# Sets de ejemplo con los estudiantes aprobados en cada parcial:
parcial1_aprobados = {"Ana", "Juan", "Sofía", "Pedro", "Luis"}
parcial2_aprobados = {"Ana", "Luis", "Martín", "Elena", "Sofía"}

print("--- Actividad 7 ---")
print(f"Aprobados Parcial 1: {parcial1_aprobados}")
print(f"Aprobados Parcial 2: {parcial2_aprobados}")

# 1. Muestro los que aprobaron ambos parciales. (Intersección)
# Uso el método .intersection()
ambos_parciales = parcial1_aprobados.intersection(parcial2_aprobados)
print(f"\n1. Aprobaron **ambos** parciales: {ambos_parciales}")

# 2. Muestro los que aprobaron solo uno de los dos. (Diferencia Simétrica)
# Uso el método .symmetric_difference()
solo_uno = parcial1_aprobados.symmetric_difference(parcial2_aprobados)
print(f"2. Aprobaron **solo uno** de los dos: {solo_uno}")

# 3. Muestro la lista total de estudiantes que aprobaron al menos un parcial. (Unión)
# Uso el método .union(), el set automáticamente elimina repetidos.
al_menos_uno = parcial1_aprobados.union(parcial2_aprobados)
print(f"3. Aprobaron **al menos uno**: {al_menos_uno}")

print("-" * 25)





# Actividad 8: Gestión de Stock (Diccionario)

# 8) Armo un diccionario (producto: stock) y permito consultar, agregar stock o agregar producto.

inventario = {"Teclado": 15, "Mouse": 20, "Monitor": 8}

print("--- Actividad 8: Gestión de Inventario ---")
print(f"Inventario actual: {inventario}")

nombre_producto = input("\nIngrese el nombre del producto a gestionar: ")
nombre_producto = nombre_producto.capitalize() # Estandarizo la capitalización

# 1. Consulto el stock.
if nombre_producto in inventario:
    stock_actual = inventario[nombre_producto]
    print(f"Stock actual de **{nombre_producto}**: **{stock_actual}** unidades.")

    # 2. Pregunto si deseo agregar stock.
    opcion = input("¿Desea agregar unidades a este producto? (s/n): ").lower()
    if opcion == 's':
        try:
            unidades_agregar = int(input("  Ingrese la cantidad de unidades a agregar: "))
            if unidades_agregar > 0:
                # Agrego las unidades al stock existente
                inventario[nombre_producto] += unidades_agregar
                print(f"Stock de **{nombre_producto}** actualizado a: **{inventario[nombre_producto]}**")
            else:
                print("Cantidad no válida, no agrego stock.")
        except ValueError:
            print("Entrada no válida. Debo ingresar un número.")

else:
    # 3. Agrego un nuevo producto si no existe.
    print(f"El producto **{nombre_producto}** no existe en el inventario.")
    opcion = input("¿Desea agregarlo como nuevo producto? (s/n): ").lower()
    if opcion == 's':
        try:
            stock_inicial = int(input("  Ingrese el stock inicial para este producto: "))
            # Agrego el producto y su stock inicial al inventario
            inventario[nombre_producto] = stock_inicial
            print(f"Producto **{nombre_producto}** agregado con stock: **{stock_inicial}**.")
        except ValueError:
            print("Entrada no válida. Debo ingresar un número.")

print(f"\nInventario final: {inventario}")
print("-" * 25)






# Actividad 9: Agenda (Tupla como clave de Diccionario)

# 9) Creo una agenda donde las claves son tuplas (día, hora) y los valores son eventos.

agenda = {
    ("lunes", "10:00"): "Reunión de proyecto",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Entrenamiento",
    ("viernes", "18:00"): "Entrega de TP"
}

print("--- Actividad 9: Consulta de Agenda ---")
print("Eventos agendados (Ejemplo): Lunes 10:00, Martes 15:00, Jueves 09:30, Viernes 18:00")

# Permito consultar qué actividad hay en cierto día y hora.
dia_consulta = input("Ingrese el día (ej: lunes): ").lower()
hora_consulta = input("Ingrese la hora (ej: 10:00): ")

# La clave que busco es una tupla
clave_consulta = (dia_consulta, hora_consulta)

print(f"\nConsultando actividad para: {clave_consulta}")

# Consulto si la clave (tupla) existe en el diccionario.
if clave_consulta in agenda:
    evento = agenda[clave_consulta]
    print(f"A esa hora hay agendado: **{evento}**")
else:
    print("No hay ninguna actividad agendada para ese día y hora.")

print("-" * 25)






# Actividad 10: Invertir Diccionario

# 10) Invierto un diccionario: claves = capitales, valores = países.

original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo"}

# Creo el nuevo diccionario invertido.
invertido = {}

# Itero sobre los pares clave-valor (país-capital) del diccionario original.
for pais, capital in original.items():
    # En el nuevo diccionario, la capital se convierte en la clave,
    # y el país se convierte en el valor.
    invertido[capital] = pais

print("--- Actividad 10 ---")
print(f"Diccionario Original (País: Capital): {original}")
print(f"Diccionario Invertido (Capital: País): {invertido}")
print("-" * 25)