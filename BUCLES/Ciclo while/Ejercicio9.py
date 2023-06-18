#Elabore un algoritmo que permita ingresar n número de temperaturas y escriba la temperatura más alta, la más baja y la temperatura promedio.
numeroTemperatura = int(input("Ingrese la cantidad de temperaturas: "))
sumaTemperaturas = 0
contador = 0
temperaturaAlta = float('-inf') #representa el número real infinitivo negativo
temperaturaBaja = float('inf') #representa el número real infinitivo positivo
while contador < numeroTemperatura:
    temperatura = float(input("Ingrese una temperatura: "))
    sumaTemperaturas += temperatura
    if temperatura > temperaturaAlta:
        temperaturaAlta = temperatura
    if temperatura < temperaturaBaja:
        temperaturaBaja = temperatura
    contador += 1
promedio = sumaTemperaturas / numeroTemperatura
print(f"Temperatura máxima: {temperaturaAlta}")
print(f"Temperatura mínima: {temperaturaBaja}")
print(f"Temperatura promedio: {promedio}")
