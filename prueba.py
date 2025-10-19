#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

numero = 0
sumatoria = 0

for numero in range(1,11):
    numero = int(input("Ingrese el un numero entero: "))
    sumatoria += numero

print("La sumatoria de los valores es: ",sumatoria)
print("La media de los valores ingresados es:",(sumatoria/10))






