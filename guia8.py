from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
# Funciones de la practica
""" #Pila de prueba, copiar esto y pegar cuando se necesite :P
pila_prueba = Pila()
pila_prueba.put(5)
pila_prueba.put(5)
pila_prueba.put(8)
pila_prueba.put(4)
print (cantidad_elementos(pila_prueba))
mostrar_pila(pila_prueba)
"""
# PILAS
#Ej 1
def generar_numero_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    p:Pila[int] = Pila()
    for i in range(cantidad):
        p.put(random.randint(desde, hasta))
    return p
# El print comun y corriente no funciona, asi que creo uno que se llama "mostrar_pila"
def mostrar_pila(p:Pila[int]) -> None:
    s: Pila[int] = Pila()
    while not p.empty():
        elem:int = p.get()
        print (elem)
        s.put(elem)
    while not s.empty():
        p.put(s.get())
#Ej 2
def cantidad_elementos(p:Pila) -> int:
    pAux: Pila = Pila()
    contador: int = 0
    while  not p.empty():
        pAux.put(p.get())
        contador += 1
    while not pAux.empty():
        p.put(pAux.get())
    return contador
"""
pila_prueba : Pila[int] = generar_numero_al_azar(2,1,20)
mostrar_pila (pila_prueba) """
#Ej 3
def buscar_el_maximo(p:Pila[int]) -> int:
    pAux: Pila[int] = Pila()
    maximo: int = p.get()
    pAux.put(maximo)
    while not p.empty():
        actual: int = p.get()
        if maximo < actual:
            maximo = actual
        pAux.put(actual)
    while not pAux.empty():
        p.put(pAux.get())
    return maximo
"""
pila_ej3 : Pila[int] = Pila()
pila_ej3.put(1)
pila_ej3.put(10)
pila_ej3.put(5)
pila_ej3.put(78)
pila_ej3.put(5)
buscar_el_maximo(pila_ej3)
mostrar_pila(pila_ej3) """
#Ej 4
def buscar_nota_maximo(p:Pila[tuple[str,int]]) -> tuple[str,int]:
    pAux: Pila[tuple[str,int]] = Pila()
    tupla_maxima: tuple[str,int] = p.get()
    pAux.put(tupla_maxima)
    while not p.empty():
        actual: tuple[str,int] = p.get()
        if tupla_maxima[1] < actual[1]:
            tupla_maxima = actual
        pAux.put(actual)
    while not pAux.empty():
        p.put(pAux.get())
    return tupla_maxima
#Ej 5 no lo entiendo xD
#Ej 6
#Ej 7
def intercalar(p1:Pila, p2:Pila) -> Pila:
    res: Pila = Pila()
    pAux1: Pila = Pila()
    pAux2: Pila = Pila()
    while not p2.empty():
        elem1 = p1.get()
        pAux1.put(elem1)
        res.put(elem1)
        elem2 = p2.get()
        pAux2.put(elem2)
        res.put(elem2)
    while not pAux2.empty():
        p1.put(pAux1.get())
        p2.put(pAux2.get())
    return res
"""
pila_prueba = Pila()
pila_prueba.put(5)
pila_prueba.put(5)
pila_prueba.put(8)
pila_prueba.put(4)
pila_prueba2 = Pila()
pila_prueba2.put(10)
pila_prueba2.put(15)
pila_prueba2.put(25)
pila_prueba2.put(35)
intercalar(pila_prueba, pila_prueba2)
mostrar_pila(pila_prueba) """
# COLAS je
# El print comun y corriente no funciona, asi que creo uno que se llama "mostrar_cola"
def mostrar_cola(c:Cola[int]) -> None:
    s: Cola[int] = Cola()
    while not c.empty():
        elem:int = c.get()
        print (elem)
        s.put(elem)
    while not s.empty():
        c.put(s.get())
#Bingo
def armar_secuencia_de_bingo() -> Cola[int]:
    c: Cola[int] = Cola()
    lista: list[int] = range(100)
    random.shuffle(lista)
    for numero in lista:
        c.put(numero)
    return c
def quitar(s:list[int], x:int) -> list[int]:
    nueva_lista: list[int] = []
    for i in range(len(s)):
        if x != s[i]:
            nueva_lista.append(s[i])
    return nueva_lista
def pertenece(s:list[int], x:int) -> bool:
    for i in range(len(s)):
        if s[i] == x:
            return True
    return False
def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    cAux: Cola[int] = Cola()
    contador: int = 0
    while len(carton) != 0:
        bola: int = bolillero.get()
        if pertenece(carton, bola):
            quitar(carton, bola)
            contador += 1
            cAux.put(bola)
        else:
            contador += 1
            cAux.put(bola)
    return contador
# Diccionarios?
# Ej 16
def agrupar_por_longitud(nombre_archivo: str) -> dict:
    res: dict[int, int] = ()

    archivo: TextIO = open(nombre_archivo, "r")
    contenido : list[str] = archivo.readlines()
    archivo.close()

    for line in contenido:
        palabras_lista: list[str] = palabras(line)
        for p in palabras_lista:
            largo: int = len(p)
            if pertenece(list(res.keys()), largo):
                res[largo] = res[largo] + 1
            else:
                res[largo] = 1

    return res
def palabras(s:list[str]) -> list[str]:
    return s.split(" ") #TODO implementar
# Ej 18
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    res: dict [str, int] = ()

    archivo: TextIO = open(nombre_archivo, "r")
    contenido : list[str] = archivo.readlines()
    archivo.close()

    for linea in contenido:
        palabras_lista: list[str] = palabras(linea)

        for p in palabras_lista:
            if pertenece (list(res.keys()),p):
                res[p] = res[p] + 1
            else:
                res[p] = 1
    maximo: int = 0
    mas_frecuente: str = ""
    for key, value in res:
        if value > maximo:
            maximo = value
            mas_frecuente = key

    return mas_frecuente
def calcular_promedio(alumno: str, notas:list[tuple[str, float]]) -> float:
    cant_notas: int = 0
    suma_notas: int = 0
    for nota in notas:
        if nota[0] == alumno:
            cant_notas += 1
            suma_notas += notas[1]
    return suma_notas / cant_notas
"""
def calcular_promedio_por_estudiante(notas : list[tuple[str, float]]) -> dict[str, float]:
    d : dict[str, float] = {}
    for tupla in notas:
        if not tupla[0] in d:
            d(tupla[0]) = calcular_promedio(tupla[0], notas)
    return d
"""
#Archivos
# Ej 21 1
def contar_linea(nombre_archivo: str) -> int:
    res:int = 0
    archivo = open(nombre_archivo, "r")
    contenido: list[str] = archivo.readlines()
    archivo.close()
    res = len(contenido)
    return res
# Ej 22 
"""
def clonar_sin_comentarios(nombre_archivo_entrada: str) -> str:
    nombre_archivo_salida: str = "salida.txt"
    archivo: TextIO = open(nombre_archivo_entrada, "r")
    contenido: list[str] = archivo.readlines()
    for i in range(len(contenido)):
        linea: str = archivo.realine()
        for n in linea:
            if n == "#":
                """
