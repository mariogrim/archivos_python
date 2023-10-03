
# CODE:31
# IMPORTANTE: NO borrar los comentarios

# --------------------------------
# Alumno:
# Aquí dentro definir la función ordenar

def ordenar(numeros):
    en_orden = sorted(numeros)
    return(en_orden)
# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = [2, 4, 10, 8, 12, 6]

    # Alumno: Crear la función "ordenar" fuera del bloque
    # condicional principal (ver arriba los comentarios)

    # Generar una una nueva funcion que se llame "ordenar",
    # que utilizaremos para odernar la lista de numeros.
    # Debe recibir 1 parámetro que es la lista de números
    # y retornar la nueva lista ordenada (igual a lo visto en clase)

    # Dentro de la función puede ordenar la lista
    # usando la funciones nativas de Python "sorted"

    # Luego de crear la función invocarla en este lugar,
    # almacenar el valor de retorno en una variable
    # llamada "lista_ordenada"

    ordenar(numeros)
    lista_ordenada = ordenar(numeros)

    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar:

    print("Los numeros ordenados son:", lista_ordenada)

    print("terminamos")
