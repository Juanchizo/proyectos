from random import *
def bienvenida():
    print ("Bienvenido al juego, Preparate\n")
    print ("Que eliges?\n1. Piedra\n2. Papel\n3. Tijeras\n")
    
bienvenida()    
    
jugador = input("Pon algun numero ")

def correcion(player):
    while player == str:
     print("Eso no es una opcion")

     bienvenida()
    
     player = input("Elige con un numero: ")
     
    if player == str:
        break
     
    while player > 3:
     print("Eso no es una opcion")

     bienvenida()
    
     player = input("Elige con un numero: ")
     
jugador = int(jugador)

correcion(jugador)