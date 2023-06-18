#. Digite un número, si el numero supera a 10, multiplique los 10 primeros números, si no, súmelos
num = int(input("Ingrese un número: "))
if num > 10:
    product = 1
    for i in range(1, 11):
        product *= i
    print(f"El producto de los primeros 10 números es: {product}")
else:
    suma = 0
    for i in range(1, num+1):
        suma += i
    print(f"La suma de los primeros {num} números es: {suma}")


