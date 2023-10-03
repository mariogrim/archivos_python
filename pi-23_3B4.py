
# CODE:14
# IMPORTANTE: NO borrar los comentarios

cantidad_numeros_positivos = 0

# Alumno:
# Deberá solicitar tres números enteros por consola,
# cada nuḿero entero lo debe almacenar en variables llamadas:
# numero_1
# numero_2
# numero_3

# Deberá realizar un tres condicionales separados,
# en cada condicional deberá averiguar si cada número
# es mayor a cero.

# Por cada número mayor a cero (cada condicional que se cumpla)
# deberá incrementar en 1 (+= 1) la "variable cantidad_numeros_positivos"


# Al finalizar, imprimir en pantalla la variable cantidad_numeros_positivos

numero_1 = int(input("ingrese el primer numero: "))

if numero_1 > 0 :
    cantidad_numeros_positivos += 1
else :
    cantidad_numeros_positivos = cantidad_numeros_positivos

numero_2 = int(input("ingrese el segundo numero: "))

if numero_2 > 0 :
    cantidad_numeros_positivos += 1
else :
    cantidad_numeros_positivos = cantidad_numeros_positivos

numero_3 = int(input("ingrese el tercer numero: "))

if numero_3 > 0 :
    cantidad_numeros_positivos += 1
else :
    cantidad_numeros_positivos = cantidad_numeros_positivos

print ("La cantidad de numeros positivos ingresados es:", cantidad_numeros_positivos)
