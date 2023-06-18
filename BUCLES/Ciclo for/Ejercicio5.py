#Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay
n = int(input("Ingrese un número: "))
suma = 0
impares = 0
for i in range(1, n+1, 2):
    suma += i
    impares += 1
print(f"La suma de todos los números impares hasta {n} es: {suma}")
print(f"Cantidad de números impares: {impares}")
