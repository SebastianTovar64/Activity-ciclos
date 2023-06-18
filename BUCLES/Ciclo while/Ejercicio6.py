#Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio
n = int(input("Ingrese la cantidad de notas a promediar: "))
notas = []
i = 1
while i <= n:
    nota = float(input("Ingrese la nota "+str(i)+": "))
    notas.append(nota)
    i += 1
promedio = sum(notas) / len(notas)
print(f"El promedio de las {n} notas es: {promedio}")
