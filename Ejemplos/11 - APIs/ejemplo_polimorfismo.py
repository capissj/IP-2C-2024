class Animal:

    def __init__(self, nombre: str , edad: int, sonido: str):
        self.nombre = nombre
        self.edad = edad 
        self.sonido = sonido   
    
    def emitir_sonido(self):
        return self.sonido

class Perro(Animal):
    def __init__(self, nombre: str , edad: int, sonido: str = "Guau"):
        #self.nombre = nombre
        #self.edad = edad 
        #self.sonido = sonido   
        super().__init__(nombre, edad, sonido)
        
    #def emitir_sonido(self):
    #    return self.sonido

class Gato(Animal):
    #def emitir_sonido(self):
    #    return "Miau!"
    pass

# Funcion que utiliza polimorfismo
def hacer_emitir_sonido(animal):
    return animal.emitir_sonido()

# Crear instancias de diferentes animales
miPerro = Perro("Dylan", 10)
miPerro2 = Perro("Connan", 10, "Guau, guau!")
miGato = Gato("Azrael", 15, "Miau") 
miGato2 = Gato("Michu", 15, "Miaou") 

# Llamar a la funcion polimorfica con diferentes instancias
print(hacer_emitir_sonido(miPerro))  # Imprime "Guau!"
print(hacer_emitir_sonido(miPerro2))  # Imprime "Guau!"
print(hacer_emitir_sonido(miGato))   # Imprime "Miau!"
print(hacer_emitir_sonido(miGato2))   # Imprime "Miau!"
