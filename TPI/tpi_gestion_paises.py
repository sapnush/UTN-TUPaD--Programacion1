import csv
import os

# ====================================================================
# A. CONFIGURACIÓN INICIAL
# ====================================================================

# Defino el nombre del archivo de datos base.
NOMBRE_ARCHIVO_BASE = 'paises.csv' 

# Calculo la ruta completa (path) al archivo CSV.
# Esto asegura que el programa encuentra el archivo sin importar desde dónde se ejecute.
RUTA_SCRIPT = os.path.dirname(os.path.abspath(__file__))
RUTA_COMPLETA_CSV = os.path.join(RUTA_SCRIPT, NOMBRE_ARCHIVO_BASE)


# ====================================================================
# B. LECTURA DE DATOS
# ====================================================================

def leer_datos_csv():
    # Esta función lee la información de países desde el archivo CSV usando la ruta absoluta.
    paises = []
    
    # Manejo los posibles errores de apertura del archivo.
    try:
        # Abro el archivo usando la RUTA COMPLETA, sin importar la carpeta actual.
        with open(RUTA_COMPLETA_CSV, 'r', newline='', encoding='utf-8') as archivo:
            # Utilizo DictReader para que cada fila se convierta en un diccionario.
            lector_csv = csv.DictReader(archivo)
            
            # Recorro cada registro (cada país) que encuentro.
            for fila in lector_csv:
                try:
                    # Implemento la conversión de los datos numéricos a enteros.
                    pais = {
                        'nombre': fila['nombre'].strip(),
                        # Convierto a entero (int) para poder hacer cálculos.
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'].strip()
                    }
                    paises.append(pais)
                
                except ValueError:
                    # Informo que encontré un error de formato11 en el dato.
                    print(f"Error de formato en la fila: {fila['nombre']}. Población o superficie no son números válidos.")
                except KeyError as e:
                    # Informo si falta alguna de las columnas clave en el CSV.
                    print(f"Error: No encuentro la columna {e} en el archivo CSV.")
                    return [] 
        
        # Si llego aquí, la carga fue exitosa.
        print(f"Se cargaron {len(paises)} países correctamente desde {NOMBRE_ARCHIVO_BASE}.")
        return paises
        
    except FileNotFoundError:
        print(f"Error: No pude encontrar el archivo '{NOMBRE_ARCHIVO_BASE}'. Verifique que exista en la carpeta del script.")
        return []
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el CSV: {e}")
        return []


# ====================================================================
# C. INTERFAZ Y MENÚ
# ====================================================================

def mostrar_menu():
    # Muestra el menú principal y pide la elección.
    print("\n" + "="*40)
    print("      GESTOR DE DATOS DE PAÍSES")
    print("="*40)
    print("1. Agregar un nuevo país")
    print("2. Actualizar datos de un país (Población/Superficie)")
    print("3. Buscar país por nombre")
    print("4. Filtrar países (por Continente o Rango)")
    print("5. Ordenar lista de países")
    print("6. Mostrar Estadísticas")
    print("7. Listar todos los países")
    print("8. Salir")
    print("-" * 40)
    
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion


# ====================================================================
# D. FUNCIONALIDADES DE GESTIÓN (Opciones 1, 2, 3, 4, 5, 6, 7)
# ====================================================================

# --- Funciones de Utilidad y Listado (Opción 7) ---

def buscar_pais_por_nombre(lista_paises, nombre_buscado):
    # Utilidad: Busca un país en la lista por su nombre (parcial o exacta).
    # Retorna el índice y el país, o None si no lo encuentra.3
    nombre_buscado_lower = nombre_buscado.lower()
    for i, pais in enumerate(lista_paises):
        # Comparación flexible.
        if nombre_buscado_lower in pais['nombre'].lower():
            return i, pais
    return None, None


def listar_paises(lista_paises):
    # Función (Opción 7): Muestro todos los países en formato tabular.
    if not lista_paises:
        print("La lista de países está vacía.")
        return
        
    print("\n{:^15} {:<25} {:>15} {:>15}".format("Continente", "Nombre", "Población", "Superficie (km²)"))
    print("-" * 70)
    
    # Recorro la lista para imprimir los datos de cada país.
    for pais in lista_paises:
        # Aplico formato de miles (,) para facilitar la lectura.
        poblacion_f = f"{pais['poblacion']:,}"
        superficie_f = f"{pais['superficie']:,}"
        
        print("{:^15} {:<25} {:>15} {:>15}".format(
            pais['continente'],
            pais['nombre'],
            poblacion_f,
            superficie_f
        ))
    print("-" * 70)


# --- Opción 1: Agregar País ---

