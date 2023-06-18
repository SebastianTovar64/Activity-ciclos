#Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
n = int(input("Por favor, ingrese un número: "))
suma = 0
numeroImpares = 0
i = 1
while i <= n:
    if i % 2 != 0:
        suma += i
        numeroImpares += 1
    i += 1
print(f"La suma de todos los números impares desde 1 hasta {n} es: {suma}")
print(f"Hay  {numeroImpares} " "números impares en total.")
