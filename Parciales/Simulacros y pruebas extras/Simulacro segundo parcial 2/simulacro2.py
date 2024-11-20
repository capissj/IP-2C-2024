#1) Índice de la n-ésima aparición [2 puntos]
#Guido y Marcela son dos estudiantes de IP, nervioses con el parcial de Python. 
#Con el objetivo de tener un rato antes del parcial para preguntarse algunas dudas 
#deciden encontrarse en el colectivo y viajar juntes. 
#Para poder coordinar de forma exacta en qué colectivo se tienen que subir, 
#Marcela usa sus habilidades de programación aprendidas en IP para acceder de forma 
#poco legítima a la base de datos de colectivos de todas las empresas. 
#Con esto, arma una lista de todos los colectivos que van a pasar por la parada de
#Guido alrededor del horario acordado y le indica a Guido que se tiene que subir en 
#el 3er colectivo de la línea 34. Por desgracia, Guido se olvida sus lentes antes 
#de salir y no es capaz de distinguir a qué línea pertenece cada colectivo que 
#llega a la parada. Por lo que solo puede contar cantidad total de colectivos que 
#pasan.
#Implementar la función ind_nesima_aparicion que dada una secuencia de enteros s, 
#y dos enteros n y elem devuelve la posición en la cual elem aparece por n-ésima vez 
#en s. En caso de que elem aparezca menos de n veces en s, devolver -1.

#problema ind_nesima_aparicion (in s: seq⟨Z⟩, in n: Z, in elem: Z) : Z {
#  requiere: {n>0}
#  asegura: {Si el elemento aparece menos de n veces en la secuencia, res= -1 }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, s[res] = elem }
#  asegura: {Si el elemento aparece al menos n veces en la secuencia, elem aparece n-1 veces en s entre las posiciones 0 y res-1 }
# }
#Por ejemplo, dadas
#s = [-1, 1, 1, 5, -7, 1, 3]
#n = 2
#elem = 1
#se debería devolver res = 2
def pertenece(s: list, elem) -> bool:
    res: bool = False
    for i in s:
        if i == elem:
            res = True
            break
    return res
def contador(s: list[int], elem: int) -> int:
    cont: int = 0
    for numero in s:
        if numero == elem:
            cont += 1
    return cont
def ind_nesima_aparicion(s: list, n: int, elem: int) -> int:
    apariciones: int = 0
    for i in range(len(s)-1):
        if contador(s, elem) < n:
            return -1
        if s[i] == elem:
            apariciones += 1
            if apariciones == n:
                return s[i]
print (ind_nesima_aparicion([-1, 1, 1, 5, -7, 1, 3],2,1))

#2) Mezclar [2 puntos]
#A la hora de jugar juegos de cartas, como el truco, el tute, o el chinchón, 
#es importante que la distribución de las mismas en el mano sea aleatoria. 
#Para esto, al comienzo de cada mano, antes de repartir las mismas se realizan 
#mezclan sucesivas. Una técnica de mezclado es la denominada "mezcla americana" 
#que consiste en separar el mazo en (aproximadamente) dos mitades e intercalar 
#las cartas de ambas mitades. Implementar la función mezclar que dadas dos listas 
#s1 y s2 con igual cantidad de elementos devuelva una lista con los elementos 
#intercalados. Esto es, las posiciones pares de res tendrán los elementos de s1 
#y las posiciones impares los elementos de s2, respetando el orden original.

#problema mezclar (in s1: seq⟨Z⟩, in s2: seq⟨Z⟩) : seq⟨Z⟩ {
#  requiere: {|s1| = |s2| }
#  asegura: {|res| = 2 * |s1|}
#  asegura: {res[2*i] = s1[i] y res[2*i+1] = s2[i], para i entre 0 y |s1|-1}
#}
#TIP: realizar la iteración mediante índices y no mediante elementos

#Por ejemplo, dadas
#s1 = [1, 3, 0, 1]
#s2 = [4, 0, 2, 3]
#se debería devolver res = [1, 4, 3, 0, 0, 2, 1, 3]

def mezclar(s1: list[int], s2: list[int]) -> list[int]:
    res: list[int] = []
    lis1: list[int] = s1.copy()
    lis2: list[int] = s2.copy()
    indice_1: int = 0
    indice_2: int = 0
    for i in range(len(s1)-1):
        if i % 2 == 0:
            for n1 in lis1:
                res.append(n1)
        else:
            for n2 in lis2:
                res.append(n2)
    return res
print (mezclar([1, 3, 0, 1], [4,0,2,3]))