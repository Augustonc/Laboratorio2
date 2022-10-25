# Faltan clases de la 1 a la 6

# FUnciones Recursivas
def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso recursivo

resultado = factorial(5) # Hacemos codigo duro
print(f'El factorial del número 5 es: {resultado}') # Tarea, que el usuario ingrese el numero para calcular el factorial