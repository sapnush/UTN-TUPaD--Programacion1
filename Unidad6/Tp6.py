# Trbajo Practico n 6 Funciones

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 1
# =================================================================

# Defino mi función. No necesita parámetros.
def imprimir_hola_mundo():
    # Imprimo el mensaje solicitado directamente en la consola.
    print("Hola Mundo!")


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Llamo a la función para que se ejecute e imprima el mensaje.
imprimir_hola_mundo()




#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 2
# =================================================================

# Defino mi función y le digo que espera un parámetro llamado 'nombre'.
def saludar_usuario(nombre):
    # Construyo el saludo usando una f-string para personalizarlo.
    saludo = f"Hola {nombre}!"
    
    # Retorno el saludo completo al lugar donde se llamó la función.
    return saludo


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido el nombre al usuario y lo guardo en una variable.
nombre_ingresado = input("Por favor, ingresa tu nombre: ")

# Llamo a mi función, pasando el nombre ingresado.
# Guardo el resultado retornado en una variable.
saludo_final = saludar_usuario(nombre_ingresado)

# Imprimo el resultado final.
print(saludo_final)




# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 3
# =================================================================

# Defino mi función con los cuatro parámetros solicitados.
def informacion_personal(nombre, apellido, edad, residencia):
    # Imprimo toda la información usando una f-string para formatear.
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido cada uno de los datos al usuario.
mi_nombre = input("Ingresa tu nombre: ")
mi_apellido = input("Ingresa tu apellido: ")
mi_edad = input("Ingresa tu edad: ")
mi_residencia = input("Ingresa tu residencia: ")

# Llamo a mi función con todos los datos ingresados por el usuario.
informacion_personal(mi_nombre, mi_apellido, mi_edad, mi_residencia)





#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_peri-
#metro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar am-
#bas funciones para mostrar los resultados.

import math # Importo la librería 'math' para poder usar el valor exacto de Pi

# =================================================================
# DEFINICIÓN DE LAS FUNCIONES 4
# =================================================================

# Defino la función para calcular el área (Pi * radio^2).
def calcular_area_circulo(radio):
    # Retorno el área: math.pi multiplicado por el radio al cuadrado.
    return math.pi * (radio ** 2)

# Defino la función para calcular el perímetro (2 * Pi * radio).
def calcular_perimetro_circulo(radio):
    # Retorno el perímetro.
    return 2 * math.pi * radio


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido el radio al usuario y lo convierto a flotante, ya que Pi es decimal.
radio_ingresado = float(input("Ingresa el radio del círculo: "))

# Llamo a la función de área.
area = calcular_area_circulo(radio_ingresado)

# Llamo a la función de perímetro.
perimetro = calcular_perimetro_circulo(radio_ingresado)

# Imprimo ambos resultados, redondeando para que se vean mejor.
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")





#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 5
# =================================================================

# Defino mi función para convertir segundos a horas.
# Hay 3600 segundos en una hora.
def segundos_a_horas(segundos):
    # Retorno el resultado de dividir los segundos por 3600.
    return segundos / 3600


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido los segundos al usuario y lo convierto a entero.
segundos_ingresados = int(input("Ingresa la cantidad de segundos a convertir: "))

# Llamo a la función y guardo el resultado.
horas_calculadas = segundos_a_horas(segundos_ingresados)

# Imprimo el resultado, usando dos decimales para mayor claridad.
print(f"{segundos_ingresados} segundos equivalen a {horas_calculadas:.2f} horas.")





#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 6
# =================================================================

# Defino mi función que recibe el 'numero' del que quiero la tabla.
def tabla_multiplicar(numero):
    # Uso un bucle 'for' para iterar desde 1 hasta 10 (range(1, 11)).
    for i in range(1, 11):
        # Calculo el resultado de la multiplicación.
        resultado = numero * i
        # Imprimo cada línea de la tabla de forma clara.
        print(f"{numero} x {i} = {resultado}")


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido el número al usuario y lo convierto a entero.
num_ingresado = int(input("Ingresa el número del que quieres la tabla de multiplicar: "))

# Llamo a la función.
tabla_multiplicar(num_ingresado)





#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resulta-
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 7
# =================================================================

# Defino mi función que recibe dos números, 'a' y 'b'.
def operaciones_basicas(a, b):
    # Calculo cada una de las cuatro operaciones.
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Hago una verificación simple para evitar la división por cero.
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
        
    # Retorno los cuatro resultados juntos como una tupla.
    return (suma, resta, multiplicacion, division)


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido los dos números al usuario y los convierto a flotantes para manejar la división.
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Llamo a mi función. Desempaqueto la tupla retornada en variables separadas.
s, r, m, d = operaciones_basicas(num1, num2)

# Imprimo los resultados de forma clara.
print(f"\nResultados de las operaciones básicas:")
print(f"Suma: {s}")
print(f"Resta: {r}")
print(f"Multiplicación: {m}")
print(f"División: {d}")





#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 8
# =================================================================

# Defino mi función con los parámetros 'peso' y 'altura'.
# La fórmula es: IMC = peso / altura^2.
def calcular_imc(peso, altura):
    # Calculo el IMC. Uso '** 2' para el cuadrado de la altura.
    imc = peso / (altura ** 2)
    # Retorno el resultado.
    return imc


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido el peso y la altura, convirtiéndolos a flotantes.
peso_kg = float(input("Ingresa tu peso en kilogramos (ej: 75.5): "))
altura_m = float(input("Ingresa tu altura en metros (ej: 1.78): "))

# Llamo a mi función para obtener el IMC.
imc_resultado = calcular_imc(peso_kg, altura_m)

# Imprimo el resultado, asegurándome de usar dos decimales como se pide.
print(f"\nTu Índice de Masa Corporal (IMC) es: {imc_resultado:.2f}")





#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 9
# =================================================================

# Defino mi función para convertir Celsius a Fahrenheit.
# La fórmula es: F = C * 9/5 + 32.
def celsius_a_fahrenheit(celsius):
    # Aplico la fórmula matemática.
    fahrenheit = (celsius * 9/5) + 32
    # Retorno el valor en Fahrenheit.
    return fahrenheit


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido la temperatura en Celsius y la convierto a flotante.
temp_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Llamo a la función para hacer la conversión.
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

# Imprimo el resultado de la conversión.
print(f"\n{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F.")





#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

# =================================================================
# DEFINICIÓN DE LA FUNCIÓN 10
# =================================================================

# Defino mi función para calcular el promedio de tres números.
def calcular_promedio(a, b, c):
    # Calculo la suma de los tres números y la divido por 3.
    promedio = (a + b + c) / 3
    # Retorno el promedio.
    return promedio


# =================================================================
# PROGRAMA PRINCIPAL
# =================================================================

# Pido los tres números al usuario. Los convierto a flotantes para un promedio preciso.
num_a = float(input("Ingresa el primer número: "))
num_b = float(input("Ingresa el segundo número: "))
num_c = float(input("Ingresa el tercer número: "))

# Llamo a mi función con los tres números ingresados.
promedio_final = calcular_promedio(num_a, num_b, num_c)

# Imprimo el promedio final con dos decimales.
print(f"\nEl promedio de los tres números es: {promedio_final:.2f}")


