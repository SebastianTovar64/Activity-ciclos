#Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio.
numeroTemperaturas= int(input("Cuantas temperaturas va a introducir: "))
temperaturas = []
for i in range(numeroTemperaturas):
    temperatura = float(input("Ingrese una temperatura: "))
    temperaturas.append(temperatura)
temperaturaAlta = temperaturas[0]
temperaturaBaja = temperaturas[0]
sumaTemperaturas = 0
for temperatura in temperaturas:
    if temperatura > temperaturaAlta:
        temperaturaAlta = temperatura
    if temperatura < temperaturaBaja:
        temperaturaBaja = temperatura
    sumaTemperaturas += temperatura
temperaturaPromedio = sumaTemperaturas / numeroTemperaturas
print(f"La temperatura más alta es {temperaturaAlta}")
print(f"La temperatura más baja es {temperaturaBaja}")
print(f"La temperatura promedio es {temperaturaPromedio}")




