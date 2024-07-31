# Escribe un programa que le solicite al usuario
# un numero entero y muestre todos los numeros
# correlativos entre el 1 y el numero
# ingresado por el usuario.

numero =int(input("Ingresa un valor: "))
numero_limite = range(1,numero+1)

numero_entero=""


for indice in numero_limite:
    numero_entero+= str(indice)+" "
    
print(numero_entero)
