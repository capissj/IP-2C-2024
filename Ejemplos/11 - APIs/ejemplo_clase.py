class Persona:
    def __init__(self, nombre: str = "Pablo", edad:int = 40):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y mi edad es {self.edad}")
        
        
# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("Pepe")

# Acceder a los atributos de la instancia
print(persona1.nombre)  # Imprime "Juan"
print(persona1.edad)    # Imprime 30
persona1.edad = 20

# Utilizar los metodos de una clase
persona1.presentarse() # Imprime "Hola, mi nombre es Juan y mi edad es 20"
persona2.presentarse() # Imprime "Hola, mi nombre es Pablo y mi edad es 40"
