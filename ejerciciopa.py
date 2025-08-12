from random import randint

def bienvenida():
    print("Bienvenido al juego, Preparate\n")
    print("Que eliges?\n1. Piedra\n2. Papel\n3. Tijeras\n")

bienvenida()

jugador = input("Elige con un numero: ")
try:
    jugador = int(jugador)
except ValueError:
    print("Por favor, ingresa un número válido.")
    jugador = 0  # O algún valor predeterminado

while not (1 <= jugador <= 3):
    print("Eso no es una opcion")
    bienvenida()
    jugador = input("Elige con un numero: ")
    try:
        jugador = int(jugador)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        jugador = 0  # O algún valor predeterminado

bot = randint(1, 3)

DefinitivoJ = "\nHas elegido Piedra" if jugador == 1 else "\nHas elegido Papel" if jugador == 2 else "\nHas elegido Tijera"
print(DefinitivoJ)

DefinitivoB = "\nEl bot eligió Piedra" if bot == 1 else "\nEl bot eligió Papel" if bot == 2 else "\nEl bot eligio Tijera"
print(DefinitivoB)

mensaje = "\nEmpataste\n" if jugador == bot else ""

if jugador != bot:
    mensaje = "\nGanaste" if (jugador == 1 and bot == 3) or (jugador == 2 and bot == 1) or (jugador == 3 and bot == 2) else "\nEl bot gano"

print(mensaje)

