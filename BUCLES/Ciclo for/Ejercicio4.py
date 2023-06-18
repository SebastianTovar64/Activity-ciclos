#Sumar pares desde 0 hasta el número que indique el usuario
num = int(input("Ingrese un número: "))
suma = 0
for i in range(0, num+1, 2):
    suma += i
print(f"La suma de los números pares hasta {num} es: {suma}")
