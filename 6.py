class Persona: 
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
        
    def get_fullname(self):
        print(f"Me llamo {self.nombre} {self.apellido}") 
        
    def IMC(self):
        print(self.peso/self.altura **2)
    
    def es_adulto(self):
        if self.edad >= 18:
            print(True)
        else:
            print(False)
        
    
  
            
Persona1 = Persona("Juan", "Moreira", 20, 1.80, 73)
Persona2 = Persona("Miguel", "Ramos", 2, 1.20, 15)

Persona2.es_adulto()