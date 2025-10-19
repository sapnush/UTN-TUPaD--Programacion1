#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Entrada. Leyendo edad.
nombre = int(input("Ingrese su edad: "))

#Condicional simple if.
if edad >= 18:
    print ("Eres mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

#Entrada. Solicitando y leyendo nota
nota = float(input("Ingrese su nota: "))

#Condicional compuesto if-else
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

#Entrada. Solicitando y leyendo nota
numero + int(input("Ingrese un numero par: "))

#Condicional compuesto if-else
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    Print("Por favor, ingrese numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

#Entrada y lectura de edad
edad = int(input("Ingrese su edad: "))

#Identificar categoria por edad e indicar a cual pertenece
if edad < 12:
    categoria = "Niño/a"
elif edad >= 12 and < 18:
    categoria = "Adolescente"
elif edad >= 18 and < 30:
    categoria = "Adulto?a joven"
else:
    edad >= 30
    categoria = "Adulto/a"

Print(f"Categoria: {categoria}")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("Ingrese su contraseña: ")

if len(contraseña) >= 8 and <= 14:
    print ("Ha ingresado una contyraseña correcta")
else:
    print ("Por favor, ingrese una contraseña entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente:

#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3]
#mean(mi_lista)

from statics import mode, mediana, mean

mi_lista = [1, 2, 5, 5, 3]

print(f"Media: {mean(mi_lista)}")
print(f"Mediana: {mediana(mi_lista)}")
print(f"Moda: {mode(mi_lista)}")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.


#Pedir una frase o palabra al usuario
frase = input("Ingrese una frase: ")

#Definir vocales
vocales = [a, e, i, o, u] or [A, E, I, O, U]

#Verificar si termina con vocal
if frase [-1] in vocales: 
	frase = frase + "!"

#Mostrar resultado
print (frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

#Solicitar y leer nombre
nombre = input("Ingrese su nombre: ")

#Solicitar que usuario ingrese la opción
opcion = input("Ingrese 1 para mayúsculas, 2 paran minúsculas, 3 para primera letra en mayúscula: ")

#Trasformar según la opción
if opcion == "1":
    print (nombre.upper(opcion))
elif opcion == "2":
    print (nombre.lower(opcion))
elif opcion == "3":
    print(nombre.title(opcion))
else:
    print("Opcion no valida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#Solicitar magnitud del terremoto y leer 
magnitud = float(input("Ingrese la magnitud del terremoto: "))

#Escala de ritcher
if magnitud < 3:
    categoria = "Muy leve"
elif magnitud >= 3 and < 4:
    categoria = "Leve"
elif magnitud >= 4 and < 5:
    categoria = "Moderado"
elif magnitud >= 5 and < 6:
    categoria = "Fuerte"
elif magnitud >= 6 and < 7:
    categoria = "Muy fuerte"
else:
    magnitud >= 7:
    categoria = "Extremo"

Print(f"Categoria: {categoria}")

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

#Entrada, solicitar hemisferio, mes y día al usuario
hemisferio = input("Ingrese el hemisferio en el que se encuentra: ")
mes = input("Ingrese el mes actual: ")
dia = int(input("Ingrese el día de hoy: "))

#Proceso, calcular estación en base a los datos Hemisferio Norte
if hemisferio == "N" or "n" or "Norte" or "norte":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        estacion = "invierno"
    elif (mes == "marzo"and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "primavera"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "verano"
    else:
        estacion = "otoño"

#Proceso, calcular estación en base a los datos Hemisferio Sur
if hemisferio == "S" or "s" or "Sur" or "sur":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        estacion = "verano"
    elif (mes == "marzo"and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "otoño"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "invierno"
    else:
        estacion = "primavera"

#Salida, informar al usuario la estación en la que se encuentra
print (f"Estacion: {estacion}")