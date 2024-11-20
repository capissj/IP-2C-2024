from queue import Queue as Cola

# Ejercicio 1
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    # Tiempo utilizado: 30 minutos

    notas: dict[str, list[tuple[str,int]]] = {}
    
    for estudiante, materia, nota in notas_estudiante_materia:
        if estudiante in notas:
            notas[estudiante].append((materia, nota))
        else:
            notas[estudiante] = [(materia, nota)]
    
    return notas
 
# Ejercicio 2
def cantidad_digitos_pares(numeros: list[int]) -> int:
    res:int = 0
    for n in numeros:
        res += cantidad_digitos_pares_en_entero(n)
    return res

def cantidad_digitos_pares_en_entero(n: int) -> int:
    cantidad:int = 0
    if n == 0:
        cantidad += 1
    while (n > 0):
        d:int = digito_unidades(n)
        if (es_par(d)):
            cantidad += 1
        n = numero_sin_unidades(n)
    return cantidad

def numero_sin_unidades(n) -> int:
    return (n // 10)

def digito_unidades(n) -> bool:
    return n%10

def es_par(n :int) -> bool:
    return n % 2 == 0

# Ejercicio 3
def copiar_cola(c: Cola):
    copia = Cola()
    aux = Cola()
    
    while not c.empty():
        e = c.get()
        copia.put(e)
        aux.put(e)
    
    while not aux.empty():
        e = aux.get()
        c.put(e)
    
    return copia

def reordenar_cola_primero_pesados(paquetes: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    # Tiempo utilizado: 35 minutos
    _paquetes = copiar_cola(paquetes)
    res = Cola()
    livianos = []
    while not _paquetes.empty():
        paquete = _paquetes.get()
        if paquete[1] > umbral:
            res.put(paquete)
        else:
            livianos.append(paquete)
    
    for paquete in livianos:
        res.put(paquete)
    
    return res

# Ejercicio 4
def minimo(l: list[int]) -> int:
    res:int = l[0]
    for n in l:
        if n < res:
            res = n
    return res

def obtener_columnas(m: list[list[int]]) -> list[list[int]]:
    columnas = []
    cant_columnas = len(m[0])
    for col in range(cant_columnas):
        columna = obtener_columna(m, col)
        columnas.append(columna)
    return columnas

def obtener_columna(m, col):
    columna: list[int] = []
    cant_filas = len(m)
    for fila in range(cant_filas):
        columna.append(m[fila][col])
    return columna

def matriz_pseudo_ordenada(matriz: list[list[int]]) -> bool:
    # Tiempo utilizado: 35 minutos
    res: bool = True
    
    columnas: list[list[int]] = obtener_columnas(matriz)
    minimo_col_i: int = minimo(columnas[0])
    res: bool = True
    col_actual: int = 1
    while (res and col_actual < len(columnas)):
        minimo_col_i_mas_1: int = minimo(columnas[col_actual])
        res = (minimo_col_i < minimo_col_i_mas_1)
        col_actual += 1
        minimo_col_i = minimo_col_i_mas_1
        
    return res
