#. Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
while num1 >= num2:
    print("Error: El primer número debe ser menor que el segundo.")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
contador = num1
while contador <= num2:
    print(contador)
    contador += 1

