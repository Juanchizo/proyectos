class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def atributos(self):
        print(f"Tu nombre: {self.nombre}\n\nTu Edad: {self.edad}\n")  
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def estancia(self):
        print(f"Tu grado: {self.grado}\n")
    
    def atributos2(self):
        super().atributos()
        self.estancia()

estudiant = Estudiante("Juan", 14, 4)

print(f"{estudiant.nombre}\n{estudiant.edad}\n{estudiant.grado}\n")

estudiant.atributos()
estudiant.estancia()
estudiant.atributos2()