def agregar_pais(lista_paises):
    # Función (Opción 1): Añadir un país con validaciones.
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    # 1. Solicito campos de texto.
    nombre = input("Ingrese el nombre del país: ").strip()
    continente = input("Ingrese el continente: ").strip()
    
    if not nombre or not continente:
        print("Error: El nombre del país y el continente no pueden estar vacíos. Intente de nuevo.")
        return

    # 2. Solicito campos numéricos con validación.
    try:
        poblacion = int(input("Ingrese la población (número entero): ").strip())
        superficie = int(input("Ingrese la superficie en km² (número entero): ").strip())
        
        if poblacion < 0 or superficie < 0:
            print("Error: La población y la superficie deben ser números positivos. Intente de nuevo.")
            return

    except ValueError:
        print("Error: La población y la superficie deben ser números enteros válidos. Intente de nuevo.")
        return

    # 3. Añadir a la lista.
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    lista_paises.append(nuevo_pais)
    print(f"\n{nombre} agregado exitosamente a la lista.")


# --- Opción 2: Actualizar Datos ---

def actualizar_pais(lista_paises):
    # Función (Opción 2): Actualización de Población y Superficie.
    print("\n--- ACTUALIZAR DATOS DE PAÍS ---")
    nombre = input("Ingrese el nombre del país que deseo actualizar: ").strip()
    
    # Utilizo mi función de búsqueda modular.
    indice, pais_encontrado = buscar_pais_por_nombre(lista_paises, nombre)
    
    if pais_encontrado is None:
        print(f"Error: No encontré ningún país que coincida con '{nombre}'.")
        return
        
    print(f"\nPaís encontrado: {pais_encontrado['nombre']} ({pais_encontrado['continente']})")
    
    # Solicito los nuevos datos numéricos con validaciones.
    try:
        nueva_poblacion = int(input(f"Ingrese la NUEVA población (Actual: {pais_encontrado['poblacion']:,}): ").strip())
        nueva_superficie = int(input(f"Ingrese la NUEVA superficie (Actual: {pais_encontrado['superficie']:,}): ").strip())
        
        if nueva_poblacion < 0 or nueva_superficie < 0:
            print("Error: Los valores deben ser números positivos.")
            return

    except ValueError:
        print("Error: Los nuevos datos de población y superficie deben ser números enteros válidos.")
        return

    # Actualizo los datos en la lista principal
    lista_paises[indice]['poblacion'] = nueva_poblacion
    lista_paises[indice]['superficie'] = nueva_superficie
    print(f"\nLos datos de {pais_encontrado['nombre']} se actualizaron exitosamente.")


# --- Opción 3: Buscar País ---

def buscar_pais_menu(lista_paises):
    # Función de interfaz para la búsqueda de un país por nombre.
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")
    nombre = input("Ingrese parte o todo el nombre del país que busco: ").strip()
    indice, pais_encontrado = buscar_pais_por_nombre(lista_paises, nombre)
    
    if pais_encontrado is None:
        print(f"Error: No encontré ningún país que coincida con '{nombre}'.")
        return
        
    print("\n¡País encontrado!")
    print("-" * 40)
    print(f"Nombre: {pais_encontrado['nombre']}")
    print(f"Continente: {pais_encontrado['continente']}")
    print(f"Población: {pais_encontrado['poblacion']:,}")
    print(f"Superficie (km²): {pais_encontrado['superficie']:,}")
    print("-" * 40)


# --- Opción 4: Filtrar Países ---

def filtrar_por_continente(lista_paises):
    # Lógica de filtro por string.
    continente_buscado = input("Ingrese el continente por el que desea filtrar: ").strip().lower()
    resultados = []
    for pais in lista_paises:
        if pais['continente'].lower() == continente_buscado:
            resultados.append(pais)
    return resultados


def filtrar_por_rango(lista_paises):
    # Lógica de filtro por rango numérico.
    print("\n--- FILTRAR POR RANGO ---")
    print("1. Filtrar por Población")
    print("2. Filtrar por Superficie")
    opcion = input("Seleccione el criterio (1 o 2): ")
    
    clave = ""
    if opcion == '1':
        clave = 'poblacion'
    elif opcion == '2':
        clave = 'superficie'
    else:
        print("Opción inválida.")
        return []
        
    # Pido los valores mínimo y máximo con manejo de errores (try-except).
    try:
        min_val = int(input(f"Ingrese el valor mínimo para {clave}: ").strip())
        max_val = int(input(f"Ingrese el valor máximo para {clave}: ").strip())
    except ValueError:
        print("Error: Los valores deben ser números enteros válidos.")
        return []
        
    if min_val > max_val:
        print("Error: El valor mínimo no puede ser mayor que el máximo.")
        return []

    resultados = []
    # Recorro y aplico la condición de rango.
    for pais in lista_paises:
        valor_pais = pais[clave]
        if min_val <= valor_pais <= max_val:
            resultados.append(pais)
            
    return resultados


