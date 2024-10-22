class Libro:
    def __init__(self, titulo, autor, n_paginas, n_capitulos, n_edicion, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.n_paginas = n_paginas
        self.n_capitulos = n_capitulos
        self.n_edicion = n_edicion
        self.cantidad = cantidad
        
    def show_attr(self):
        print(f"""
              Titulo: {self.titulo}
              Autor: {self.autor}
              Numero de paginas: {self.n_paginas}
              Capitulos: {self.n_capitulos}
              Edición: {self.n_edicion}
              Cantidad: {self.cantidad}          
              """)
        
        
Libro1 = Libro("100 años de soledad", "Gabriel Garcia Marquez", 560, 20, 100, 8)
Libro2 = Libro("El arte de la guerra", "Sun Tzu", 96, 13, 15, 4)
Libro3 = Libro("No hay vida sin matrinomio", "Teo Tang", 46, 3, 2, 10)
Libro4 = Libro("Ha vuelto", "Pio Medina", 205, 20, 3, 2)

Libro2.show_attr()

class Autor:
    def __init__(self, nombre, apellido, cedula, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.nacionalidad = nacionalidad
        
    def show_attr(self):
        print(f"""
            Nombre = {self.nombre}
            Apellido = {self.apellido}
            Cedula = {self.cedula}
            Nacionalidad = {self.nacionalidad}            
              """)
        
Autor1 = Autor("Pio", "Medina", 15865474, "Venezolano")
Autor2 = Autor("Alberto", "Paz", 19345678, "Venezolano")

Autor2.show_attr()

class Editorial:
    def __init__(self, nombre, dirección):
        self.nombre = nombre
        self.dirección = dirección
        
    def show_attr(self):
        print(f"""
              Nombre = {self.nombre}
              Dirección = {self.dirección}           
              """)
        
Editorial1 = Editorial("Santillana", "Caricuao")

Editorial1.show_attr()
        

        

