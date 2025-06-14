def encontrar_mayor_y_menor(numeros):
    """Encuentra el número mayor y el número menor en una lista.

    Args:
        numeros: Una lista de números.

    Returns:
        Una tupla con el número mayor y el número menor, o (None, None) si la lista está vacía o contiene elementos no numéricos.
    """
    if not numeros:
        return None, None  # Manejar el caso de lista vacía

    try:
        mayor = max(numeros)
        menor = min(numeros)
        return mayor, menor
    except TypeError:
        return None, None  # Manejar el caso de elementos no numéricos

def obtener_lista_numeros():
    """Obtiene una lista de números del usuario."""
    while True:
        entrada = input(" Ingresa una lista de números separados por espacios (ej. 1 2 3): ")
        if not entrada.strip():
            print("⚠ Por favor, ingresa al menos un número.")
            continue

        try:
            numeros = [float(num) for num in entrada.split()]
            return numeros
        except ValueError:
            print("Por favor, ingresa solo números válidos.")

def main():
    """Función principal que obtiene la lista, encuentra el mayor y el menor, y muestra los resultados."""
    numeros = obtener_lista_numeros()
    mayor, menor = encontrar_mayor_y_menor(numeros)

    if mayor is not None and menor is not None:
        print(f"\n Números ingresados: {numeros}")
        print(f" Mayor: {mayor}")
        print(f" Menor: {menor}")
    else:
        print("No se pudo determinar el mayor y el menor. Asegúrate de ingresar números válidos.")

main()
      
 
