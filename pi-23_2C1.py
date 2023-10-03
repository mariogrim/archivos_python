
# CODE:6
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Almacenar el valor de cada operación realizada en las
  variables que usted creará con los siguientes nombres:
  suma, resta, multiplicacion, division, potencia

- Al final imprimir todos los resultados almacenados
  en esas variables
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

numero_1 = float(input ("Ingrese el primer numero decimal: "))
numero_2 = float(input ("Ingrese el segundo numero decimal: "))
suma = numero_1+numero_2
resta = numero_1-numero_2
multiplicacion = numero_1*numero_2
division = numero_1/numero_2
potencia = numero_1**numero_2
print ("La suma de esos numeros es:", suma)
print ("La resta de esos numeros es:", resta)
print ("La multiplicacion de esos numeros es:",multiplicacion)
print ("La division de esos numeros es:", division)
print ("La potencia de esos numeros es:", potencia)

