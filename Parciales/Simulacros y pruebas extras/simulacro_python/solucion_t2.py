from queue import Queue as Cola

# Ejercicio 1
def gestion_ventas(ventas_empleado_producto: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    res:dict = {}
    for n, p, c in ventas_empleado_producto:
        ventas_por_vendedor:list
        if (n in res.keys()):
            ventas_por_vendedor = res.get(n)
        else:
            ventas_por_vendedor = []
            res[n] = ventas_por_vendedor
        ventas_por_vendedor.append((p, c))
    return res 


# Ejercicio 2
def cantidad_digitos_impares(numeros: list[int]) -> int:
    res:int = 0
    for n in numeros:
        res += cantidad_digitos_impares_en_entero(n)
    return res

def cantidad_digitos_impares_en_entero(n: int):
    cantidad:int = 0
    while (n > 0):
        d:int = digito_unidades(n)
        if (es_impar(d)):
            cantidad += 1
        n = numero_sin_unidades(n)
    return cantidad

def numero_sin_unidades(n) -> int:
    return (n // 10)

def digito_unidades(n) -> bool:
    return n%10

def es_impar(n :int) -> bool:
    return n % 2 == 1

# Ejercicio 3
def reordenar_cola_primero_numerosas(carpetas: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    res:Cola = Cola()
    cola_temp:Cola = Cola() #para luego restarurar carpetas que es IN

    menores_o_iguales_umbral:list = []
    mayores_umbral:list = []

    while not (carpetas.empty()):
        carpeta = carpetas.get()
        if (carpeta[1] > umbral): 
            mayores_umbral.append(carpeta)
        else:
            menores_o_iguales_umbral.append(carpeta)

        cola_temp.put(carpeta) #para luego restarurar carpetas que es IN

    for e in mayores_umbral:
        res.put(e)
    for e in menores_o_iguales_umbral:
        res.put(e)
    
    #restaruro carpetas que es IN
    while not (cola_temp.empty()):
        v = cola_temp.get()
        carpetas.put(v)

    return res

# Ejercicio 4
def maximo(l: list[int]) -> int:
    res:int = l[0]
    for n in l:
        if n > res:
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

def matriz_cuasi_decreciente(matriz: list[list[int]]) -> bool:
    # Tiempo utilizado: 35 minutos
    res: bool = True
    
    columnas: list[list[int]] = obtener_columnas(matriz)
    maximo_col_i: int = maximo(columnas[0])
    res: bool = True
    col_actual: int = 1
    while (res and col_actual < len(columnas)):
        maximo_col_i_mas_1: int = maximo(columnas[col_actual])
        res = (maximo_col_i > maximo_col_i_mas_1)
        col_actual += 1
        maximo_col_i = maximo_col_i_mas_1
        
    return res
