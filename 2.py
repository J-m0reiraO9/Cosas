"""Un colegio te ha contratado para que diseñes un programa que los ayude a almacenar de una manera más sencilla toda la información de sus alumnos. Cada alumno tiene nombre, grado que cursa, promedio, dirección de habitación, nombre del representante, teléfono del representante y la condición de becado o no.
Si el promedio del alumno es menor a 18, el alumno no tendrá beca; de lo contrario, sí la tendrá.
Luego de almacenar esto en su base de datos, debe existir una función que permita ver la información organizada de cada alumno de la institución.
Como requerimientos adicionales pidieron:
Mostrar los nombres, grados  y promedios de las 5 personas con mejores promedios del colegio
Mostrar un promedio general de todos los promedios de los alumnos del plantel
Mostrar cuántos alumnos tienen promedios menores a 10, cuántos entre 10 y 15 (o sea, hasta 15.9) y cuántos entre 16 y 20. """

class Alumno:
    def __init__(self, nombre, grado, promedio, dirección, nombre_padres, telefono_padres):
        self.nombre = nombre
        self.grado = grado
        self.promedio = promedio
        self.dirección = dirección
        self.nombre_padres = nombre_padres
        self.telefono = telefono_padres
        
    def show_attr(self):
        f"""
              El nombre del alumno es: {self.nombre}
              El grado del alumno es: {self.grado}
              El promedio del alumno es: {self.promedio}
              La dirección del alumno es: {self.dirección}
              El nombre de los representantes son: {self.nombre_padres}
              El numero de los papas son: {self.telefono}
              """
        
        
        
        
alumno1 = Alumno("Jose", "4to", 12.3, "El Cafetal", "Adriana y Andres", "555-3221")
alumno2 = Alumno("Maria", "4to", 17,1, "Terrazas", "Maria y Luis", "555-6666")
alumno3 = Alumno("Ignacio", "4to", 16,0, "Los Chaguaramos", "Fernanda y Daniel", "555-2122")
alumno4 = Alumno("Andrea", "4to", 19.4, "Guarenas", "Mireya y Juan", "555-3234")
alumno5 = Alumno("Hector", "4to", 11,3, "Los cortijos", "Andres y Veronica", "555-3210")


alumno2.show_attr()
        
    