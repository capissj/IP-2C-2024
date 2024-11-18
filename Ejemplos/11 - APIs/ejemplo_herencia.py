class Animal:

    def __init__(self, nombre: str , edad: int):
        self.nombre = nombre
        self.edad = edad    
    
    #def emitir_sonido(self):
    #    pass

class Insecto(Animal):
    pass

class Perro(Animal):
    def emitir_sonido(self):
        return "Guau!"

class Gato(Animal):
    def emitir_sonido(self):
        return "Miau!"

class Pato(Animal):
    def emitir_sonido(self):
        return "Cuac!"

# Crear instancias de diferentes animales
miPerro = Perro("Dylan", 10)
miGato = Gato("Azrael", 15) 
miPato = Pato("Daffy", 2)
miInsecto = Insecto("Polilla", 1)

# Acceder a los atributos y metodos de las subclases
print(f"{miPerro.nombre} tiene {miPerro.edad} y hace {miPerro.emitir_sonido()}")
print(f"{miGato.nombre} tiene {miGato.edad} y hace {miGato.emitir_sonido()}")
print(f"{miInsecto.nombre} tiene {miInsecto.edad} y hace {miInsecto.emitir_sonido()}")
