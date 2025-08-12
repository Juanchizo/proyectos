from colorama import Fore, Back, Style, init

#Creamos la clase celular q es como un objeto, pero nop, es una clase pq lo dice ahi

class CrearCelular():
    #Estas cosas q son funciones dentro de la clase se llaman metodos, pq sip, se pueden ejecutar
    #Este metodo q tiene el nombre de __init__ es de python, yo ni loco llamo una funcion asi
    
    def __init__(self, marca, modelo, calidad):
        self.marca = marca
        self.modelo = modelo
        self.calidad = calidad
        
    #El self es un parametro para referirse asi mismo
    #No influye como parametro pero es importante, lo otro q pongas despues del self se toma como parametro como todas las funciones normales
    
    #Aqui creo un metodo llamado todas q printea todo lo q le hayamos pasado con el input
    #Ya q los inputs se van todos como parametro para el metodo init asi: nomdevar = CrearCelular(imput1, input2, input3) 
    
    def todas(self):
        print(f"Tu Marca: {self.marca} \nTu Modelo: {self.modelo} \nTu Calidad: {self.calidad}")
    
    #Aqui esto es un metodo q lit destruye tu telefono y te muestra todo las caracteristicas de tu celular con self.todas()
    
    def destruirse(self):
        print("\nDestruiste tu celular el cual tenia: \n")
        self.todas()
        
    #Casi lo mismo, esto es un metodo q printea un texto q dice q agregaste aplicaciones a tu celular
    #La variable mensaje es para cuando elijas la opcion de agregar varias veces para q ya sepas q le estas metiendo mas aplicaciones de las q ya tenia
    #Lo demas es decorativo solo pq me da rabia ver todo de color gris en la terminal 
        
    def aplicaciones(self):
        print(Fore.RED + "\nAgregaste " + mensaje + "aplicaciones a tu celular!" + Style.RESET_ALL)
    
#Lit crea tu celular

print("Crea tu celular\n")
boe = input("Marca: ")
boe2 = input("Modelo: ")
boe3 = input("Calidad: ")

#Todos esos inputs a parametros para esta clase, q los convierte en variables adentro de esta

celular = CrearCelular(boe, boe2, boe3)
print("Bueno aqui estan los datos de tu celular: ")

#Para contar cuantas veces elijiste agregar

i = 0

#While True con break para q nada mas salgas destruyendo tu telefono

while True:
    
    #Aqui el mensaje utilizando la clasica de operadores ternarios para ahorrar lineas de codigo
    #Lo demas, relajao
    
    mensaje = "" if i == 0 else "muchas " if i == 1 else "muchas mas " if i == 2 else "demasiadas "
    
    eleccion = input('''
Que quieres hacer? 
      
#Destruir tu telefono
#Agregar aplicaciones
(Escribe, [Destruir] o [Agregar] sin los corchetes obvio)
      
: ''')

    eleccion = eleccion.lower()


    if eleccion == "destruir":
        celular.destruirse()
        break
        
    elif eleccion == "agregar":
        celular.aplicaciones()
        i += 1
        
    else: 
        print("Emmm eso no es una opcion")
        
#Y yapo buenisimo