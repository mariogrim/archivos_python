
# CODE:35
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Generar una nueva funcion que se llame "contar",
que cuente la cantidad de veces que un número (pasado
por parámetro a la función) se repite en la lista
(también pasada por parámetro)
- Primer parámetro --> la lista de números
- Segundo parámetro --> el número a buscar y contar

Para saber cuantas veces se repiten el elemento pasado
en la lista pueden usar el método nativo de list "count"
'''
import random

# --------------------------------
# Aquí copiar la función "lista_aleatoria"
# ya elaborada en el ejercicio anterior

def lista_aleatoria(inicio, fin, cantidad):
    numeros_aleatorios = []
    for numero_aleatorio in range(cantidad):
        numero_aleatorio = random.randint(inicio, fin)
        numeros_aleatorios.append(numero_aleatorio)
    return numeros_aleatorios    

# --------------------------------

# --------------------------------
# Aquí dentro definir la función contar
def contar(lista_numeros, numero):
    for i in lista_numeros: 
        veces = lista_numeros.count(numero)
    return veces

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    inicio = 1
    fin = 6
    cantidad = 5
    numero = 3

    # Alumno: Utilizar la función "lista_aleatoria"
    # para que genere una lista de 5 números que esten comprendidos
    # entre los números 1 al 6 inclusive

    lista_numeros = lista_aleatoria(inicio, fin, cantidad)

    # Imprimir en pantalla "lista_numeros" que tendrá
    # los valores retornado por la función "lista_aleatoria":

    print("Los numeros a contar son:\n",lista_numeros)


    # Luego quiero averiguar cuantas veces se repite el numero 3
    # en la lista aleatoria creada
    cantidad_tres = contar(lista_numeros, numero)

    # print(cantidad_tres)
    print("La cantidad de numeros 3 encontrados es: ", cantidad_tres)

    print("terminamos")
