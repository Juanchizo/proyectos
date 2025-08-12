hola = ["pizza", "hamburguesa", "ensalada", "pasta", "sushi"]

print(f"""¡Hola! Aquí tienes esta lista: """)
for cosas in hola: 
    print(cosas)

inputwd = input("¿Qué te gustaría comer? ")
inputwd = inputwd.lower()

def Recorrido():
    
    i = 0
    
    while not i > 4:
        
        if hola[i] == inputwd:
            break
        else: i += 1 
        
    if i == 5:
        return f"su ({inputwd}) no se encuentra en la lista"
    
    else: 
        return f"Tome su {hola[i]} caballero"
    
print(Recorrido())