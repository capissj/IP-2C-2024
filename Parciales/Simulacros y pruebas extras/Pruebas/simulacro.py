# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion(s:list[int], e:int) -> int:
    res: int = -1
    for i in range(len(s)-1):
        if e == s[i] and res <= i:
            res = i
    return res

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def pertenece(s: list, e) -> bool:
    res: bool = False
    for elemento in s:
        if elemento == e:
            res = True
            break
    return res
"""
def eliminar_repetidos(s: list[int]) -> list[int]:
    lista_sin_repetidos: list[int] = []
    for numero in s:
        if not pertenece(lista_sin_repetidos, numero):
            lista_sin_repetidos.append(numero)
    return lista_sin_repetidos """
def elementos_exclusivos(s: list[int], t: list[int]) -> list[int]:
    lista_nueva: list[int] = []
    for i in range(len(s) - 1):
        if not pertenece(t, s[i]) and not pertenece(lista_nueva, s[i]):
            lista_nueva.append(s[i])
    for j in range (len(t) - 1):
        if not pertenece(s, t[j]) and not pertenece(lista_nueva, t[j]):
            lista_nueva.append(t[j])
    return lista_nueva

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res:int = 0
    for palabra in ingles.keys():
        if pertenece(aleman.keys(), palabra) and ingles[palabra] == aleman[palabra]:
            res += 1
    return res

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}

def cuantas_veces_aparece(n: int, l: list) -> int:
    res:int = 0
    for e in l:
        if e == n:
            res += 1
    return res
def convertir_a_diccionario(lista: list) -> dict:
    diccionario:dict = {}
    for e in lista:
        diccionario[e] = cuantas_veces_aparece(e,lista)
    return diccionario