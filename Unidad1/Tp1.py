#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
#Salida, muestro por pantalla el saludo.
print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f...) para
#realizar la impresión por pantalla.

#Entrada. Leyendo nombre.
nombre = input("Ingrese su nombre: ")

#Salida. Generando saludo personalizado.
print("Hola,", nombre)

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f...) para realizar
#la impresión por pantalla. ***

#Entrada. Solicitando datos al usuario. En edad leyendo y convirtiendo a entero.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
recid = input("Ingrese su lugar de recidencia: ")

#Salida. Generando mensaje de los datos de usuario.
print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {recid}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

#Entrada. Solicitud de valor posible decimal para radio. Leyendo y convirtiendo a flotante.
radio = float(input("Ingrese radio del circulo:"))

#Proceso. Calculando area y perimetro del circulo.
area = 3.14 * (radio*radio)
perimetro = 2 * 3.14 * radio

#Salida. Expresando los resultados de area y perimetro del circulo.
print (f"El area del circulo es de {area}, su perimetro es de {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

#Entrada. Solicitando, leyendo y convirtiendo valor a entero.
seg = int(input("Ingrese una cantidad de segundos: "))

#Proceso. Aplico regla de 3 simples para calcular, donde 1h=3600segundos, por lo cual la VariableHora = 1(hora)*VaiableSeg/3600segundos
hora = 1*seg/3600

#Salida. Expreso equivalencia.
print(f"La cantidad de segundos ingresados equivale a {hora} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

#Entrada. Solicito valor al usuario. Leo y convierto en entero.
num = int(input("Ingrese un numero: "))

#Salida. Titulo del calculo.
print ("La tabla de multiplicar del numero ingresado es la siguiente: ") 

#Proceso y salida de cada numero.
resultado1=num*1
print(f"{num}*1={resultado1}")

resultado2=num*2
print(f"{num}*2={resultado2}")

resultado3=num*3
print(f"{num}*3={resultado3}")

resultado4=num*4
print(f"{num}*4={resultado4}")

resultado5=num*5
print(f"{num}*5={resultado5}")

resultado6=num*6
print(f"{num}*6={resultado6}")

resultado7=num*7
print(f"{num}*7={resultado7}")

resultado8=num*8
print(f"{num}*8={resultado8}")

resultado9=num*9
print(f"{num}*9={resultado9}")

resultado10=num*10
print(f"{num}*10={resultado10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

#Entrada. Solicito dos numeros distintos de cero a usuario.
numero1=int(input("Ingrese el primer numero distinto de 0: "))
numero2=int(input("Ingrese el segundo numero distinto de 0: "))

#Proceso, realizo suma, resta, division y multiplicacion de ambos numeros ingresados.
suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2

#Salida. Imprimo los resultados del calculo.
print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicacion de {numero1} y {numero2} es: {multiplicacion}")
print(f"La division de {numero1} y {numero2} es: {division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

#IMC =  peso en kg
#      (altura en m)

#Entrada. Solicito datos decimales al usuario. Leo y convierto a decimal.
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

#Procesa, formula del calculo de IMC de una persona.
imc = peso / (altura*altura)

#Salida. Expreso el resultado del calculo.
print(f"Su Indice de masa corporal es de: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#Temperatura en Fahrenheit = 9/5*Temperatura en Celsius + 32

#Entrada. Leo y convierto a decimal el numero solicitado.
celsius=float(input("Ingrese la temperatura en grados Celsius: "))

#Proceso. Realizo el calculo de conversion de Celcius a fahrenheit 
fahrenheit=(9/5)*celsius+32

#Salida. Expreso el resultado del calculo.
print(f"{celsius} grados Celsius equivales a {fahrenheit} grados en Fahrenheit")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

#Entrada. Leo y convierto los 3 valores solicitados a decimales.
numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
numero3=float(input("Ingrese el tercer numero: "))

#Proceso. Realizo el calculo de 3 numeros para obtener su promedio.
suma=numero1+numero2+numero3
promedio=suma/3

#Salida. Expreso el resultado obtenido.
print(f"El promedio de los 3 numeros es: {promedio}")