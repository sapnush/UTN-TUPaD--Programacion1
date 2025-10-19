# ------------------------------------------
# PRIMER PARCIAL - PROGRAMACIÓN 1
# Sistema de gestión de biblioteca escolar
# ------------------------------------------

# Listas paralelas para títulos y ejemplares
titulos = []
ejemplares = []

opcion = 0

# Bucle principal del menú
while opcion != 8:
    print ("\n=== SISTEMA DE BIBLIOTECA ESCOLAR ===")
    print ("1. Cargar títulos iniciales")
    print ("2. Cargar cantidad de ejemplares")
    print ("3. Ver catálogo completo")
    print ("4. Consultar ejemplares de un libro")
    print ("5. Ver libros agotados")
    print ("6. Agregar un nuevo libro al catálogo")
    print ("7. Registrar préstamo o devolución")
    print ("8. Salir del sistema")

    # Pedir opción al usuario
    opcion = input("Ingresa el número de la opción deseada: ")

    # Validación: opción debe ser un número
    if opcion.isdigit():
        opcion = int (opcion)
    else:
        print ("Error, ingresa un número válido.")
        opcion = 0

    # Opción 1: ingresar títulos
    if opcion == 1:
        cant = input ("¿Cuántos libros distintos desea cargar?: ")
        if cant.isdigit():
            cant = int (cant)
            for i in range(cant):
                titulo = input(f"Ingresa el título del libro {i+1}: ").strip()
                while titulo == "":
                    titulo = input ("Título vacío. Ingrese de nuevo: ").strip()
                titulos.append(titulo)
                ejemplares.append(0)  # Inicialmente sin stock
        else:
            print("Error, ingresa un número válido.")

    # Opción 2: ingresar ejemplares
    elif opcion == 2:
        if len(titulos) == 0:
            print("Todavía no cargó ningún título.")
        else:
            for i in range (len(titulos)):
                cantidad = input(f"¿Cuántos ejemplares tiene de '{titulos[i]}'?: ")
                while not cantidad.isdigit() or int(cantidad) < 0:
                    cantidad = input ("La cantidad debe ser un número entero mayor o igual a 0. Intente nuevamente: ")
                ejemplares[i] = int(cantidad)

    # Opción 3: mostrar catálogo
    elif opcion == 3:
        if len (titulos) == 0:
            print ("No hay libros en el catalogo.")
        else:
            print ("\n--- CATÁLOGO DE LIBROS ---")
            for i in range(len(titulos)):
                print (f"{i+1}. {titulos[i]} → {ejemplares[i]} ejemplares disponibles")

    # Opción 4: consultar disponibilidad de un título
    elif opcion == 4:
        titulo_buscar = input ("Título del libro que busca: ").strip()
        if titulo_buscar in titulos:
            indice = titulos.index(titulo_buscar)
            print(f"El libro '{titulos[indice]}' tiene {ejemplares[indice]} ejemplares disponibles.")
        else:
            print("No contamos con ese vlibro en el catálogo.")

    # Opción 5: listar libros agotados
    elif opcion == 5:
        agotados = False
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(f"El libro '{titulos[i]}' está agotado.")
                agotados = True
        if not agotados:
            print("Por el momento, no hay libros agotados.")

    # Opción 6: agregar un nuevo título
    elif opcion == 6:
        nuevo_titulo = input("Ingrese el título del nuevo libro: ").strip()
        while nuevo_titulo == "":
            nuevo_titulo = input("El título no puede estar vacío. Ingrese nuevamente: ").strip()
        if nuevo_titulo in titulos:
            print("Ese libro ya existe en el catálogo.")
        else:
            cant = input(f"Ingrese la cantidad de ejemplares para '{nuevo_titulo}': ")
            while not cant.isdigit() or int(cant) < 0:
                cant = input("La cantidad debe ser un número entero mayor o igual a 0. Repita elñ intento: ")
            titulos.append(nuevo_titulo)
            ejemplares.append(int(cant))
            print(f"Se agregó el libro '{nuevo_titulo}' con {cant} ejemplares.")

    # Opción 7: actualizar ejemplares (préstamo o devolución)
    elif opcion == 7:
        if len(titulos) == 0:
            print("El catálogo está vacío.")
        else:
            titulo_mod = input("Cual es el título del libro que quiere actualizar: ").strip()
            if titulo_mod in titulos:
                indice = titulos.index(titulo_mod)
                print("Seleccione la acción:")
                print("1. Registrar un préstamo")
                print("2. Registrar una devolución")
                accion = input("Ingrese 1 o 2: ")

                if accion == "1":
                    if ejemplares[indice] > 0:
                        ejemplares[indice] -= 1
                        print(f"Se registró un préstamo de '{titulos[indice]}'. Ahora quedan {ejemplares[indice]} ejemplares.")
                    else:
                        print("No hay libros para prestar")
                elif accion == "2":
                    ejemplares[indice] += 1
                    print(f"Se registró una devolución de '{titulos[indice]}'. Ahora hay {ejemplares[indice]} ejemplares.")
                else:
                    print("Error,.")
            else:
                print("Título inexistenyte.")

    # Opción 8: salir
    elif opcion == 8:
        print("Gracias por utilizar el sistema de gestion de la biblioteca escolar. Adios!")

    # Opción inválida
    elif opcion != 0:
        print("Error, intente de nuevo.")