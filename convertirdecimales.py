# Escribe un programa que solicite al usuario ingresar un numero
# con decimales y almacenalo en una variable.
# A continuacion, el programa debe solicitar al usuario que ingrese
# un mumero entero y guardarlo en otra variable.
# En una tercera variable se debera guardar el resultado de la suma
# de los dos numeros ingresados por el usuario.
# Por ultimo, se debe mostar en pantalla el texto
# "El resultado de la suma es [suma]", donde "[suma]"
# se reemplazara por el resultado de la operacion.

valordecimal = float(input("Ingrese un decimal: "))
valorentero = int(input("Ingrese un entero: "))
suma = valordecimal + valorentero
print("El resultado de la suma es ", suma)
print("El resultado de la suma es " + str (suma))
