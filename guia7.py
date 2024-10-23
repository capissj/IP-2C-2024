import math
#Punto 1 1
def pertenece(lista:list[int], x:int) -> bool:
    return lista.count(x) != 0
def pertenece2(lista:list[int], x:int) -> bool:
    for i in range(len(s)):
        if lista[i] == 0:
            return True
    return False
#Punto 1 2
def divide_a_todos(s:list[int], e:int) -> bool:
    for i in s:
        if i % e != 0:
            return False
            break
    return True
print (divide_a_todos([2,4,6,8,10],2))

#Punto 1 3
def suma_total(lista:list) -> int:
    suma:int = 0
    for i in lista:
        suma += i
    return suma
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

