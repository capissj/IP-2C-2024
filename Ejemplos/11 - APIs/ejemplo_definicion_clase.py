class Persona:
    def __init__(self, nombre: str, edad:int):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y mi edad es {self.edad}")
        

