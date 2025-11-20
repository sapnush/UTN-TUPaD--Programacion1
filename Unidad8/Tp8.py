#------------- TP MANEJO DE ARCHIVOS --------------
# Estudiante: Sabina Perez

#Consignas y resolusion:

#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

# Coloco esta función para crear y poblar el archivo 'productos.txt'
# con los datos iniciales que nos pide el enunciado.
def crear_archivo_inicial():
    # Uso 'with open' para asegurar que el archivo se cierre automáticamente,
    # que es una buena práctica. Uso el modo 'w' (write/escritura) para crear el archivo
    # o sobrescribirlo si ya existe, garantizando que solo tenga los 3 productos iniciales.
    with open('productos.txt', 'w') as archivo:
        # Escribo cada producto en una línea separada, siguiendo el formato
        # nombre,precio,cantidad. Agrego el carácter de nueva línea '\n' al final
        # de cada línea para que el siguiente producto empiece correctamente abajo.
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno A4,850.0,15\n")
        archivo.write("Resaltador,95.75,50\n")

    # Informo al usuario que el archivo ya está listo.
    print("Archivo 'productos.txt' creado con los 3 productos iniciales.")

# Llamo a la función para que se ejecute y cree el archivo.
crear_archivo_inicial()






#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:

#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# Coloco esta función para leer el archivo 'productos.txt' y mostrar los datos formateados.
def leer_y_mostrar_productos():
    print("--- Listado de Productos ---")

    # Uso 'with open' en modo lectura ('r') para acceder al archivo de manera segura.
    try:
        with open('productos.txt', 'r') as archivo:
            # Recorro cada línea que está dentro del archivo.
            for linea in archivo:
                # Primero, uso .strip() para limpiar la línea de posibles espacios
                # o el salto de línea al final.
                linea_limpia = linea.strip()

                # Luego, uso .split(',') para dividir la cadena en una lista de
                # tres elementos: [nombre, precio, cantidad].
                datos = linea_limpia.split(',')

                # Verifico que la línea contenga los 3 datos esperados antes de procesarla.
                if len(datos) == 3:
                    nombre = datos[0]
                    # Convierto el precio a float (número decimal) para el formato de salida.
                    # Asumo que el precio es el segundo elemento de la lista (índice 1).
                    precio = float(datos[1])
                    # La cantidad la dejo como string, es suficiente para solo mostrarla.
                    cantidad = datos[2]

                    # Imprimo el producto usando el formato solicitado por el enunciado.
                    # Uso una f-string para insertar las variables en la cadena fácilmente.
                    # Uso :.2f en precio para asegurar dos decimales.
                    print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")
                else:
                    # Coloco un mensaje de advertencia si encuentro una línea con formato incorrecto.
                    print(f"Advertencia: Línea con formato incorrecto encontrada: {linea_limpia}")

    # Este bloque try-except me sirve para manejar el error si el archivo no existe
    # cuando el programa intenta abrirlo en modo lectura.
    except FileNotFoundError:
        print("Error: El archivo 'productos.txt' no se encontró. Asegúrate de haber ejecutado el paso 1.")

# Ejecuto la función para ver el listado de productos.
leer_y_mostrar_productos()






#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente.

# Coloco esta función para crear y poblar el archivo 'productos.txt'
# con los datos iniciales, asegurando que siempre tengamos un archivo base.
def crear_archivo_inicial():
    # Uso el modo 'w' para sobrescribir o crear el archivo.
    with open('productos.txt', 'w') as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno A4,850.0,15\n")
        archivo.write("Resaltador,95.75,50\n")
    print("Archivo 'productos.txt' asegurado con datos iniciales.")

# Coloco la función para leer y mostrar los productos (Paso 2).
def leer_y_mostrar_productos():
    print("\n--- Listado de Productos Actual ---")
    try:
        with open('productos.txt', 'r') as archivo:
            # Uso esta bandera para saber si se procesó al menos un producto.
            productos_encontrados = False
            for linea in archivo:
                linea_limpia = linea.strip()
                datos = linea_limpia.split(',')

                if len(datos) == 3:
                    nombre = datos[0]
                    # Intento convertir el precio y la cantidad para mostrarlos correctamente.
                    try:
                        precio = float(datos[1])
                        cantidad = int(datos[2])
                        print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")
                        productos_encontrados = True
                    except ValueError:
                        print(f"Advertencia: Error al convertir precio o cantidad en la línea: {linea_limpia}")
                
            if not productos_encontrados:
                print("No hay productos registrados en el archivo.")

    except FileNotFoundError:
        print("Error: El archivo 'productos.txt' no se encontró.")

