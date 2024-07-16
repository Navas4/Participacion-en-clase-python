# Realice un programa que imprima los 50 primeros numeros de la sucesion de Fibonacci empezando en 0.
# * La serie Fibonacci se compone por una sucesion de numeros en la que el siguiente siempre es la suma de los anteriores.
# * 0, 1, 1, 2, 3, 5, 8, 13...

N = 0
A = 1
C=0
for C in range (50):
    print(N)
    S=N+A
    N=A
    A=S
     
     