#Sumar pares desde 0 hasta el número que indique el usuario.
numero = int(input("Ingresa un número: "))
suma = 0
i = 0
while i <= numero:
    if i % 2 == 0:
        suma += i
    i += 1
print(f"La suma de los números pares hasta {numero} es: {suma}")