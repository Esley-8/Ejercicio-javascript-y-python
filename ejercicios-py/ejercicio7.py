import random

# Función para invertir una palabra
def invertir_palabra(palabra):
    invertida = ''
    for letra in palabra:  # ciclo for
        invertida = letra + invertida
    return invertida  # retorno

# Lista de palabras (declaración de variable)
palabras = ["hola", "mundo", "python", "codigo", "cadena"]

# Condicional para verificar que la lista no esté vacía
if len(palabras) == 0:
    print("La lista de palabras está vacía.")
else:
    palabra_aleatoria = random.choice(palabras)
    palabra_invertida = invertir_palabra(palabra_aleatoria)
    print(f"La palabra seleccionada es: {palabra_aleatoria}")
    print(f"La palabra invertida es: {palabra_invertida}")