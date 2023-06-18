#Digite un número, si el numero supera a 10, multiplique los 10 primeros números, sino, súmelos
numero = int(input("Ingrese un número: "))
if numero > 10:
    resultado = 1
    contador = 1
    while contador <= 10:
        resultado *= contador
        contador += 1
else:
    resultado = 0
    contador = 1
    while contador <= numero:
        resultado += contador
        contador += 1
print(f"El resultado es: {resultado}")
