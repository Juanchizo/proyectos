print("Aqui esta el menu\n")

menu = ["Papas Fritas","Hamburguesa","Arepa","Jamon"]

for comidas in menu:
    print(f"*{comidas}")
    
comida = input("\nElige la comida correcta para Sofia: ")

while comida != menu[0] and comida != menu[2] and comida != menu[3]:
    
    if not comida in menu:
        print("\nEso no esta en el menu")
  
    else:
        print("\nEso no le gusta a Sofia")
        
    print("\nAqui esta el menu otra vez\n")
    
    for comidas in menu:
        print(f"*{comidas}")
        
    comida = input("\nElige la comida correcta para Sofia: ")

 
print("Bien Hecho!!")
