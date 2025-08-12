from decimal import Decimal
import re

introducir = input("Coloca un numero te lo pasaremos a letra: ")

def NUM1LE():
    indente = True
    lista = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince"]
    converbo = Decimal(introducir)
    converint = int(converbo)
    comprob = re.findall(r"\W", introducir)
    

    if comprob == ["."]:
        decimals = int((converint - converbo) * -10)
        print(lista[converint], "punto", lista[decimals])
        indente = False
            
    if indente:
        print(lista[converint])
        
NUM1LE()