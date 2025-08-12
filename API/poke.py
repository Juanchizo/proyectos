import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

reponer = requests.get( URL )

datos = reponer.json()

print("Hola checa esta lista de pokemons")

#Imprime todos los nombres de los pokemones
for pokemons in datos["results"]:
    print(pokemons["name"])
    
pokemon = input("\nDecime un pokemon de esa lista: ")

reponer = requests.get( URL + pokemon )
datos = reponer.json()

want = input(f"que quieres saber sobre {pokemon}? [responde con su repectivo numero] \n1. Abilidades \n2. En que juegos aparece \n3. Su peso \n4. Movimientos\n")

want = int(want)

if want == 1:
    for abilidades in datos["abilities"]:
        print(abilidades["ability"]["name"])

if want == 2:
    for gameindices in datos["game_indices"]:
        print(gameindices["version"]["name"])

if want == 3:
    print(datos["height"], "kg")

if want == 4:
    for moviemientos in datos["moves"]:
        print(moviemientos["move"]["name"])
        
