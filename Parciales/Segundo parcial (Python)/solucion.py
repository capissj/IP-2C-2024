from queue import Queue as Cola
from queue import LifoQueue as Pila

# Ejercicio 1
def subsecuencia_mas_larga(v: list[int]) -> tuple[int,int]:
    longitud: int = len(v)
    lista_aux: list[int] = []
    indice: int = 0
    tuplas: list[tuple[int, int]] = []
    num: int = 0
    for contador in range(1, longitud, 1):
        if indice == contador - 1:
            lista_aux.append(v[indice])
        res: tuple[int, int] = [num, indice]
        lista_aux.append(v[contador])
        if todos_consecutivos(lista_aux):
            num = len(lista_aux)
            continue
        else:
            indice = contador
            lista_aux.clear()
            tuplas.append(res)
            res = [0, 0]
    if contador + 1 == longitud:
        indice = contador
        lista_aux.clear()
        tuplas.append(res)
        res = [0, 0]
    if len(tuplas) == 0:
        return res
    else:
        return maximo_tupla(tuplas)
def maximo_tupla(tuplas: list[tuple[int,int]]):
    maximo: int = 0
    res: tuple[int, int] = [0, 0]
    for i in tuplas:
        if i[0] >= res[0]:
            res = i
    return res
def todos_consecutivos(v: list[int]) -> bool:
    res: bool = False
    for i in range(len(v)-1):
        if v[i] == v[i+1] - 1:
            res = True
        else:
            res = False
            break
    return res
print (subsecuencia_mas_larga([1,2,4,5,6]))
# Ejercicio 2
def contador(examen: list[bool]) -> int:
    longitud: int = len(examen)
    verdaderas: bool = 0
    falsas: bool = 0
    res: int = 0
    for i in examen:
        if i == True:
            verdaderas += 1
        else:
            falsas += 1
    if verdaderas > longitud/2:
        res = longitud - (verdaderas - longitud/2)
    else:
        res = longitud - (falsas - longitud/2)
    return res

def mejor_resultado_de_ana(examenes: Cola[list[bool]]) -> list[int]:
    cola_Aux: Cola[list[bool]] = Cola()
    res: list[int] = []
    while not examenes.empty():
        auxiliar: list[bool] = examenes.get()
        cola_Aux.put(auxiliar)
        res.append(contador(auxiliar))
    while not cola_Aux.empty():
        examenes.put(cola_Aux.get())
    return res
# Ejercicio 3
def conjunto_matriz(matriz: list[list[int]]) -> list[int]:
    res: list[int] = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if not pertenece_lista(res, matriz[i][j]):
                res.append(matriz[i][j])
    return res
def pertenece_lista(lista: list[int], num:int) -> bool:
    res: bool = False
    for i in lista:
        if i == num:
            res = True
            break
    return res
def cambiar_matriz(A: list[list[int]]) -> None:
    auxiliar: list[list[int]] = A.copy()
    conjunto: list[int] = conjunto_matriz(auxiliar)
    longitud: int = len(conjunto) - 1
    contador: int = 0
    #A = A.clear()
    for i in range(len(auxiliar)):
        for j in range(len(auxiliar[0])):
            A[i][j] = conjunto[longitud - contador]
            contador += 1
    # return A (este return no deberia ir)
mas_filas = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
mas_columnas = [ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15] ]
#print(cambiar_matriz(mas_filas))
cambiar_matriz(mas_columnas)
print( mas_columnas )
#print(cambiar_matriz([[]]))

# Ejercicio 4
def pertenece_str(lista: list[str], caracter: str) -> bool:
    res: bool = False
    for i in lista:
        if i == caracter:
            res = True
            break
    return res
def quitar_str(palabras: list[str], caracter:str) -> list[str]:
    res: list[str] = []
    for palabra in palabras:
        if palabra != caracter:
            res.append(palabra)
    return res
def contador_vocales(palabra: str) -> int:
    vocales: list[str] = ["a","e","i","o","u","A","E","I","O","U"]
    contador: int = 0
    for letra in palabra:
        if pertenece_str(vocales, letra):
            contador += 1
    return contador
def separa_texto_en_palabras(texto: str) -> list[str]:
    palabras: list[str] = []
    palabra: str = ""
    for letra in texto:
        if letra != " ":
            palabra += letra
        else:
            if len(palabra) != 0:
                palabras.append(palabra)
            palabra = ""
    #if len(palabra) != 0:
    #    palabras.append(palabra)  
    return palabras
texto = "Hola Como  estas"
print (separa_texto_en_palabras(texto))

def palabras_por_vocales(texto: str) -> dict[int, int]:
    auxiliar: str = texto
    res: dict[int, int]
    return {}
