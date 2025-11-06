# 
#
#1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja.
#
import random

# [random.uniform(1.0, 10.0) for _ in range(10)] genera 10 números al azar.
notas = [random.uniform(1.0, 10.0) for _ in range(10)]

# Redondeamos las notas a un decimal para que sean más legibles.
notas = [round(nota, 1) for nota in notas] 

print("--- Listado de Notas (10 Estudiantes) ---")

# • Mostrar la lista completa.
# Usamos un bucle 'for' para mostrar las notas de forma individual,
# cumpliendo con la nota del práctico de usar estructuras repetitivas.
for nota in notas:
    print(f"| {nota:.1f} |", end=" ")
print("\n") # Salto de línea al final del listado

# • Calcular y mostrar el promedio.
# La función 'sum()' suma todos los elementos de la lista.
suma_notas = sum(notas)

# La función 'len()' obtiene el número total de elementos (10 en este caso).
cantidad_estudiantes = len(notas)

# Calculamos el promedio. Usamos :.2f para mostrar dos decimales.
promedio = suma_notas / cantidad_estudiantes

print(f"Promedio General: {promedio:.2f}")

# • Indicar la nota más alta y la más baja.
# La función 'max()' encuentra el valor más grande.
nota_maxima = max(notas)

# La función 'min()' encuentra el valor más pequeño.
nota_minima = min(notas)

print(f"Nota más alta (Máxima): {nota_maxima:.1f}")
print(f"Nota más baja (Mínima): {nota_minima:.1f}")






#2) Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# Pedir al usuario que cargue 5 productos en una lista.
productos = []
print("--- Gestión de Productos ---")
print("Por favor, ingresa el nombre de 5 productos:")

# Usamos un bucle for para iterar 5 veces y pedir la entrada del usuario.
for i in range(5):
    producto = input(f"Producto {i + 1}: ")
    productos.append(producto) # Añadimos el producto ingresado a la lista.

print(f"\nLista original de productos: {productos}")

# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# La función sorted() recibe un iterable (la lista 'productos') y devuelve una
# NUEVA LISTA ORDENADA. La lista 'productos' original no se modifica.
productos_ordenados = sorted(productos)

print(f"Lista ordenada alfabéticamente (usando sorted()): {productos_ordenados}")

# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
while True:
    producto_eliminar = input("\n¿Qué producto deseas eliminar de la lista? (Ingresa el nombre exactamente): ")
    
    try:
        # El método remove() elimina la PRIMERA aparición del valor especificado.
        # Si el valor no se encuentra, lanza una excepción ValueError.
        productos.remove(producto_eliminar)
        print(f"'{producto_eliminar}' ha sido eliminado.")
        break  # Salimos del bucle si la eliminación fue exitosa
    except ValueError:
        # Manejamos el error si el producto no existe en la lista.
        print(f"Error: El producto '{producto_eliminar}' no se encontró en la lista. Intenta de nuevo.")

# Mostrar la lista final actualizada.
print(f"Lista final actualizada: {productos}")






#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista.
#
import random

# 1) Generar una lista con 15 números enteros al azar entre 1 y 100.
# Usamos random.randint(1, 100) para asegurar que los números sean enteros.
numeros_al_azar = [random.randint(1, 100) for _ in range(15)]

print("--- Lista Original de 15 Números al Azar (entre 1 y 100) ---")
# Mostramos la lista completa para referencia.
print(numeros_al_azar)

# 2) Crear una lista con los pares y otra con los impares.
pares = []
impares = []

# Iteramos sobre la lista de números al azar.
for num in numeros_al_azar:
    # Usamos el operador módulo (%) para verificar la paridad.
    # Si el resto de la división por 2 es 0, el número es par.
    if num % 2 == 0:
        pares.append(num)
    else:
        # Si el resto es 1, el número es impar.
        impares.append(num)

# Muestro resultados y conteos 

