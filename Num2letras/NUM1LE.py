from decimal import Decimal as deck
import re

introducir = input("Coloca un numero te lo pasaremos a letra: ")

def NUM1LE():
    indente = True
    lista = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince"]
    lista2 = ["diez", "veinte", "treinta"]
    converde = deck(introducir)
    converint = int(converde)
    comprob = re.findall(r"\W", introducir)
    

    if comprob == ["."]:
        decimals = introducir.split(".")
        print(lista[converint], "punto", lista[int(decimals[1])])
        indente = False
            
    if indente:
        if converint > 15:
            print({lista2[0]}, "y", lista[converint - 10])
        else:
            print(lista[converint])
        
NUM1LE()