# Esta es la función principal para el Paso 3: Agregar desde el teclado.
def agregar_producto_desde_teclado():
    print("\n--- Agregar Nuevo Producto ---")

    # Pido al usuario que ingrese los datos requeridos: nombre, precio y cantidad.
    # Uso input() y strip() para limpiar cualquier espacio sobrante.
    nombre_nuevo = input("Ingresa el nombre del nuevo producto: ").strip()
    precio_nuevo = input("Ingresa el precio: ").strip()
    cantidad_nueva = input("Ingresa la cantidad: ").strip()

    # Construyo la cadena de texto con el formato que usa el archivo: nombre,precio,cantidad.
    # Es crucial agregar '\n' al final para que el nuevo producto empiece en una
    # línea nueva en el archivo, evitando que se pegue al producto anterior.
    nuevo_registro = f"{nombre_nuevo},{precio_nuevo},{cantidad_nueva}\n"

    # Uso 'with open' en modo 'a' (append/agregar).
    # Este modo me permite escribir al final del archivo sin borrar lo que ya existía,
    # que es el requisito principal de esta actividad.
    try:
        with open('productos.txt', 'a') as archivo:
            # Escribo el registro en el archivo.
            archivo.write(nuevo_registro)
        print(f"Producto '{nombre_nuevo}' agregado correctamente al archivo.")

    except Exception as e:
        # Coloco un manejo de error general por si ocurre algún problema en la escritura.
        print(f"Ocurrió un error al intentar agregar el producto: {e}")


# --- Flujo principal del programa para demostrar el paso 3 ---

# 1. Aseguro el archivo inicial (para tener los 3 productos base).
crear_archivo_inicial()

# 2. Leo y muestro los productos actuales antes de agregar.
leer_y_mostrar_productos()

# 3. Pido y agrego un nuevo producto.
agregar_producto_desde_teclado()

# 4. Leo y muestro los productos de nuevo para confirmar que el nuevo
#    producto se haya agregado al final del listado.
leer_y_mostrar_productos()






#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

# Coloco esta función para crear y poblar el archivo 'productos.txt'
# con los datos iniciales, asegurando que siempre tengamos un archivo base.
def crear_archivo_inicial():
    # Uso el modo 'w' para sobrescribir o crear el archivo.
    with open('productos.txt', 'w') as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno A4,850.0,15\n")
        archivo.write("Resaltador,95.75,50\n")
    print("Archivo 'productos.txt' asegurado con datos iniciales.")


# Esta es la nueva función principal para el Paso 4. Ahora se encarga de
# leer el archivo y construir la lista de diccionarios.
def cargar_productos_en_lista():
    # Inicializo la lista vacía que contendrá todos los diccionarios de productos.
    lista_productos = []
    print("\n--- Cargando productos desde archivo a lista de diccionarios ---")

    # Uso 'with open' en modo lectura ('r').
    try:
        with open('productos.txt', 'r') as archivo:
            # Recorro cada línea del archivo, como en el paso anterior.
            for linea in archivo:
                linea_limpia = linea.strip()
                datos = linea_limpia.split(',')

                # Verifico que la línea tenga 3 datos válidos.
                if len(datos) == 3:
                    try:
                        # Extraigo y convierto los datos a sus tipos correspondientes:
                        # nombre (str), precio (float), cantidad (int).
                        nombre = datos[0]
                        precio = float(datos[1])
                        cantidad = int(datos[2])

                        # Creo un diccionario para el producto actual con las claves solicitadas.
                        producto = {
                            'nombre': nombre,
                            'precio': precio,
                            'cantidad': cantidad
                        }
                        
                        # Agrego el diccionario a mi lista principal.
                        lista_productos.append(producto)

                    except ValueError:
                        # Si la conversión a float o int falla, solo muestro una advertencia
                        # y sigo con la siguiente línea.
                        print(f"Advertencia: Error de formato (precio/cantidad) en la línea: {linea_limpia}. Saltando registro.")
                
                else:
                    print(f"Advertencia: Línea con formato incorrecto (no 3 campos) encontrada: {linea_limpia}. Saltando registro.")

    except FileNotFoundError:
        print("Error: El archivo 'productos.txt' no se encontró. Retornando lista vacía.")
        return [] # Si hay error, devuelvo una lista vacía para no romper el programa.

    print(f"Se cargaron {len(lista_productos)} productos a la lista en memoria.")
    # Al final, retorno la lista de diccionarios que acabamos de construir.
    return lista_productos


