# Eunción para sumar los elementos de una lista
def sumar_array(lista): 
   suma=0
   for numero in lista : # ciclo for
        suma += numero
   return suma # retorno

# Declaración de lista (array)
numeros = { 5, 12, 3, 7, 8}

# Condicional para verificar si la lista está vacia
if len(numeros) == 0:
    print("La lista está vacia.")
else:
    total = sumar_array(numeros) # llamada a función
    print(f"La suma de los elementos es: {total}")