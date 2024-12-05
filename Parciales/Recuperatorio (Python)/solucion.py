from queue import Queue as Cola

# Ejercicio 1
def maximas_cantidades_consecutivos (v: list[int]) -> dict[int,int]:
    res: dict[int, int] = {}
    for i in v:
        if not pertenece_enteros(res.keys(), i):
            res[i] = apariciones_consecutivas(v, i)
    return res
def apariciones_consecutivas(s: list[int], elem: int) -> int:
    actual: int = 1
    maximo: int = 1
    for i in range(len(s)-1):
        if s[i] == s[i + 1] and s[i] == elem:
            actual += 1
        else:
            if actual > maximo:
                maximo = actual
                actual = 1
    if actual > maximo:
        maximo = actual
    return maximo
def pertenece_enteros(s: list[int], elem: int) -> bool:
    res: bool = False
    for i in s:
        if i == elem:
            res = True
            break
    return res
#s = [1,1,2,3,4,4,5,5,7,7,30,30,30,7,8,8]
#print (maximas_cantidades_consecutivos(s))
# Ejercicio 2
def maxima_cantidad_primos( A: list[list[int]]) -> int:
    res: int = 0
    actual: int = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if es_primo(A[j][i]):
                actual += 1
        if actual > res:
            res = actual
            actual = 0
        else:
            actual = 0
    return res
def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for divisor in range(2,n-1,1):
        if n % divisor  == 0:
            return False
    return True
#A = [[7,1,1],[2,1,1],[5,1,1]]
#print(maxima_cantidad_primos(A))
# Ejercicio 3
def tuplas_positivas_y_negativas(c: Cola[tuple[int, int]]) -> None:
    lista_positivos: list[tuple[int, int]] = []
    lista_negativos: list[tuple[int, int]] = []
    lista_nulos: list[tuple[int, int]] = []
    while not c.empty():
        auxiliar: tuple[int, int] = c.get()
        if auxiliar[0] * auxiliar[1] > 0:
            lista_positivos.append(auxiliar)
        elif auxiliar[0] * auxiliar[1] < 0:
            lista_negativos.append(auxiliar)
        else:
            lista_nulos.append(auxiliar)
    for i in lista_positivos:
        c.put(i)
    for i in lista_negativos:
        c.put(i)
def imprimir_cola(c: Cola[tuple[int, int]]) -> None:
    cola_aux: Cola[tuple[int, int]] = Cola()
    while not c.empty():
        auxiliar: tuple[int, int] = c.get()
        print(auxiliar)
        cola_aux.put(auxiliar)
    while not cola_aux.empty():
        c.put(cola_aux.get())

#c = Cola()
#c.put([4,5])
#c.put([0,5])
#c.put([-4,5])
#c.put([4,0])
#c.put([4,-5])
#c.put([5,4])
#print (imprimir_cola(c))
#print("########################")
#tuplas_positivas_y_negativas(c)
#print(imprimir_cola(c)) #"""
# Ejercicio 4
def resolver_cuenta(s: str) -> float:
    res: float = 0
    numeros: str = ""
    lista: list[str] = ["0","1","2","3","4","5","6","7","8","9"]
    for caracter in s:
        if (caracter == "+" or caracter == "-") and numeros != "":
            res = res + float(numeros)
            numeros: str = ""
            numeros += caracter
        else:
            numeros += caracter
    if len(numeros) > 0:
        res = res + float(numeros)
    return res
#print(resolver_cuenta("10-20.5"))
