import random

def obtener_nombres_aleatorios(nombre):
    return random.choice(nombre)

amigos = ["Juan", "Pedro", "Maria", "Ana", "Luis", "Carlos", "Laura", "Sofia", "Javier", "Isabel"]

# Mostramos el nombre elegido con un mensaje más claro
nombre_aleatorio = obtener_nombres_aleatorios(amigos)
print("El nombre elegido al azar es:")
print(f"Nombre elegido al azar: {nombre_aleatorio}")
print("El premio debe ser retirado en la tienda de la esquina.")
# Fin del programa  
