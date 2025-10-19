#Práctico 4: Estructuras repetitivas
#
#Actividades
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0,101):
    print(numero)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
numero = 0
cantidad_caracteres = 0

numero = input("Ingrese un numero entero: ")

cantidad_caracteres = len(numero)

print(f"El numero ingresado tiene {cantidad_caracteres} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

primer_valor = 0
segundo_valor = 0
sumatoria = 0
num = 0

primer_valor = int(input("Ingrese el primer numero entero: "))
segundo_valor = int(input("Ingrese el segundo numero entero: "))

for num in range(primer_valor+1,segundo_valor):
        sumatoria = sumatoria + num

print(sumatoria)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

numero = 0
sumatoria = 0

numero = int(input("Ingrese el primer numero para comenzar a sumar (0 para cortar): "))
while numero != 0:
      sumatoria += numero
      numero = int(input("Ingrese el siguiente numero para continuar sumando (0 para cortar): "))

print(sumatoria)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

NUMERO_ALEATORIO = 0
num_intento_usuario = 0
cant_intentos = 1

num_intento_usuario = int(input("Ingrese un numero para adivinar: "))
while num_intento_usuario != NUMERO_ALEATORIO:
     cant_intentos += 1
     num_intento_usuario = int(input("Intentalo de nuevo! Ingresa otro numero: "))

print("Adivinaste! Se realizaron",cant_intentos,"intentos.")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for numero in range(100,-1,-2):
    print(numero)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

primer_valor = 0
valor_usuario = 0
sumatoria = 0
num = 0


valor_usuario = int(input("Ingrese un numero entero, para sumar los numeros comprendidos entre 0 y su numero: "))

for num in range(primer_valor,valor_usuario):
        sumatoria = sumatoria + num

print(sumatoria)


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numero = 0
num_par = 0
num_impar = 0
num_positivo = 0
num_negativo = 0


for numero in range(1,101):
    numero = int(input("Ingrese el un numero entero: "))
#pares e impares
    if numero % 2 == 0:
        num_par += 1
    else:
        num_impar += 1

#positivos y negativos
    if numero > 0:
        num_positivo += 1
    else:
        num_negativo += 1

#Mostrar resultados al final
print(num_par, "numeros son par.")
print(num_impar, "numeros son impar.")
print(num_positivo, "numeros son positivos.")
print(num_negativo, "numeros son negativos.")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

for numero in range(1,101):
    numero = int(input("Ingrese el un numero entero: "))
    sumatoria += numero

print("La sumatoria de los valores es: ",sumatoria)
print("La media de los valores ingresados es:",(sumatoria/100))

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingresa un numero: "))

if numero < 0:
    es_negativo = True
    numero = -numero #Lo convierto a postivo temporalmente.
else:
    es_negativo = False

#invierto el numero
inverso = 0
while numero > 0:
    digito = numero % 10 #obtengo el ultimo digito
    inverso = inverso * 10 + digito #construyo el numero invertido
    numero = numero // 10 #eimino el ultimo digito

#signo negativo
if es_negativo:
    inverso = -inverso

#muestro el numero invertido
print("El numero invertido es: ", inverso)