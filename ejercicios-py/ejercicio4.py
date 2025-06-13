""" Imprime la tabla de multiplicar de un numero n"""

num = int(input("Digite un numero:"))

print ()
for i in range (0,11):
    print(f"{num} x {i} ={i*num}")