print("\n--- Números Pares ---")
# Mostramos la lista de pares usando una estructura repetitiva (bucle for).
for p in pares:
    print(p, end=" | ")
print() # Salto de línea

# • Mostrar cuántos números tiene cada lista.
print(f"Total de números pares: {len(pares)}")


print("\n--- Números Impares ---")
# Mostramos la lista de impares.
for i in impares:
    print(i, end=" | ")
print() # Salto de línea

# • Mostrar cuántos números tiene cada lista.
print(f"Total de números impares: {len(impares)}")

# Verificación de la suma de conteos (debe ser 15)
# print(f"\nVerificación (pares + impares): {len(pares) + len(impares)}")





#4) Dada una lista con valores repetidos: 
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado. 

# Dada una lista con valores repetidos:
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
print("Eliminación de duplicados")
print(f"Mi lista original con valores repetidos es: {datos}")

# • Crear una nueva lista sin elementos repetidos.
# Para esta tarea, utilizo el tipo de dato 'set' (conjunto).
# La propiedad principal de un conjunto es que no permite elementos duplicados.

# 1. Convierto la lista 'datos' en un 'set'. Al hacerlo, Python elimina automáticamente los duplicados.
datos_unicos_set = set(datos) 

# 2. Convierto el 'set' resultante de vuelta a una lista para obtener la estructura requerida.
datos_sin_repetir = list(datos_unicos_set)

# • Muestro el resultado.
print(f"Mi nueva lista sin elementos repetidos es: {datos_sin_repetir}")






#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada. 

# 1) Creo una lista con los nombres de 8 estudiantes presentes en clase.
estudiantes = ["Sofía", "Pablo", "Laura", "Daniel", "Camila", "Andrés", "Valeria", "Ricardo"]
print("Gestión de aistencia de estudiantes")
print(f"Mi lista inicial de 8 estudiantes es: {estudiantes}")

# 2) Pregunto al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
while True:
    # Convierto la entrada a mayúsculas para simplificar la validación.
    accion = input("¿Quiero AGREGAR (A) o ELIMINAR (E) un estudiante? (Escribo A/E o SALIR): ").upper()
    
    if accion == "A":
        # Opción para agregar un estudiante.
        nuevo_estudiante = input("Ingreso el nombre del estudiante a agregar: ")
        # Uso append() para añadir el nuevo estudiante al final de la lista.
        estudiantes.append(nuevo_estudiante)
        print(f"Confirmado: '{nuevo_estudiante}' ha sido agregado a la lista.")
    
    elif accion == "E":
        # Opción para eliminar un estudiante.
        estudiante_a_eliminar = input("Ingreso el nombre del estudiante a eliminar: ")
        
        try:
            # Uso remove() para eliminar al estudiante por su nombre (valor).
            estudiantes.remove(estudiante_a_eliminar)
            print(f"Confirmado: '{estudiante_a_eliminar}' ha sido eliminado.")
        except ValueError:
            # Capturo el error si el nombre ingresado no está en mi lista.
            print(f"Error: El estudiante '{estudiante_a_eliminar}' no se encontró. No puedo eliminarlo.")
    
    elif accion == "SALIR":
        # Condición de salida del bucle.
        print("\nFinalizo la gestión de la lista.")
        break
    
    else:
        # Mensaje para entradas no válidas.
        print("Opción no válida. Debo ingresar A, E o SALIR.")

# 3) Muestro la lista final actualizada.
print("\n--- Muestro mi Lista Final Actualizada ---")
# Uso un bucle for para mostrar los nombres individualmente.
for est in estudiantes:
    print(est, end=" | ")
print(f"\nTotal final de estudiantes: {len(estudiantes)}")






#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero).

# 1) Dada una lista con 7 números, creo la lista inicial.
numeros_rotar = [10, 20, 30, 40, 50, 60, 70]
print("Rotación de lista")
print(f"Mi lista original es: {numeros_rotar}")

