#Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero
num = int(input("Ingrese un número mayor que cero: "))
while num <= 0:
    num = int(input("Error: Ingrese un número mayor que cero: "))
print(f"Los divisores de {num} son:")
divisor = 1
while divisor <= num:
    if num % divisor == 0:
        print(divisor)
    divisor += 1
