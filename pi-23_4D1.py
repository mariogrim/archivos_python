
# CODE:41
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Comience por crear una variable llamada resultado
  para almacenar la palabra final que usted arme
  segun el criterio establecido en el enunciado.

- Deberá proveer por consola la palabra objetivo a ordenar
  la cual se almacenará en la variable llmada objetivo
- Deberá utilizar bucles para recorrer la palabra objetivo
  y deberá usar listas y todo método de strings a su disposición
  que lo ayude a resolver este desafio.
'''

print("Ordenar caracteres")
objetivo = input("Ingrese palabra de entrada:\n")
# Empezar aquí la resolución del ejercicio

resultado = 0
minusculas = ""
mayusculas = ""
num_pares = ""
num_impares = ""

for i in objetivo:
    if i.islower():
        minusculas += i
    elif i.isupper():
        mayusculas += i
    elif i == "0":
        num_pares += i   
    elif int(i):
        if int(i) % 2 == 0:
            num_pares += i
        else:
            num_impares += i

minusculas = "".join(sorted(minusculas))
mayusculas = "".join(sorted(mayusculas))
num_pares = "".join(sorted(num_pares))
num_impares = "".join(sorted(num_impares))

resultado = minusculas+mayusculas+num_impares+num_pares

print("El resultado es:", resultado)