# 2) Roto todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

# Paso A: Extraigo el último elemento de la lista. 
# Uso el método pop() sin argumentos, que elimina y devuelve el último elemento.
ultimo_elemento = numeros_rotar.pop() # El elemento 70 es extraído.
# Ahora la lista 'numeros_rotar' es [10, 20, 30, 40, 50, 60].

# Paso B: Inserto el elemento extraído en la primera posición (índice 0).
# Uso el método insert(indice, valor).
numeros_rotar.insert(0, ultimo_elemento) 
# La lista 'numeros_rotar' ahora es [70, 10, 20, 30, 40, 50, 60].

# Muestro el resultado de la rotación.
print(f"Mi lista después de la rotación es: {numeros_rotar}")






#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica.

# 1) Creo una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# La estructura es [[Min, Max], [Min, Max], ...].
# Uso datos de ejemplo para 7 días, desde el Lunes hasta el Domingo.
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [
    [10, 25],  # Lunes
    [12, 28],  # Martes
    [15, 30],  # Miércoles
    [14, 26],  # Jueves
    [11, 22],  # Viernes
    [16, 32],  # Sábado 
    [18, 29]   # Domingo
]

print("\n--- Análisis de Temperaturas Semanales (Mínima / Máxima) ---")
# Muestro la matriz completa y legible para referencia.
for i in range(len(dias)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    print(f"| {dias[i]}: Mín {minima}°C | Máx {maxima}°C |")


# 2) Calculo el promedio de las mínimas y el de las máximas.

# Extraigo todas las temperaturas mínimas (columna 0) y máximas (columna 1) 
# usando comprensión de listas para mayor eficiencia.
minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

# Calculo los promedios.
promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)

print(f"Mi promedio de temperaturas mínimas es: {promedio_minimas:.2f}°C")
print(f"Mi promedio de temperaturas máximas es: {promedio_maximas:.2f}°C")


# 3) Muestro en qué día se registró la mayor amplitud térmica.
# Amplitud térmica = Máxima - Mínima.

amplitudes = []
for min_temp, max_temp in temperaturas:
    amplitud = max_temp - min_temp
    amplitudes.append(amplitud)

# Encuentro la mayor amplitud en la lista 'amplitudes'.
mayor_amplitud = max(amplitudes)

# Encuentro el índice de esa mayor amplitud para saber a qué día corresponde.
indice_mayor_amplitud = amplitudes.index(mayor_amplitud)

# Uso el índice para obtener el nombre del día de mi lista 'dias'.
dia_mayor_amplitud = dias[indice_mayor_amplitud]

print(f"\nLa mayor amplitud térmica fue de {mayor_amplitud}°C.")
print(f"Se registró el día: {dia_mayor_amplitud}.")





#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

# 1) Creo una matriz con las notas de 5 estudiantes en 3 materias.
# Estructura: Las filas representan a los estudiantes y las columnas a las materias.
# [[NotaMateria1, NotaMateria2, NotaMateria3] (Estudiante 1), ...]
estudiantes_nombres = ["Ana", "Beto", "Carla", "David", "Elena"]
materias = ["Programación", "Base Datos", "Inglés"]

notas_estudiantes = [
    [8.0, 7.5, 9.0], # Notas de Ana
    [6.0, 5.5, 7.0], # Notas de Beto
    [9.5, 8.0, 8.5], # Notas de Carla
    [7.0, 9.0, 6.5], # Notas de David
    [5.0, 6.5, 7.5]  # Notas de Elena
]

print("\n--- Análisis de Notas (Matriz 5x3) ---")

# Muestro la matriz de notas de manera legible.
print("Estudiante\t| Programación\t| Base Datos\t| Inglés")

