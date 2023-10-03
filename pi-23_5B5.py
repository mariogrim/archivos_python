
# CODE:33
# IMPORTANTE: NO borrar los comentarios

# --------------------------------
# Alumno:
# Aquí copiar la función "generar_invitados"
# ya elaborada
def generar_invitados():
    invitados = []
    for i in range(3):
        i = input("Ingrese invitado: ",  )
        invitados.append(i)
    return invitados


# --------------------------------

# --------------------------------
# Alumno:
# Aquí copiar la función "ordenar"
# ya elaborada
def ordenar(lista_invitados):
    en_orden = sorted(lista_invitados)
    return(en_orden)

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: 
    # Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bloque "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenarla

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el retorno en "lista_invitados"

    lista_invitados = generar_invitados()

    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada
    #    --> Almacenar el retorno en "lista_invidatos_ordenada"

    lista_invidatos_ordenada = ordenar(lista_invitados)

    # Imprimir en pantalla "lista_invidatos_ordenada":

    print("La lista ordenada es:", lista_invidatos_ordenada)
    print("terminamos")