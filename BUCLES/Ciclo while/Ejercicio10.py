#Elaborar un algoritmo que pida las 3 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio
n = int(input("Ingrese la cantidad de estudiantes: "))
estudiantes = 1
while estudiantes <= n:
    print(f"Estudiante {estudiantes}")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    nota_maxima = max(nota1, nota2, nota3)
    nota_minima = min(nota1, nota2, nota3)
    promedio = (nota1 + nota2 + nota3) / 3
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")
    print(f"Promedio: {promedio}")
    print()
    estudiantes += 1
