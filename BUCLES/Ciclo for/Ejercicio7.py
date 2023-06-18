#Algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10.
number = int(input("Introduce el número de la tabla a multiplicar: "))
for i in range(11):
    print(f"{number} x {i} = {number * i}")