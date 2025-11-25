# GESTOR DE DATOS DE PAÍSES EN PYTHON

## Trabajo Práctico Integrador | Programación 1

Autora: Sabina Perez

***

## 📖 Descripción del Proyecto

Aplicación de consola desarrollada en Python para la **gestión y análisis de datos geográficos y demográficos de países**.

El sistema cumple con las consignas del TPI de Programación 1, leyendo información inicial desde un archivo CSV y ofreciendo un menú interactivo con 8 funcionalidades clave que demuestran el uso de **listas de diccionarios**, **modularización con funciones**, **control de flujo** y **manejo de errores**.

***

## 🚀 Requisitos y Ejecución

### 1. Requisitos

Se necesita tener instalado **Python 3.x** en el sistema operativo. El proyecto utiliza únicamente librerías estándar (`csv` y `os`), por lo que no es necesario instalar paquetes adicionales.

### 2. Archivos

Asegúrate de que los dos archivos principales se encuentren en la **misma carpeta**:
* `tpi_gestion_paises.py` (el código fuente).
* `paises.csv` (el dataset base).

### 3. Ejecución

Para iniciar el programa, abre tu terminal o Símbolo del Sistema, navega hasta la carpeta del proyecto y ejecuta el siguiente comando:

```bash
python tpi_gestion_paises

Funcionalidades Implementadas
La aplicación presenta un menú interactivo con 8 opciones:
1. Agregar país: Permite ingresar un nuevo país y valida los datos numéricos.

2. Actualizar datos: Modifica los valores de población y superficie de un país existente.

3. Buscar país: Realiza una búsqueda flexible por nombre (parcial o completo).

4. Filtrar países: Permite filtrar los países por continente o por rango numérico (población o superficie).

5. Ordenar lista: Ordena la lista por Nombre, Población (descendente) o Superficie (descendente).

6. Mostrar Estadísticas: Calcula y muestra la población total, superficie promedio y el conteo de países por continente.

7. Listar todos: Muestra todos los países cargados en formato tabular.

8. Salir: Finaliza la ejecución del programa.

Ejemplo de entrada y salida. Opcion 4: filtrar
> Ingrese el número de la opción deseada: 4

--- FILTROS DE PAÍSES ---
1. Filtrar por Continente
2. Filtrar por Rango Numérico (Población o Superficie)
3. Volver al menú principal
Ingrese la opción deseada (1, 2 o 3): 2

--- FILTRAR POR RANGO ---
1. Filtrar por Población
2. Filtrar por Superficie
Seleccione el criterio (1 o 2): 1
Ingrese el valor mínimo para poblacion: 100000000
Ingrese el valor máximo para poblacion: 300000000

Se encontraron 2 resultados.

   Continente         Nombre       Población  Superficie (km²)
----------------------------------------------------------------------
      Asia          Japón       125,800,000      377,975
     América        Brasil      213,993,437    8,515,767
----------------------------------------------------------------------