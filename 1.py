class Pikachu: 
    tipo = "Electrico"
    
    def __init__(self,nombre,nivel,salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
    
    def ataque(self):
        print(f"Pikachu ataca y genera {self.salud/4} de daño")
        
Pikachu_1 = Pikachu("Pepe", 5, 100)
Pikachu_2 = Pikachu("Jose", 9, 120)

print(f"Tipo: {Pikachu_1.tipo}")
Pikachu_2.ataque()
print(f"Salud: {Pikachu_2.salud}")
        