def filtrar_paises_menu(lista_paises):
    # Función de interfaz (Opción 4) para el filtrado de países.
    print("\n--- FILTROS DE PAÍSES ---")
    print("1. Filtrar por Continente")
    print("2. Filtrar por Rango Numérico (Población o Superficie)")
    print("3. Volver al menú principal")
    
    opcion = input("Ingrese la opción deseada (1, 2 o 3): ")
    lista_filtrada = []
    
    if opcion == '1':
        lista_filtrada = filtrar_por_continente(lista_paises)
    elif opcion == '2':
        lista_filtrada = filtrar_por_rango(lista_paises)
    elif opcion == '3':
        print("Volviendo al menú principal.")
        return
    else:
        print("Opción inválida. Intente de nuevo.")
        return
        
    # Muestro los resultados, reutilizando la función listar_paises.
    if lista_filtrada:
        print(f"\nSe encontraron {len(lista_filtrada)} resultados.")
        listar_paises(lista_filtrada)
    else:
        print("\nNo se encontraron países que coincidan con los criterios de búsqueda.")


# --- Opción 5: Ordenar Países ---

def ordenar_paises_menu(lista_paises):
    # Permite al usuario ordenar la lista de países por un criterio.
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Ordenar por Nombre (A-Z)")
    print("2. Ordenar por Población (Mayor a Menor)")
    print("3. Ordenar por Superficie (Mayor a Menor)")
    opcion = input("Seleccione el criterio (1, 2 o 3): ")

    clave = None
    reversa = False

    if opcion == '1':
        clave = 'nombre'
    elif opcion == '2':
        clave = 'poblacion'
        reversa = True # Mayor a Menor
    elif opcion == '3':
        clave = 'superficie'
        reversa = True # Mayor a Menor
    else:
        print("Opción inválida.")
        return

    # Utilizamos la función sorted() de Python.
    # Usamos una función lambda para especificar la clave de ordenamiento.
    lista_ordenada = sorted(lista_paises, key=lambda pais: pais[clave], reverse=reversa)

    print(f"\nLista ordenada por {clave} ({'Descendente' if reversa else 'Ascendente'}):")
    listar_paises(lista_ordenada)


# --- Opción 6: Mostrar Estadísticas ---

def mostrar_estadisticas(lista_paises):
    # Calcula y muestra el total de población, promedio de superficie y países por continente.
    if not lista_paises:
        print("\nNo hay datos para calcular estadísticas.")
        return

    print("\n--- ESTADÍSTICAS GLOBALES ---")

    # 1. Población total
    poblacion_total = sum(pais['poblacion'] for pais in lista_paises)
    print(f"Población total de los países cargados: {poblacion_total:,}")

    # 2. Superficie promedio
    superficie_total = sum(pais['superficie'] for pais in lista_paises)
    promedio_superficie = superficie_total / len(lista_paises)
    print(f"Superficie promedio por país: {promedio_superficie:,.2f} km²")

    # 3. Cantidad de países por continente
    conteo_continentes = {}
    for pais in lista_paises:
        continente = pais['continente']
        # Si el continente no está en el diccionario, lo inicializa en 0. Si ya está, suma 1.
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad}")


# ====================================================================
# E. FUNCIÓN PRINCIPAL DE EJECUCIÓN
# ====================================================================

def main():
    # Esta es la función principal. Inicia la aplicación, 
    # carga los datos y gestiona el bucle del menú.
    
    # 1. Cargo los datos al iniciar el programa.
    datos_paises = leer_datos_csv() 
    
    # Si la carga falla, salgo.
    if not datos_paises:
        print("El programa no puede continuar sin datos. Verifico el archivo CSV.")
        return

    # 2. Entro al bucle que mantiene el menú funcionando.
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            # Opción 1: Agregar País
            agregar_pais(datos_paises)
        
        elif opcion == '2':
            # Opción 2: Actualizar Datos
            actualizar_pais(datos_paises)
        
        elif opcion == '3':
            # Opción 3: Buscar país
            buscar_pais_menu(datos_paises)
            
        elif opcion == '4':
            # Opción 4: Filtrar países
            filtrar_paises_menu(datos_paises)
            
        elif opcion == '5':
            # Opción 5: Ordenar países
            ordenar_paises_menu(datos_paises) 
            
        elif opcion == '6':
            # Opción 6: Mostrar Estadísticas
            mostrar_estadisticas(datos_paises)
            
        elif opcion == '7':
            # Opción 7: Listar todos los países.
            print("\nOpción 7: Listar Países")
            listar_paises(datos_paises)
        
        elif opcion == '8':
            # Opción 8: Salir
            print("\nTerminé la ejecución. ¡Hasta pronto!")
            break 
        
        else:
            print("\nOpción inválida. Por favor, ingreso un número del 1 al 8.")

# Bloque que indica que la función 'main' debe ejecutarse cuando corro este script.
if __name__ == "__main__":
    main()