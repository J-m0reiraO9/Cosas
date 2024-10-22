class Alimento:
    def __init__(self, peso, empaque): 
        self.peso = peso
        self.empaque = empaque
        
class carnes(Alimento):
    def __init__(self, nombre, peso, empaque, marca):
        super().__init__(peso, empaque)
        self.marca = marca
        self.nombre = nombre
        
        
    def show_attr(self):
        print(f"""
              
              nombre = {self.nombre}
              peso = {self.peso}
              empaque = {self.empaque}
                            
              """)

        
carnico = carnes("Costilla", "3kg", "plastico", "Oscar Mayer")
carnico.show_attr()

class verduras(Alimento):
    def __init__(self, nombre, peso, empaque, marca):
        super().__init__(peso, empaque)
        self.nombre = nombre
        self.marca = marca
        
    def show_attr(self):
        print(f"""
              
              nombre = {self.nombre}
              peso = {self.peso}
              empaque = {self.empaque}
              marca = {self.marca}
              
              """)


vegetal = verduras("Cebolla", "350g", "plastico", "Finca 2 aguas")

vegetal.show_attr()

class frutas(Alimento):
    def __init__(self, nombre, peso, empaque, fruta):
        super().__init__(peso, empaque)
        self.fruta = fruta
        self.nombre = nombre
        
    def show_attr(self):
        print(f"""
              
              fruta = {self.nombre}
              peso = {self.peso}
              empaque = {self.empaque}
              marca = {self.fruta}
              
              """)

fruta = frutas("uva", "8g", "plastico", "Ocean Spray")

fruta.show_attr()

class Bebida:
    def __init__(self,nombre, volumen, grado_alcoholico):
        self.nombre = nombre
        self.volumen = volumen
        self.alcoholico = grado_alcoholico
        
class Alcoholica(Bebida):
    def __init__(self, volumen, grado_alcoholico, precio, nombre):
        super().__init__(volumen, grado_alcoholico, nombre)
        self.precio = precio * 0.65
        
    def show_attr(self):
        print(f"""
              
              nombre = {self.nombre}
              peso = {self.volumen}
              empaque = {self.alcoholico}
              bebida = {self.precio}
              
              """)

        
Alcohol = Alcoholica("Jagermeister","150ml", 75, 0.35)

Alcohol.show_attr()

class Energetica(Bebida):
    def __init__(self, volumen, grado_alcoholico, costo, nombre):
        super().__init__(volumen, grado_alcoholico, nombre)
        self.costo = costo * 0.85
        
    def show_attr(self):
        print(f"""
              
              nombre = {self.nombre}
              volumen = {self.volumen}
              Volumen de alcohol = {self.alcoholico}
              precio = {self.costo}
              
              """)

        
Red_Bull = Energetica("Red Bull", "473ml", 3, 0)

Red_Bull.show_attr()

class Comercial(Bebida):
    def __init__(self, volumen, grado_alcoholico, costo, nombre):
        super().__init__(volumen, grado_alcoholico, nombre)
        self.costo = costo * 0.85
        
        
    def show_attr(self):    
        print(f"""
              
              nombre = {self.nombre}
              volumen = {self.volumen}
              Volumen de alcohol = {self.alcoholico}
              precio = {self.costo}
              
              """)
             
        
Del_Valle = Comercial("Del_Valle", "300ml", 2, 0)

Del_Valle.show_attr()    