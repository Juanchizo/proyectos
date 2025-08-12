from random import randint

bot = randint(1, 50)
numero = randint(1, 50)

def inicio(x):
 print(f"Bienvenido{x}al juego")

inicio(" ")

jugador = input("\nElige un numero del uno al 50: ")
jugador = int(jugador)

while jugador == 0 or jugador > 50:
    print("Eso no es una opcion")
    inicio(" otra vez ")
    jugador = input("\nElige un numero del uno al 50: ")
    jugador = int(jugador)


while jugador != numero and bot != numero:
    mensajej = "Tu numero es menor al q debes adivinar" if jugador < numero else "Tu numero es mayor al q debes adivinar"
    mensajeb = f"El numero del bot es menor al q debe adivinar.\nNumero del bot: {bot}" if bot < numero else f"El numero del bot es mayor al q debe adivinar.\nNumero del bot: {bot}"
    
    print(mensajej)
    print(mensajeb)
    #print(jugador)
    
    bot = randint(1,50)
    
    #print(numero)

    jugador = input("\nElige un numero del uno al 50: ")
    jugador = int(jugador)

mensajef = "Ganaste!!" if jugador == numero else "El bot gano" + "\nPerdiste" + str(bot) if bot == numero else "Empataste"

print(mensajef)