# Función auxiliar para mostrar la lista cargada (similar al paso 2, pero usando la lista).
def mostrar_productos_cargados(productos):
    print("\n--- Contenido de la Lista de Diccionarios (Verificación) ---")
    if not productos:
        print("La lista de productos está vacía.")
        return
        
    for p in productos:
        # Muestro el producto usando las claves del diccionario.
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}")


# --- Flujo principal del programa para demostrar el paso 4 ---

# 1. Aseguro el archivo inicial.
crear_archivo_inicial()

# 4. Cargo los productos del archivo en la lista de diccionarios.
productos_en_memoria = cargar_productos_en_lista()

# Muestro el contenido de la lista para verificar que la carga fue exitosa.
mostrar_productos_cargados(productos_en_memoria)





#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error.

# Coloco esta función para crear y poblar el archivo 'productos.txt'.
def crear_archivo_inicial():
    # Uso el modo 'w' para sobrescribir o crear el archivo.
    with open('productos.txt', 'w') as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno A4,850.0,15\n")
        archivo.write("Resaltador,95.75,50\n")
    print("Archivo 'productos.txt' asegurado con datos iniciales.")


# Coloco la función del Paso 4 para cargar los datos del archivo en una lista de diccionarios.
# Esta función es crucial, ya que la usaremos para la búsqueda.
def cargar_productos_en_lista():
    lista_productos = []
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                datos = linea_limpia.split(',')

                if len(datos) == 3:
                    try:
                        nombre = datos[0]
                        precio = float(datos[1])
                        cantidad = int(datos[2])

                        producto = {
                            'nombre': nombre,
                            'precio': precio,
                            'cantidad': cantidad
                        }
                        lista_productos.append(producto)

                    except ValueError:
                        print(f"Advertencia: Error de formato (precio/cantidad) en la línea: {linea_limpia}. Saltando registro.")

    except FileNotFoundError:
        print("Error: El archivo 'productos.txt' no se encontró. Retornando lista vacía.")
        return []

    return lista_productos


# Esta es la nueva función principal para el Paso 5: Buscar.
def buscar_producto_por_nombre(productos):
    print("\n--- Buscar Producto ---")
    
    # Primero, verifico si la lista de productos está vacía. Si lo está, no puedo buscar nada.
    if not productos:
        print("Error: No hay productos cargados en la lista para realizar la búsqueda.")
        return

    # Pido al usuario el nombre del producto que quiere buscar.
    # Uso .strip() para limpiar el nombre y .lower() para estandarizar la búsqueda a minúsculas
    # y así hacerla menos sensible a mayúsculas y minúsculas.
    nombre_buscado = input("Ingresa el nombre del producto a buscar: ").strip().lower()

    # Uso esta bandera para saber si encontré el producto.
    encontrado = False

    # Recorro la lista de diccionarios que me pasaron como argumento.
    for producto in productos:
        # Comparo el nombre buscado con el nombre del producto actual,
        # también convertido a minúsculas.
        if producto['nombre'].lower() == nombre_buscado:
            # Si lo encuentro, muestro todos sus datos.
            print("\nProducto encontrado:")
            print(f"  Nombre: {producto['nombre']}")
            print(f"  Precio: ${producto['precio']:.2f}")
            print(f"  Cantidad: {producto['cantidad']}")
            encontrado = True
            # Como solo necesito encontrar el primer resultado, uso break para salir del bucle.
            break

    # Si el bucle termina y la bandera 'encontrado' sigue siendo False, significa que no existe.
    if not encontrado:
        print(f"\nError: El producto con nombre '{nombre_buscado.capitalize()}' no existe en el inventario.")


# --- Flujo principal del programa para demostrar el paso 5 ---

# 1. Aseguro el archivo inicial.
crear_archivo_inicial()

# 4. Cargo los productos en la lista de diccionarios (preparación para el paso 5).
productos_en_memoria = cargar_productos_en_lista()

# 5. Ejecuto la búsqueda del producto.
buscar_producto_por_nombre(productos_en_memoria)






#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

# Coloco esta función para crear y poblar el archivo 'productos.txt'
# (Se mantiene para asegurar un estado inicial).
def crear_archivo_inicial():
    with open('productos.txt', 'w') as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno A4,850.0,15\n")
        archivo.write("Resaltador,95.75,50\n")
    print("Archivo 'productos.txt' asegurado con datos iniciales.")

