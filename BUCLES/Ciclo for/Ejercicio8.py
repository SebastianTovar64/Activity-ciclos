#Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio.
numero_de_notas = int(input("Ingrese el numero de notas: "))
nota = [] #Crear lista vacia para almacenar las notas
for i in range(numero_de_notas):
#el .format nos permite incluir en una cadena, texto ordinario y caracteres de formateo, que representan un tipo en particular de datos, tales como entero, cadena o flotante 
    nota.append(float(input("ingrese la nota {}: " .format(i+1)))) 
# sum recibe como argumento un objeto iterable y retorna la suma de sus elementos
promedio = sum(nota)/ numero_de_notas 
print("El promedio de la nota es: {} ." .format(promedio))
