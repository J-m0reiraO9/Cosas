#Crear en un archivo “persona.py” una clase persona con los atributos ‘nombre’, ‘apellido’, ‘edad’, ‘altura’ y ‘peso’. Crear un archivo “main” y crear una lista de objetos de la clase persona, recorrer la lista de objetos persona e imprimir su información.

class Persona: 
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
    
    def show_attr(self):
        print(f"""
                Nombre: {self.nombre}
                Apellido: {self.apellido}
                Edad: {self.edad}
                Altura: {self. altura}
                Peso: {self.peso}
              """)
        
            
Persona1 = Persona("Juan", "Moreira", 20, 1.80, 73)
Persona2 = Persona("Miguel", "Ramos", 2, 1.20, 15)

Persona2.show_attr()