# Coloco la función del Paso 4 para cargar los datos del archivo en una lista de diccionarios.
# Esta lista es la que vamos a guardar.
def cargar_productos_en_lista():
    lista_productos = []
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                datos = linea_limpia.split(',')

                if len(datos) == 3:
                    try:
                        nombre = datos[0]
                        precio = float(datos[1])
                        cantidad = int(datos[2])

                        producto = {
                            'nombre': nombre,
                            'precio': precio,
                            'cantidad': cantidad
                        }
                        lista_productos.append(producto)
                    except ValueError:
                        pass # Ignoro líneas con formato incorrecto.
    except FileNotFoundError:
        return []
    return lista_productos

# Coloco la función para agregar un producto a la lista (Paso 3, modificado para trabajar con la lista).
# En un programa real, agregaríamos a la lista, no directamente al archivo.
# Para la demostración, agrego a la lista y luego lo guardamos en el archivo.
def agregar_producto_a_lista(productos):
    print("\n--- Agregar Nuevo Producto ---")
    nombre_nuevo = input("Ingresa el nombre del nuevo producto: ").strip()
    
    # Coloco un bucle para asegurar que el precio sea un número válido.
    while True:
        try:
            precio_nuevo = float(input("Ingresa el precio: ").strip())
            break
        except ValueError:
            print("El precio debe ser un número. Inténtalo de nuevo.")
            
    # Coloco un bucle para asegurar que la cantidad sea un número entero válido.
    while True:
        try:
            cantidad_nueva = int(input("Ingresa la cantidad: ").strip())
            break
        except ValueError:
            print("La cantidad debe ser un número entero. Inténtalo de nuevo.")

    # Creo el diccionario y lo añado a la lista que recibimos.
    nuevo_producto = {
        'nombre': nombre_nuevo,
        'precio': precio_nuevo,
        'cantidad': cantidad_nueva
    }
    productos.append(nuevo_producto)
    print(f"Producto '{nombre_nuevo}' agregado a la lista en memoria.")

# Función auxiliar para mostrar la lista (para verificación).
def mostrar_productos_cargados(productos):
    print("\n--- Contenido Actual del Inventario ---")
    if not productos:
        print("La lista de productos está vacía.")
        return
        
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}")


# Esta es la nueva función principal para el Paso 6: Guardar los datos actualizados.
def guardar_productos_actualizados(productos):
    # Uso 'with open' en modo 'w' (write/escritura).
    # Este modo es fundamental porque BORRA todo el contenido previo del archivo
    # y lo sobrescribe con lo nuevo. Así se garantiza que solo la lista actualizada
    # quede grabada, cumpliendo con la idea de "actualizar".
    print("\n--- Guardando cambios en el archivo 'productos.txt' ---")
    try:
        with open('productos.txt', 'w') as archivo:
            # Recorro cada diccionario dentro de la lista de productos que está en memoria.
            for producto in productos:
                # Creo la cadena con el formato "nombre,precio,cantidad" + salto de línea (\n).
                # Uso str() para asegurar que los números se conviertan a texto antes de escribir.
                registro = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(registro)
        print(f"Éxito: Se guardaron {len(productos)} registros en el archivo 'productos.txt'.")
    
    except Exception as e:
        print(f"Error al intentar guardar los productos: {e}")


# --- Flujo principal completo para demostrar los pasos 4, 3 y 6 ---

# 1. Aseguro el archivo inicial.
crear_archivo_inicial()

# 4. Cargo los productos del archivo en la lista de diccionarios.
productos_en_memoria = cargar_productos_en_lista()

# Muestro los productos antes del cambio.
mostrar_productos_cargados(productos_en_memoria)

# 3. Agrego un nuevo producto a la lista en memoria.
agregar_producto_a_lista(productos_en_memoria)

# Muestro la lista con el nuevo producto (aún no está en el archivo).
mostrar_productos_cargados(productos_en_memoria)

# 6. Guardo la lista completa (los 3 originales + el nuevo) en el archivo,
#    sobrescribiendo el contenido previo y haciendo el cambio permanente.
guardar_productos_actualizados(productos_en_memoria)

# OPCIONAL: Recargo la lista desde el archivo para confirmar que el nuevo
# registro esté realmente guardado.
productos_recargados = cargar_productos_en_lista()
mostrar_productos_cargados(productos_recargados)