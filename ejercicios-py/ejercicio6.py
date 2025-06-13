import random

# Función que calcula el factorial
def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):  # Uso de ciclo for
        resultado *= i
    return resultado  # Retorno

# Declaración de variable (sin tipo)
numero = random.randint(1, 10)

# Condicional
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Llamada a la función
factorial = calcular_factorial(numero)
print(f"{numero}! = {factorial}")