for i in range(len(estudiantes_nombres)):
    # Accedo a la fila completa del estudiante [i] y muestro sus notas.
    nota_prog = notas_estudiantes[i][0]
    nota_bd = notas_estudiantes[i][1]
    nota_ing = notas_estudiantes[i][2]
    print(f"{estudiantes_nombres[i]}\t| {nota_prog:.1f}\t\t| {nota_bd:.1f}\t\t| {nota_ing:.1f}")


# 2) Muestro el promedio de cada estudiante (promedio por fila).
print("Promedio por estudiante")
for i in range(len(estudiantes_nombres)):
    # Obtengo la lista de notas de la fila 'i'.
    notas_fila = notas_estudiantes[i]
    
    # Sumo las notas de la fila y divido por la cantidad de materias (columnas).
    promedio_estudiante = sum(notas_fila) / len(notas_fila)
    
    print(f"Mi promedio para {estudiantes_nombres[i]} es: {promedio_estudiante:.2f}")


# 3) Muestro el promedio de cada materia (promedio por columna).
print("Promedio por materia")

# Itero sobre las columnas (materias).
for j in range(len(materias)):
    suma_materia = 0
    
    # Itero sobre las filas (estudiantes) para sumar las notas de la columna 'j'.
    for i in range(len(estudiantes_nombres)):
        # Accedo al elemento en la posición [fila][columna]
        suma_materia += notas_estudiantes[i][j]
    
    # Calculo el promedio dividiendo por la cantidad de estudiantes (filas).
    promedio_materia = suma_materia / len(estudiantes_nombres)
    
    print(f"Mi promedio para la materia {materias[j]} es: {promedio_materia:.2f}")





#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada.  

# 1) Represento un tablero de Ta-Te-Ti como una lista de listas (3x3).
# Inicializo el tablero con guiones "-" representando casillas vacías.
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print("Juego: Ta-Te-Ti (Tres en Raya)")

# Defino una función auxiliar para mostrar el tablero de forma legible.
def mostrar_tablero(t):
    """Función que uso para mostrar el estado actual del tablero."""
    print("\n  0 1 2")  # Muestro los índices de columna
    print("-------")
    for i in range(3):
        # Muestro el índice de fila 'i' y luego los elementos de esa fila, separados por espacio.
        print(f"{i}| {' '.join(t[i])}")
    print("-------")

# Defino una función para verificar si el jugador actual ha ganado.
def verificar_ganador(t, jugador):
    """Verifico todas las posibles combinaciones ganadoras (filas, columnas, diagonales)."""
    
    # Verifico las 3 Filas y las 3 Columnas
    for i in range(3):
        # Condición 1: Compruebo si todos los elementos de la Fila 'i' son iguales al símbolo del jugador.
        if all(t[i][j] == jugador for j in range(3)):
            return True
        # Condición 2: Compruebo si todos los elementos de la Columna 'i' son iguales al símbolo del jugador.
        if all(t[j][i] == jugador for j in range(3)):
            return True
    
    # Verifico la Diagonal Principal (0,0), (1,1), (2,2)
    if t[0][0] == jugador and t[1][1] == jugador and t[2][2] == jugador:
        return True
        
    # Verifico la Diagonal Secundaria (0,2), (1,1), (2,0)
    if t[0][2] == jugador and t[1][1] == jugador and t[2][0] == jugador:
        return True
        
    return False

# 2) Permito que dos jugadores ingresen posiciones para colocar "X" o "O".
jugador_actual = "X"
turno = 0 # Uso el contador para saber si hay empate (máximo 9 turnos).
juego_terminado = False

mostrar_tablero(tablero)

