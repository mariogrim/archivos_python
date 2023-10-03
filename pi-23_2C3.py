
# CODE:8
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada nombre_completo
  para almacenar el nombre completo que usted
  debe ingresar por consola con la función input.
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_lower
  para almacenar el nombre completo con todas
  las letras transformadas a minúsculas
  por la función lower
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_upper
  para almacenar el nombre completo con todas
  las letras transformadas a mayúsculas
  por la función upper
  Imprimir en consola el contenido de esta variable

- Crear una variable llamada nombre_capitalize
  para almacenar el nombre completo con
  la primera letra del nombre en mayúscula
  por la función capitalize
  Imprimir en consola el contenido de esta variable

'''

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio

nombre_completo = str(input("Ingrese nombre completo: "))
nombre_lower = (nombre_completo).lower()
nombre_upper = (nombre_completo).upper()
nombre_capitalize = (nombre_completo).capitalize()

print ("Nombre en minusculas: ", nombre_lower)
print ("Nombre en mausculas: ", nombre_upper)
print ("Nombre con letra capital: ", nombre_capitalize)
