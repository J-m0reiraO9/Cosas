class Persona: 
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__altura = altura
        self.__peso = peso
    
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_edad(self):
        return self.__edad
    def get_altura(self):
        return self.__altura
    def get_peso(self):
        return self.__peso
    
    def set__peso(self,peso):
        self.__peso = peso
    
Persona1 = Persona("Juan", "Moreira", 20, 1.80, 73)
Persona2 = Persona("Miguel", "Ramos", 2, 1.20, 15)

print(Persona1.get_nombre())
Persona2.set__peso(78)
print(Persona2.get_peso())


    