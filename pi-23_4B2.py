
# CODE:21
# IMPORTANTE: NO borrar los comentarios

print("Desafio con bucles y listas")

# Alumno:
# Crear una variable del tipo lista
# llamada temperaturas --> crearla vacia
# Utilizar un bucle "for" con "range"
# para solicitarle al usuario que ingrese 5
# temperaturas utilizando input
# Cada temperatura ingresada en cada iteración
# con input deberá almacenarse en la lista
# temperaturas utilizando append

# TIP
# Utilice el debugger para ver como avanza
# el programa paso a paso

# IMPORTANTE
# Cada temperatura deberá almacenarse
# como un valor decimal (utilice float con el input)



# Imprimir en pantalla la variable temperaturas
# Deberá observar sus 5 temperaturas ingresadas
# por consola

temperaturas = []
temeratura = 0 

for i in range(5):
    temperatura = float(input("Ingrese temperatura: "))
    temperaturas.append(temperatura)
print ("Las temperaturas ingresadas son:\n", temperaturas)
