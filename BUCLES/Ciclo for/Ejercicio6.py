#Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero:"))
if num1 > num2:
    print("El primer numero debe ser menor que el segundo numero")
for num in range(num1, num2 + 1):
    print(num)



