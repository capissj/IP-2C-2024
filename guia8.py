from queue import LifoQueue as Pila
import random
# Funciones de la practica
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
"""
pila_prueba : Pila[int] = generar_numero_al_azar(2,1,20)
mostrar_pila (pila_prueba) """
#Ej 10
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
pila_ej10 : Pila[int] = Pila()
pila_ej10.put(1)
pila_ej10.put(10)
pila_ej10.put(5)
pila_ej10.put(78)
pila_ej10.put(5)
buscar_el_maximo(pila_ej10)
mostrar_pila(pila_ej10) """
from queue import Queue as Cola
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
def calcular_promedio_por_estudiante(notas : list[tuple[str, float]]) -> dict[str, float]:
    d : dict[str, float] = {}
    for tupla in notas:
        if tupla[0] in d:
            
        else:
