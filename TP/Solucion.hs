module Solucion where
-- Nombre del equipo: VMJ
-- Integrante 1: Jonathan Salomonsky
-- Integrante 2: Micaela Ramos
-- Integrante 3: Valentin Capart
type Ciudad = String
type Duracion = Float
type Vuelo = (Ciudad, Ciudad, Duracion)

type AgenciaDeViajes = [Vuelo]

-- Funciones auxiliares

origen :: Vuelo -> Ciudad
origen (x,_,_) = x
destino :: Vuelo -> Ciudad
destino (_,y,_) = y
duracion :: Vuelo -> Duracion
duracion (_,_,z) = z


-- EJERCICIO 1
vuelosValidos :: AgenciaDeViajes -> Bool -- Comprueba si los vuelos de una lista dada son válidos
vuelosValidos [] = True
vuelosValidos l | (validezVuelos l) && (vuelosChequeados l) = True
                | otherwise = False
-- Funciones auxiliares ej 1

contenido :: (Eq t) => t -> [t] -> Bool -- Te dice si un elemento pertenece a una lista
contenido _ [] = False
contenido e (x:xs) | e == x = True
                   | otherwise = contenido e xs
{-
verificarRepetidos :: AgenciaDeViajes -> Bool -- Chequea que no haya repetidos en una lista
verificarRepetidos [x] = True
verificarRepetidos (x:xs) | contenido x xs = False
                          | otherwise = verificarRepetidos xs -} -- No hace falta verificarRepetidos en el ejercicio 1, ya que vuelosChequeados ya cumple esa condicion :)

chequeoVuelo :: Vuelo -> AgenciaDeViajes -> Bool -- Verifica que si hay dos vuelos iguales con distinta o igual duracion no los cuente
chequeoVuelo (_,_,_) [] = True
chequeoVuelo (a,b,c) (x:xs) | (a == (origen x)) && (b == (destino x)) = False
                            | otherwise = chequeoVuelo (a,b,c) xs

vuelosChequeados :: AgenciaDeViajes -> Bool -- Verifica una lista de vuelos con las condiciones de chequeoVuelo
vuelosChequeados [x] = True
vuelosChequeados (x:xs) | chequeoVuelo x xs = vuelosChequeados xs
                        | otherwise = False

vueloValido :: Vuelo -> Bool -- Funcion que se fija si un vuelo cumple con los requisitos dados
vueloValido (x,y,d) | (x == y) || (d <= 0) = False
                    | otherwise = True

validezVuelos :: AgenciaDeViajes -> Bool -- Esta funcion mira si los vuelos de una lista son válidos
validezVuelos [] = True
validezVuelos (x:xs) | vueloValido x = validezVuelos xs
                     | otherwise = False


-- EJERCICIO 2
ciudadesConectadas :: AgenciaDeViajes -> Ciudad -> [Ciudad] -- Indica que ciudades estan conectadas a una ciudad dada
ciudadesConectadas [] e = []
ciudadesConectadas (x:xs) e | origen x == e = eliminarRepetidos ([destino x] ++ ciudadesConectadas xs e)
                            | destino x == e = eliminarRepetidos ([origen x] ++ ciudadesConectadas xs e)
                            | otherwise = ciudadesConectadas xs e
--Funciones auxiliares ej 2

