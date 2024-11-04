import math
#Punto 1 1
def pertenece(lista:list[int], x:int) -> bool:
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
        if len(s[i]) > 7:
            resultado = True
            break
    return resultado
#Punto 1 10
#Punto 1 11
def consecutivos_iguales(s:list[int]) -> bool:
    for i in range(len(s)):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            return True
    return False
#Punto 1 12
def tres_vocales(s:str) -> bool:
    vocales: str = "aeiouAEIOU"
    contador_vocales: int = 0
    for i in range(len(s)):
        if s[i] in vocales:
            contador_vocales += 1
    return contador_vocales >= 3
#Punto 1 13
#Punto 1 14
def cantidad_digitos_impares(s:list[int]) -> int:
    cantidad: int = 0
    for numero in s:
        while numero > 0:
            digito: int = numero % 10
            if digito % 2 != 0:
                cantidad += 1
            numero //= 10
    return cantidad
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
#Punto 2 3
def quitar_vocales(s:str) -> str:
    vocales: str = "aeiouAEIOU"
    string_sin_vocales:str = ""
    for i in range(len(s)):
        if not pertenece(vocales,s[i]):
            string_sin_vocales += s[i]
    return string_sin_vocales
#Punto 2 4
def reemplaza_vocales(s:str) -> str:
    vocales: str = "aeiouAEIOU"
    string_sin_vocale: str = ""
    for i in range(len(s)):
        if not pertenece(vocales, s[i]):
            string_sin_vocale += s[i]
        else:
            string_sin_vocale += "_"
    return string_sin_vocale
#Punto 2 5
def da_vuelta_string(s:str) -> str:
    nuevo_string: str = ""
    for i in range(len(s)-1,-1,-1):
        nuevo_string += s[i]
    return nuevo_string
#Punto 2 6
def eliminar_repetidos(s:str) -> str:
    res: str = ""
    for i in s:
        if not pertenece(res, i):
            res += i
    return res
#Punto 3
def problema_materia(s:int) -> int:
    aprobados:int = 0
    desaprobados:int = 0
    suma:int = 0
    for i in s:
        if i >= 4:
            aprobados += 1
        else:
            desaprobados +=1
        suma += i
    promedio:float = suma / (desaprobados + aprobados)
    if promedio >= 7 and desaprobados == 0:
        return 1
    elif desaprobados == 0:
        return 2
    else:
        return 3
#Punto 4
def calcular_saldo(s:list[tuple[str,int]]) -> float:
    saldo: float = 0
    for tipo, monto in s:
        if tipo == "I":
            saldo += monto
        elif tipo == "R":
            saldo -= monto
    return saldo
#Matrices
#Punto 5
def pertenece_a_cada_uno_version1(s:list[list[int]], x:int, res:list[bool]) -> None:
    res.clear()
    for i in s:
        res.append(pertenece(i, x))
def pertenece_a_cada_uno_version2(s:list[list[int]], x:int, res:list[bool]) -> None:
    res.clear()
    for i in s:
        res.append(pertenece(i, x))
def pertenece_a_cada_uno_version3(s:list[list[int]], x:int) -> list[bool]:
    res: list[bool] = []
    for i in s:
        res.append(pertenece(i, x))
    return res
#Punto 6 1
def es_matriz(s:list[list[int]]) -> bool:
    res: bool = True
    for i in range(len(s)-1):
        if len(s[i]) == len(s[i+1]):
            res = True
        else:
            res = False
            break
    return res
#Punto 6 2
def filas_ordenadas(m:list[list[int]], res:list[bool]):
    res.clear()
    for i in m:
        res.append(ordenados(i))
    return res
#Punto 6 3
