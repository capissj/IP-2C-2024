from queue import Queue as Cola
import math
# Ejercicio 1
def gestion_notas(notas_estudiante_materia: list[tuple[str, str, int]]) -> dict[str, list[tuple[str,int]]]:
    return {} 
 
# Ejercicio 2
def cantidad_digitos_pares(numeros: list[int]) -> int:
    contador: int = 0
    for i in numeros:
        while i > 0:
            if ultimo_digito(i) % 2 == 0:
                i = i // 10
                contador += 1
            else:
                i = i // 10
    return contador
def cant_digitos(numero: int) -> int:
    contador: int = 1
    while numero >= 10:
        numero = numero // 10
        contador += 1
    return contador
def ultimo_digito(numero: int) ->int:
    ultimo: int = numero % 10
    return ultimo
# Ejercicio 3 (Corregido)
def reordenar_cola_primero_pesados(paquetes: Cola[tuple[str,int]], umbral:int) -> Cola[tuple[str,int]]:
    res: Cola[tuple[str,int]] = Cola()
    cola_aux : Cola[tuple[str,int]] = Cola()
    cola_umbral: Cola[tuple[str,int]] = Cola()
    while not paquetes.empty():
        auxiliar: tuple[str,int] = paquetes.get()
        cola_aux.put(auxiliar)
        if auxiliar[1] > umbral:
            res.put(auxiliar)
        else:
            cola_umbral.put(auxiliar)
    while not cola_aux.empty():
        paquetes.put(cola_aux.get())
    while not cola_umbral.empty():
        res.put(cola_umbral.get())
    return res

        
# Ejercicio 4
def matriz_pseudo_ordenada(matriz: list[list[int]]) -> bool:
    longitud: int = len(matriz)
    res: bool = True
    return res
def ordenados(columna: list[int]) -> bool:
    res: bool = True
    for i in range(len(columna)-1):
        if columna [i] > columna [i+1]:
            res = False
            break
    return res