while turno < 9 and not juego_terminado:
    print(f"Es el turno del Jugador {jugador_actual}")
    
    try:
        # Pido la fila y la columna al usuario.
        fila = int(input("Ingreso la fila (0, 1, o 2): "))
        columna = int(input("Ingreso la columna (0, 1, o 2): "))
        
        # 3) Muestro el tablero después de cada jugada.
        
        # Primero, valido que las coordenadas sean válidas y la casilla esté vacía.
        if 0 <= fila <= 2 and 0 <= columna <= 2 and tablero[fila][columna] == "-":
            
            # Marco la casilla: modifico la matriz anidada en la posición [fila][columna].
            tablero[fila][columna] = jugador_actual
            mostrar_tablero(tablero)
            turno += 1
            
            # Verifico si el jugador actual ganó.
            if verificar_ganador(tablero, jugador_actual):
                print(f"\n¡VICTORIA! El jugador {jugador_actual} ha ganado.")
                juego_terminado = True
            else:
                # Si no ganó, cambio al otro jugador para el siguiente turno.
                jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Movimiento inválido. Debo ingresar coordenadas 0-2 y la casilla debe estar vacía.")
            
    except ValueError:
        print("Error: La entrada debe ser un número entero (0, 1 o 2). Intento de nuevo.")

# Condición de empate (si todos los 9 turnos se jugaron y nadie ganó).
if turno == 9 and not juego_terminado:
    print("¡Es un EMPATE! El tablero está lleno.")





#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana.

# 1) Defino la matriz de ventas (4 productos x 7 días).
# Las filas representan los productos y las columnas los días.
productos_nombres = ["PC", "Monitor", "Teclado", "Mouse"]
dias_semana = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

# Mis datos de ventas simuladas (unidades vendidas):
# Filas: Productos (4)
# Columnas: Días (7)
ventas = [
    [10, 12, 15, 11, 14, 20, 18], # Ventas de PC
    [ 5,  8,  9,  6,  7, 10,  8], # Ventas de Monitor
    [20, 18, 25, 22, 30, 40, 35], # Ventas de Teclado
    [30, 25, 35, 32, 45, 50, 48]  # Ventas de Mouse
]

print("\n--- Análisis de Ventas Semanales (Matriz 4x7) ---")

# Muestro la matriz de ventas de manera legible.
print("Producto\t|", "\t".join(dias_semana))

for i in range(len(productos_nombres)):
    ventas_dia_str = "\t".join(map(str, ventas[i]))
    print(f"{productos_nombres[i]}\t| {ventas_dia_str}")


# 2) Muestro el total vendido por cada producto (Suma por fila).
print("Total Vendido por Producto")
total_por_producto = []
for i in range(len(productos_nombres)):
    # Sumo la fila completa de ventas[i].
    total_producto = sum(ventas[i])
    total_por_producto.append(total_producto)
    print(f"Total vendido de {productos_nombres[i]}: {total_producto} unidades.")


# 3) Muestro el día con mayores ventas totales (Suma por columna).
print("Análisis de Ventas por Día")
total_por_dia = []
# Itero sobre las columnas (días).
for j in range(len(dias_semana)):
    suma_dia = 0
    # Itero sobre las filas (productos) para sumar las ventas del día 'j'.
    for i in range(len(productos_nombres)):
        suma_dia += ventas[i][j]
    total_por_dia.append(suma_dia)

# Encuentro el día con el total máximo.
max_ventas_dia = max(total_por_dia)
indice_max_dia = total_por_dia.index(max_ventas_dia)
dia_max_ventas = dias_semana[indice_max_dia]

print(f"Mis ventas totales por día fueron: {total_por_dia}")
print(f"El día con mayores ventas totales fue {dia_max_ventas}, con {max_ventas_dia} unidades vendidas.")


# 4) Indico cuál fue el producto más vendido en la semana.
# Reutilizo mi lista 'total_por_producto' calculada en el punto 2.

max_ventas_producto = max(total_por_producto)
indice_max_producto = total_por_producto.index(max_ventas_producto)
producto_mas_vendido = productos_nombres[indice_max_producto]

print(f"El producto más vendido en la semana es: {producto_mas_vendido}, con un total de {max_ventas_producto} unidades.")




