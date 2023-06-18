#Elabore un algoritmo que pida un número entero mayor que cero y que escriba sus divisores. Validar que el usuario haya ingresado un número mayor a cero
num= int(input("ingrese un numero: "))
if num <= 0:
    print("El numero debe ser mayor que cero.")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
