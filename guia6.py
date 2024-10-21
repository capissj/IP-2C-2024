import math

#Punto 1 1
def imprimir_hola_mundo():
    print("Hola Mundo")

#Punto 1 3
def raizDeDos() -> float:
    print (round (math.sqrt (2),4))

#Punto 1 4
def factorial_2() -> int:
    print (2)

#Punto 1 5
def perimetro() -> float:
    print (round (2 * math.pi, 8))

#Punto 2 1
def imprimir_saludo(nombre: str):
    print ("Hola", nombre)

#Punto 2 2
def raiz_cuadrada(x: int) -> float:
    return math.sqrt (x)

#Punto 2 3
def fahrenheit_a_celcius(x: float) -> float:
    return (x - 32) * 5/9 

#Punto 2 4
def imprimir_dos_veces(estribillo: str) -> str:
    print (estribillo + " " + estribillo)

#Punto 2 5 
def es_multiplo_de(x: int, y: int) -> bool:
    if x < y or y == 0:
        return False
    elif x % y == 0:
        return True
    else:
        return False

#Punto 2 6
def es_par(n: int) -> bool:
    return es_multiplo_de(n, 2)

#Punto 2 7
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    return round ((comensales * min_cant_de_porciones) / 8, 0) + 1

#Punto 3 1
def alguno_es_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 or numero2 == 0

#Punto 3 2
def ambos_son_0(numero1: float, numero2: float) -> bool:
    return numero1 == 0 and numero2 == 0

#Punto 3 3
def es_nombre_largo(nombre: str) -> bool:
    return len(nombre) <= 8 and len(nombre) >= 3

#Punto 3 4
def es_bisiesto(a: int) -> bool:
    return es_multiplo_de(a,4) and (es_multiplo_de(a,400) or not es_multiplo_de(a,100))

#Punto 4 1
def peso_pino(m: int) -> int:
    m = m * 100
    if m > 300:
        return 300 * 3 + (m-300) * 2
    else:
        return m * 3

#Punto 4 2
def es_peso_util(m: int) -> bool:
    return m >= 400 and m <= 1000

#Punto 4 3 y 4 4
def sirve_pino(l: int) -> bool:
    return es_peso_util (peso_pino (l))

#Punto 5 1
def el_doble_si_es_par(n: int) -> int:
    if n % 2 == 0:
        return n*2
    else:
        return n

#Punto 5 2
def convierte_en_pares(n: int) -> int:
    if n % 2 == 0:
        return n
    else:
        return n + 1

#Punto 5 3
def multi_9_y_3(n: int) -> int:
    if n % 9 == 0:
        return  n * 3
    elif n % 3 == 0:
        return n * 2
    else:
        return n

#Punto 5 4
def longitud_nombre(nombre: str):
    if len(nombre) >= 5:
        print ("Tu nombre tiene muchas letras")
    else:
        print("Tu nombre tiene menos de 5 letras!")

#Punto 5 5
def en_rango(n: int):
    if n < 5:
        print ("Menor a 5")
    elif n >= 10 and n <= 20:
        print ("Entre 10 y 20")
    elif n > 20:
        print("Mayor a 20")
    else:
        print("No está en rango")

#Punto 5 6
def vacaciones(sexo: str, edad: int):
    if sexo == "F" and (edad < 18 or edad >= 60):
        print ("Andá de vacaciones") 
    elif sexo == "M" and (edad < 18 or edad >= 65):
        print ("Andá de vacaciones")
    else:
        print ("Te toca trabajar")

#Punto 6 1
def uno_al_diez() -> int:
    n:int = 1
    while n <= 10:
        print (n)
        n= n+1 

#Punto 6 2
def pares_del_10_al_40() -> int:
    n:int = 10
    while (n <= 40):
        print (n)
        n = n + 2

#Punto 6 3
def eco() -> str:
    n:int = 0
    while n < 10:
        print("eco")
        n+=1

#Punto 6 4
def cuenta_regresiva(n: int):
    while (n >= 1):
        print (n)
        n = n - 1
    print ("Despegue")

#Punto 6 5
def viaje_al_pasado(partida: int, llegada: int):
    while partida > llegada:
        partida -= 1
        print ("Viajó un año al pasado, estamos en el año:", partida)

#Punto 6 6
def aristoteles(partida: int):
    llegada: int = -384
    while llegada <= partida:
        partida -= 20
        print ("Viajó 20 años al pasado, estamos en el año:", partida)

#Punto 7 1
def cuenta_1_10() -> int:
    for i in range(1,11):
        print (i)

#Punto 7 2
def diez_cuarenta_pares() -> int:
    for i in range (10,41,2):
        print (i)

#Punto 7 3
def eco_for() -> str:
    for i in range(10):
        print("eco")

#Punto 7 4
def despegue(x: int):
    for i in range(x,0,-1):
        print(i)
    print("Despegue")

#Punto 7 5
def viaje_un_ano_atras(partida: int, llegada: int):
    for i in range(partida,llegada - 1,-1):
        print("Viajó un año al pasado, estamos en el año:", i)
    
#Punto 7 6
def viaje_a_aristoteles(partida: int):
    llegada: int = - 384
    for i in range(partida, llegada, -20):
        print("Viajó 20 años al pasado, estamos en el año:", i)
"""
#Punto 8
x=5 ; y=7; x = x + y

x=5 ; y=7 ; z=x+y; y = z * 2

x=5 ; y=7 ; x="hora"; y = x * 2

x=False ; res=not(x)

x=False ; x=not(x)

x=True ; y=False ; res=x and y; x = res and x

"""
#Punto 9
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g
g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g
