from num2words import num2words

while True:
    try:
        numero = input("Ingresa cualquier numero y te lo pasaremos a letra: ")
        trobo = numero
        trobo = bool(trobo)
        break
    except:
        print("Eso no es un numero")

numerao = num2words(numero, lang="es")
print(numerao)
