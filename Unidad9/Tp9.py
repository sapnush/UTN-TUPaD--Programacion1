#------------- TP RECURSIVIDAD --------------
# Estudiante: Sabina Perez

#Consignas y resolusion:

#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def calcular_factorial(n):
    # Primero, defino el caso base de la recursión.
    # El factorial de 0 o 1 es 1, esto detiene la cadena de llamadas recursivas.
    if n == 0 or n == 1:
        return 1
    
    # Este es el paso recursivo. Para calcular el factorial de 'n',
    # multiplico 'n' por el factorial del número anterior (n-1).
    # La función se llama a sí misma con un argumento más pequeño, acercándome al caso base.
    return n * calcular_factorial(n - 1)

def main_ejercicio_1():
    # Pido al usuario que ingrese el número límite.
    # Me aseguro de que el dato ingresado sea un entero.
    while True:
        try:
            limite = int(input("Ingresa un número entero positivo para calcular el factorial hasta él: "))
            # Verifico que el número sea positivo, como se espera para el factorial.
            if limite < 0:
                print("Por favor, ingresa un número entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f"\nCalculando el factorial de los números enteros entre 1 y {limite}:")
    
    # Uso un bucle 'for' para iterar desde 1 hasta el número ingresado por el usuario,
    # incluyendo el 'limite' (por eso uso 'limite + 1' en el range).
    for i in range(1, limite + 1):
        # Llamo a la función recursiva para calcular el factorial de 'i'.
        resultado = calcular_factorial(i)
        # Muestro el resultado en la pantalla de forma clara.
        print(f"El factorial de {i} ({i}!) es: {resultado}")

# Llamo a la función principal para ejecutar el algoritmo.
main_ejercicio_1()





#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def fibonacci_recursivo(posicion):
    # Primero, defino los casos base. Estos son los primeros dos números de la serie 
    # y son cruciales porque detienen la recursión.
    if posicion <= 0:
        # F(0) = 0
        return 0
    elif posicion == 1:
        # F(1) = 1
        return 1
    
    # Este es el paso recursivo. Para obtener el número en la posición actual, 
    # sumo los resultados de las dos posiciones anteriores.
    # La función se llama a sí misma dos veces, descomponiendo el problema.
    return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

def main_ejercicio_2():
    # Pido al usuario que ingrese la posición límite para generar la serie.
    while True:
        try:
            limite = int(input("Ingresa la posición máxima (un número entero no negativo) para mostrar la serie de Fibonacci: "))
            # Verifico que el número sea no negativo, ya que las posiciones de la serie comienzan en 0.
            if limite < 0:
                print("Por favor, ingresa un número entero positivo o cero.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f"\nGenerando la serie de Fibonacci hasta la posición {limite}:")
    
    # Coloco una lista para guardar los elementos de la serie.
    serie_fibonacci = []
    
    # Itero desde la posición 0 hasta la posición límite (incluida).
    for i in range(limite + 1):
        # Llamo a la función recursiva para calcular el valor en cada posición 'i'.
        valor_fib = fibonacci_recursivo(i)
        # Guardo el valor en la lista.
        serie_fibonacci.append(valor_fib)
        
    # Muestro la serie completa en pantalla.
    print("Serie:", serie_fibonacci)
    # También muestro el valor de la posición límite, que es el último elemento calculado.
    print(f"El valor de la serie de Fibonacci en la posición {limite} es: {valor_fib}")

# Llamo a la función principal para ejecutar el algoritmo.
main_ejercicio_2()





#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula n^m = n ∗ n^(m−1). Prueba esta función en un algoritmo general.

def calcular_potencia(base, exponente):
    # Primero, manejo los casos de exponente no negativo, que son los más comunes.
    
    # Este es el caso base. La recursión debe detenerse cuando el exponente llega a 0.
    # Cualquier número elevado a 0 es 1.
    if exponente == 0:
        return 1
    
    # Este es el paso recursivo. Para calcular la potencia, multiplico la 'base' 
    # por el resultado de la función llamándose a sí misma, pero con el 'exponente' reducido en 1.
    # Esto sigue la fórmula: n^m = n * n^(m-1).
    if exponente > 0:
        return base * calcular_potencia(base, exponente - 1)
        
    # Coloque este bloque opcional para manejar exponentes negativos, aunque la fórmula 
    # se centra en el caso positivo. Si el exponente es negativo, se aplica la propiedad
    # n^(-m) = 1 / n^m.
    # Uso la recursión sobre el exponente positivo y luego tomo el inverso.
    if exponente < 0:
        # Uso 'abs(exponente)' para obtener el exponente positivo y hago la llamada recursiva.
        resultado_positivo = calcular_potencia(base, abs(exponente))
        # Devuelvo 1 dividido por el resultado positivo.
        return 1 / resultado_positivo

def main_ejercicio_3():
    # Pido la base al usuario.
    while True:
        try:
            base = float(input("Ingresa la base (un número cualquiera): "))
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número para la base.")

    # Pido el exponente al usuario.
    while True:
        try:
            exponente = int(input("Ingresa el exponente (un número entero): "))
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero para el exponente.")

    # Llamo a la función recursiva para obtener el resultado.
    resultado = calcular_potencia(base, exponente)

    # Muestro el resultado en un formato claro.
    # Uso f-string para mostrar la operación y el resultado.
    print(f"\nEl resultado de {base} elevado a la potencia {exponente} es: {resultado}")
    
# Llamo a la función principal para probar el algoritmo.
main_ejercicio_3()

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario_recursivo(decimal):
    # Primero, defino el caso base de la recursión.
    # Si el número decimal llega a 0, ya no hay más divisiones ni más bits que generar, 
    # por lo que devuelvo una cadena vacía para que la concatenación pueda empezar.
    if decimal == 0:
        return ""

    # Este es el paso recursivo.
    
    # 1. Calculo el cociente de la división entera por 2 (decimal // 2). 
    # Llamo a la función recursivamente con este cociente. Esto genera los bits más significativos 
    # (los de la izquierda) primero, porque se resuelven las llamadas anidadas primero (fondo de la pila).
    resto_de_llamada = decimal_a_binario_recursivo(decimal // 2)
    
    # 2. Calculo el resto de la división por 2 (decimal % 2). Este resto es el bit binario actual.
    # El resto debe ser convertido a string para poder concatenarlo.
    bit_actual = str(decimal % 2)
    
    # 3. Concateno el resultado de la llamada recursiva (los bits anteriores) con el bit actual.
    # Al leer los restos desde "el último" que se genera (el de la última llamada) 
    # y que se concatena primero, se arma el número binario en el orden correcto (de izquierda a derecha).
    return resto_de_llamada + bit_actual

def main_ejercicio_4():
    # Pido al usuario el número decimal a convertir.
    while True:
        try:
            decimal = int(input("Ingresa un número entero positivo en base decimal para convertir a binario: "))
            # Verifico que el número sea positivo, como se especifica en el enunciado.
            if decimal < 0:
                print("Por favor, ingresa un número entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    # Manejo el caso especial donde el usuario ingresa 0, ya que el caso base devuelve "".
    if decimal == 0:
        binario = "0"
    else:
        # Llamo a la función recursiva.
        binario = decimal_a_binario_recursivo(decimal)

    # Muestro el resultado en pantalla.
    print(f"\nEl número decimal {decimal} es igual al binario: {binario}")

# Llamo a la función principal para ejecutar el algoritmo.
main_ejercicio_4()





#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    # La función debe recibir la palabra sin espacios ni tildes, asumo que esto se maneja 
    # antes de llamar a la función, pero la lógica de la recursión es la siguiente:

    # 1. Caso Base: La recursión se detiene si la palabra tiene 0 o 1 carácter.
    # En ambos casos, es considerada un palíndromo.
    if len(palabra) <= 1:
        return True

    # 2. Caso de No Palíndromo (Fallo): Compruebo si el primer carácter es diferente al último.
    # Si son diferentes, no es un palíndromo, y retorno False inmediatamente.
    # [0] es el primer carácter y [-1] es el último.
    if palabra[0] != palabra[-1]:
        return False

    # 3. Paso Recursivo: Si los caracteres coinciden, llamo a la función de nuevo con una
    # subcadena que excluye el primer y el último carácter. 
    # [1:-1] crea una nueva cadena que va desde el índice 1 (el segundo carácter) 
    # hasta el índice -1 (el penúltimo carácter), excluyendo los extremos.
    return es_palindromo(palabra[1:-1])

def main_ejercicio_5():
    print("--- Prueba de Palíndromos ---")
    
    # Coloque un ejemplo de una palabra que sea palíndromo.
    palabra_1 = "reconocer"
    print(f"'{palabra_1}': {es_palindromo(palabra_1)}") # Resultado esperado: True

    # Coloque un ejemplo de una palabra que NO sea palíndromo.
    palabra_2 = "algoritmo"
    print(f"'{palabra_2}': {es_palindromo(palabra_2)}") # Resultado esperado: False
    
    # Coloque un ejemplo de una palabra con un número par de caracteres.
    palabra_3 = "abba"
    print(f"'{palabra_3}': {es_palindromo(palabra_3)}") # Resultado esperado: True

    # Coloque un ejemplo de una palabra con un número impar de caracteres.
    palabra_4 = "ojo"
    print(f"'{palabra_4}': {es_palindromo(palabra_4)}") # Resultado esperado: True

    # Para ser riguroso con los requisitos, simulo la limpieza de entrada (aunque el enunciado 
    # asume que la entrada ya viene limpia).
    entrada_usuario = input("\nIngresa una palabra (sin espacios ni tildes): ")
    # Podría convertir a minúsculas aquí para una verificación más robusta.
    entrada_limpia = entrada_usuario.lower() 
    
    resultado_final = es_palindromo(entrada_limpia)
    print(f"La palabra '{entrada_usuario}' ¿es palíndromo?: {resultado_final}")

# Llamo a la función principal para ejecutar las pruebas.
main_ejercicio_5()





#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    # Asumo que 'n' es un número entero positivo según el enunciado.

    # 1. Caso Base: Si el número es de un solo dígito (es decir, n < 10), 
    # la recursión se detiene y ese dígito es el último que queda por sumar.
    if n < 10:
        return n
    
    # 2. Paso Recursivo: Descompongo el problema.
    
    # El primer término (n % 10) me da el último dígito del número, que sumo al total.
    ultimo_digito = n % 10
    
    # El segundo término (n // 10) me da el resto del número sin el último dígito.
    # Llamo a la función recursivamente con este número más pequeño.
    resto_del_numero = n // 10
    
    # Sumo el dígito actual más la suma de los dígitos del resto del número.
    return ultimo_digito + suma_digitos(resto_del_numero)

def main_ejercicio_6():
    print("--- Prueba de Suma de Dígitos Recursiva ---")

    # Coloque varios ejemplos para probar la función.
    
    # Ejemplo 1: suma_digitos(1234) -> 10
    num_1 = 1234
    print(f"La suma de los dígitos de {num_1} es: {suma_digitos(num_1)} (1+2+3+4)") 

    # Ejemplo 2: suma_digitos(9) -> 9
    num_2 = 9
    print(f"La suma de los dígitos de {num_2} es: {suma_digitos(num_2)}") 
    
    # Ejemplo 3: suma_digitos(305) -> 8
    num_3 = 305
    print(f"La suma de los dígitos de {num_3} es: {suma_digitos(num_3)} (3+0+5)") 
    
    # Pido un número al usuario para una prueba interactiva.
    while True:
        try:
            entrada_usuario = int(input("\nIngresa un número entero positivo para sumar sus dígitos: "))
            if entrada_usuario < 0:
                print("Por favor, ingresa un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
            
    resultado_final = suma_digitos(entrada_usuario)
    print(f"La suma total de los dígitos de {entrada_usuario} es: {resultado_final}")

# Llamo a la función principal para ejecutar las pruebas.
main_ejercicio_6()





#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    # La función asume que 'n' es el número de bloques en el nivel más bajo y es un entero positivo.

    # 1. Caso Base: La recursión termina cuando el nivel de la pirámide tiene solo 1 bloque.
    # Si n es 1, el total es 1.
    if n == 1:
        return 1
    
    # Manejo el caso donde n sea 0 o negativo (aunque el problema es para números positivos),
    # devolviendo 0 bloques si no hay niveles.
    if n <= 0:
        return 0

    # 2. Paso Recursivo: Descompongo el problema.
    
    # Sumo los bloques del nivel actual ('n') más el resultado de la función llamándose a sí misma 
    # con un nivel menos (n - 1). Esto suma los bloques de todos los niveles superiores.
    return n + contar_bloques(n - 1)

def main_ejercicio_7():
    print("--- Prueba de Bloques de Pirámide Recursiva ---")

    # Coloque los ejemplos dados para la prueba.
    
    # Ejemplo 1: contar_bloques(1) -> 1
    num_1 = 1
    print(f"Bloques para {num_1} nivel(es): {contar_bloques(num_1)}") 

    # Ejemplo 2: contar_bloques(2) -> 3 (2+1)
    num_2 = 2
    print(f"Bloques para {num_2} nivel(es): {contar_bloques(num_2)}") 
    
    # Ejemplo 3: contar_bloques(4) -> 10 (4+3+2+1)
    num_3 = 4
    print(f"Bloques para {num_3} nivel(es): {contar_bloques(num_3)}") 
    
    # Pido un número al usuario para una prueba interactiva.
    while True:
        try:
            entrada_usuario = int(input("\nIngresa el número de bloques en el nivel más bajo (n): "))
            if entrada_usuario < 0:
                print("Por favor, ingresa un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
            
    resultado_final = contar_bloques(entrada_usuario)
    print(f"El total de bloques necesarios para la pirámide con base {entrada_usuario} es: {resultado_final}")

# Llamo a la función principal para ejecutar las pruebas.
main_ejercicio_7()





#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    # La función asume que 'numero' es positivo y 'digito' está entre 0 y 9.

    # 1. Caso Base: La recursión termina cuando el número se reduce a 0.
    # Esto significa que ya se examinaron todos los dígitos, por lo que devuelvo 0 coincidencias.
    if numero == 0:
        return 0

    # 2. Paso de Verificación: Verifico si el último dígito del número coincide con el dígito buscado.
    ultimo_digito = numero % 10
    
    # Uso un 'sumador' que vale 1 si hay coincidencia, o 0 si no la hay.
    if ultimo_digito == digito:
        sumador = 1
    else:
        sumador = 0

    # 3. Paso Recursivo: Descompongo el problema.
    # El resultado final es la suma del 'sumador' actual más el resultado de la función 
    # llamándose a sí misma con el número sin el último dígito (numero // 10).
    numero_restante = numero // 10
    
    return sumador + contar_digito(numero_restante, digito)

def main_ejercicio_8():
    print("--- Prueba de Conteo de Dígitos Recursivo ---")

    # Coloque los ejemplos dados para la prueba.
    
    # Ejemplo 1: contar_digito(12233421, 2) -> 3
    num_1 = 12233421
    dig_1 = 2
    print(f"El dígito {dig_1} aparece {contar_digito(num_1, dig_1)} veces en {num_1}") 

    # Ejemplo 2: contar_digito(5555, 5) -> 4
    num_2 = 5555
    dig_2 = 5
    print(f"El dígito {dig_2} aparece {contar_digito(num_2, dig_2)} veces en {num_2}") 
    
    # Ejemplo 3: contar_digito(123456, 7) -> 0
    num_3 = 123456
    dig_3 = 7
    print(f"El dígito {dig_3} aparece {contar_digito(num_3, dig_3)} veces en {num_3}") 
    
    # Pido un número y un dígito al usuario para una prueba interactiva.
    while True:
        try:
            entrada_numero = int(input("\nIngresa un número entero positivo: "))
            entrada_digito = int(input("Ingresa el dígito (0-9) que quieres contar: "))
            if entrada_numero < 0 or not (0 <= entrada_digito <= 9):
                print("Por favor, el número debe ser positivo y el dígito entre 0 y 9.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa números enteros.")
            
    resultado_final = contar_digito(entrada_numero, entrada_digito)
    print(f"El dígito {entrada_digito} aparece {resultado_final} veces en {entrada_numero}.")

# Llamo a la función principal para ejecutar las pruebas.
main_ejercicio_8()