quitarTodos :: (Eq t) => t -> [t] -> [t] -- Le das un elemento y quita todos los elementos que son iguales al elemento dado
quitarTodos e [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e (xs)
                     | otherwise = [x] ++ quitarTodos e xs

eliminarRepetidos :: (Eq t) => [t] -> [t] -- Elimina todos los elementos repetidos
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | contenido x xs = [x] ++ quitarTodos x (eliminarRepetidos xs)
                         | otherwise = [x] ++ eliminarRepetidos xs


-- EJERCICIO 3
modernizarFlota :: AgenciaDeViajes -> AgenciaDeViajes -- Mejora la duracion de los vuelos de una lista dada
modernizarFlota [] = []
modernizarFlota (x:xs) = [mejoraDeVuelo x] ++ modernizarFlota xs
-- Funciones auxiliares ej 3

mejoraDeVuelo :: Vuelo -> Vuelo -- Mejora un vuelo
mejoraDeVuelo (x,y,z) = (x,y,z - 1/10 *z)


-- EJERCICIO 4
ciudadMasConectada :: AgenciaDeViajes -> Ciudad -- Indica cual es la ciudad mas conectada
ciudadMasConectada [] = "Racing 4 - Paranaense 1"
ciudadMasConectada agencia = maximoTuplas (tuplaDeCiudades agencia)
--Funciones auxiliares ej 4

maximoTuplas :: [(Ciudad, Integer)] -> Ciudad -- Busca el maximo de todas las tuplas de tuplaDeCiudades
maximoTuplas [x] = fst x
maximoTuplas (x:y:xs) | snd x >= snd y = maximoTuplas (x:xs)
                      | otherwise = maximoTuplas (y:xs)

tuplaDeCiudades :: AgenciaDeViajes -> [(Ciudad, Integer)] -- Te arma una tupla con una ciudad y con la cantidad de vuelos que salen de esa ciudad y tambien con los vuelos que llegan a esa ciudad y su cantidad de vuelos
tuplaDeCiudades [] = []
tuplaDeCiudades (x:xs) = [((origen x), cantDeCiudades (x:xs) (origen x)), ((destino x), cantDeCiudades (x:xs) (destino x))] ++ tuplaDeCiudades xs

longitud :: [Ciudad] -> Integer -- Indica cuantas ciudades tiene una lista
longitud  [] = 0
longitud (x:xs) = 1 + longitud xs

cantDeCiudades :: AgenciaDeViajes -> Ciudad -> Integer -- Cantidad de ciudades a las que podes ir o volver a una ciudad elegida
cantDeCiudades [] _ = 0
cantDeCiudades agencia c = longitud (ciudadesConectadas agencia c)


-- EJERCICIO 5
sePuedeLlegar :: AgenciaDeViajes -> Ciudad -> Ciudad -> Bool -- Te indica si dados un origen y un destino podes llegar de uno a otro con como máximo una escala (GRAN FUNCION) :D
sePuedeLlegar [] _ _ = False
sePuedeLlegar (x:xs) o d | miroSiHayUnVuelo (x:xs) o d = True
                         | (origen x == o) && (contenido (destino x) interseca) = True
                         | (destino x == d) && (contenido (origen x) interseca) = True
                         | otherwise = sePuedeLlegar xs o d
                         where interseca = interseccion (aDondeLlega (x:xs) o) (deDondeSale (x:xs) d)
-- Funciones auxiliares ej 5

miroSiHayUnVuelo :: AgenciaDeViajes -> Ciudad -> Ciudad -> Bool -- Mira si hay un vuelo exactamente igual que sale de o y va a d
miroSiHayUnVuelo [] _ _ = False
miroSiHayUnVuelo (x:xs) o d | (o == origen x) && (d == destino x) = True
                            | otherwise = miroSiHayUnVuelo xs o d


-- EJERCICIO 6
duracionDelCaminoMasRapido :: AgenciaDeViajes -> Ciudad -> Ciudad -> Duracion -- Te indica la manera mas rapida de llegar de una ciudad a otra dadas en como maximo una escala
duracionDelCaminoMasRapido [] _ _ = 0
duracionDelCaminoMasRapido (x:xs) c d = minimo (duraciones (x:xs) c d)
-- Funciones auxiliares ej 6

escalas :: AgenciaDeViajes -> Ciudad -> Ciudad -> AgenciaDeViajes -- Utiliza interseccion de conjuntos para encontrar un vuelo desde c hasta d con una escala maximo (La mejor funcion hasta ahora) :P
escalas [] _ _ = []
escalas (x:xs) c d | (origen x == c) && (contenido (destino x) interseca) = [x, buscaVuelo xs (destino x) d] ++ escalas (quitarTodos (buscaVuelo xs (destino x) d) xs) c d
                   | (destino x == d) && (contenido (origen x) interseca) = [x, buscaVuelo xs c (origen x)] ++ escalas (quitarTodos (buscaVuelo xs c (origen x)) xs) c d
                   | otherwise = escalas xs c d
                where interseca = interseccion (aDondeLlega (x:xs) c) (deDondeSale (x:xs) d)

duraciones :: AgenciaDeViajes -> Ciudad -> Ciudad -> [Duracion] -- Devuelve una lista con todas las duraciones posibles hacia d (Esta funcion es una locura) :3
duraciones [] _ _ = []
duraciones (x:xs) c d | miroSiHayUnVuelo (x:xs) c d = [duracion (buscaVuelo (x:xs) c d)] ++ duraciones (quitarTodos (buscaVuelo (x:xs) c d) (x:xs)) c d
                      | escalas (x:xs) c d /= [] = [cuentaDuracion (head (escalas (x:xs) c d)) (head (tail (escalas (x:xs) c d)))] ++ duraciones (quitarTodos (head (escalas (x:xs) c d)) (x:xs)) c d
                      | otherwise = duraciones xs c d

cuentaDuracion :: Vuelo -> Vuelo -> Duracion -- Devuelve la duracion de dos vuelos sumados
cuentaDuracion (x1,y1,z1) (x2,y2,z2) = z1 + z2

minimo :: [Duracion] -> Duracion -- Devuelve el mínimo de una lista
minimo [x] = x
minimo (x:y:xs) | x <= y = minimo (x:xs)
                | otherwise = minimo (y:xs)

aDondeLlega :: AgenciaDeViajes -> Ciudad -> [Ciudad] -- A que ciudades podes llegar desde Ciudad
aDondeLlega [] _ = []
aDondeLlega (x:xs) c | origen x == c = eliminarRepetidos ([destino x] ++ aDondeLlega xs c)
                     | otherwise = aDondeLlega xs c

deDondeSale :: AgenciaDeViajes -> Ciudad -> [Ciudad] -- De donde provienen los viajes a Ciudad
deDondeSale [] _ = []
deDondeSale (x:xs) c | destino x == c = eliminarRepetidos ([origen x] ++ deDondeSale xs c)
                     | otherwise = deDondeSale xs c

interseccion :: [Ciudad] -> [Ciudad] -> [Ciudad] -- Interseccion entre listas de ciudades
interseccion [] l = []
interseccion (x:xs) l | contenido x l = [x] ++ interseccion xs l
                      | otherwise = interseccion xs l

buscaVuelo :: AgenciaDeViajes -> Ciudad -> Ciudad -> Vuelo -- Devuelve un vuelo que sale de c y va hasta d
buscaVuelo [] c d = (" ", " ", 111111110)
buscaVuelo (x:xs) c d | (origen x == c) && (destino x == d) = x
                      | otherwise = buscaVuelo xs c d


-- EJERCICIO 7
puedoVolverAOrigen :: AgenciaDeViajes -> Ciudad -> Bool -- Verifica si se puede volver a la ciudad de origen
puedoVolverAOrigen agencia origen = True
-- No lo puedo resolver :( 