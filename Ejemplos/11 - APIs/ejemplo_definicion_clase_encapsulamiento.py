class Persona:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad

    def dameNombre(self):
        return self.__nombre

    def dameEdad(self):
        return self.__edad

    def definirNombre(self, nombre: str = "Héctor"):
        self.__nombre = nombre

    def definirEdad(self, edad: int):
        self.__edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.__nombre} y mi edad es {self.__edad}")

persona1 = Persona("Pablo", 30)
persona1.presentarse()
#print(persona1.__nombre) #Esto da error, no se puede acceder directamente 
print(persona1.dameNombre())
persona1.definirNombre("Pepe")
print(persona1.dameNombre())
persona1.__nombre = "Juan"
a = "Juan"
persona1.definirNombre("María")
print(persona1.dameNombre())