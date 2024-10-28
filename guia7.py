import math
#Punto 1 1
def pertenece(lista:list[int], x:int) -> bool:
    return lista.count(x) != 0
def pertenece2(s:list[int], x:int) -> bool:
    for i in range(len(s)):
        if s[i] == x:
            return True
    return False
#Punto 1 2
def divide_a_todos(s:list[int], e:int) -> bool:
    for i in s:
        if i % e != 0:
            return False
            break
    return True
#Punto 1 3
def suma_total(lista:list[int]) -> int:
    suma:int = 0
    for i in lista:
        suma += i
    return suma
#Punto 1 4
def maximo(lista:list[int]) -> int:
    elemento:int = lista[0]
    for i in lista:
        if i > elemento:
            elemento = i
    return elemento
#Punto 1 5
def minimo(lista:list[int]) -> int:
    elemento:int = lista[0]
    for i in lista:
        if i < elemento:
            elemento = i
    return elemento
#Punto 1 6
def ordenados(lista:list) -> bool:
    resultado = True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            resultado = False
            break
    return resultado
#Punto 1 7
def pos_maximo(s:list[int]) -> int:
    maximus = 0
    for i in s:
        if maximo(s) != i:
            maximus += 1
        else:
            return maximus
#Punto 1 8
def pos_minimo(s:list[int]) -> int:
    minimus = 0
    for i in s:
        if minimo(s) != i:
            minimus += 1
        else:
            return minimus
#Punto 1 9
def siete_caracteres(s:list[str]) -> bool:
    resultado = False
    for i in range(len(s)-1):
        if len(s[i]) >= 7:
            resultado = True
            break
    return resultado
#Punto 1 10

#Punto 2 1
def ceros_en_posiciones_pares(s:list[int]):
    for i in range(len(s)):
        if i % 2 == 0:
            s[i] = 0
#Punto 2 2
def ceros_en_posiciones_pares2(s:list[int]) -> list[int]:
    t = s.copy
    for i in range(len(t)):
        if i % 2 == 0:
            t[i] = 0
    return t

