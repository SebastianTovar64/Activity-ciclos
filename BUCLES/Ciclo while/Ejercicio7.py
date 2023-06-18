#Leer números enteros del teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados
suma = 0
num = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
while num!= 0:
    suma += num
    num = int(input("Ingrese un número entero (ingrese 0 para finalizar): "))
print("La sumatoria de los números ingresados es:", suma)

