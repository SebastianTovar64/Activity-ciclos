#Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.
n = int(input("Ingrese el número de estudiantes: "))
notas = []
for i in range(n):
    nota = float(input("Ingrese la nota del estudiante {}: ".format(i+1)))
    notas.append(nota)

notaAlta = max(notas)
notaBaja = min(notas)
promedio = sum(notas) / n
print(f"La nota más alta es: {notaAlta}")
print(f"La nota más baja es: {notaBaja}")
print(f"El promedio es: {promedio:.1f}")



