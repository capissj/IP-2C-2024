import Test.HUnit
import Data.List
import Solucion
-- No está permitido agregar nuevos imports.


runCatedraTests = runTestTT allTests

allTests = test [
    "vuelosValidos" ~: testsEjvuelosValidos,
    "ciudadesConectadas" ~: testsEjciudadesConectadas,
    "modernizarFlota" ~: testsEjmodernizarFlota,
    "ciudadMasConectada" ~: testsEjciudadMasConectada,
    "sePuedeLlegar" ~: testsEjsePuedeLlegar,
    "duracionDelCaminoMasRapido" ~: testsEjduracionDelCaminoMasRapido,
    "puedoVolverAOrigen" ~: testsEjpuedoVolverAOrigen
    ]

-- corregir los tests si es necesario con las funciones extras que se encuentran al final del archivo

testsEjvuelosValidos = test [ -- Ejercicio 1
    "lista vacía, caso base" ~: vuelosValidos [] ~?= True,
    "agencia con vuelo válido" ~: vuelosValidos [("BsAs", "Rosario", 5.0)] ~?= True,
    "agencia con un vuelo invalido" ~: vuelosValidos [("BsAs","BsAs",30.2)] ~?= False,
    "vuelo con una duracion invalida" ~: vuelosValidos [("BsAs","Rosario",0)] ~?= False,
    "vuelo con duracion negativa" ~: vuelosValidos [("BsAs","Rosrio",(-30))] ~?= False,
    "vuelo totalmente invalido" ~: vuelosValidos [("BsAs", "BsAS", 0)] ~?= False,
    "vuelos con dos elementos validos" ~: vuelosValidos [("BsAs","Rosario",30),("Rosario","Bsas",456)] ~?= True,
    "vuelos con vuelos validos repetidos " ~: vuelosValidos [("BsAs","Rosario",25),("BsAs","Rosario",25)] ~?= False,
    "vuelos invalidos repetidos" ~: vuelosValidos [("BsAs","BsAs",0), ("BsAs","BsAs",0)] ~?= False,
    "vuelos iguales pero con distinta duracion" ~: vuelosValidos [("BsAs","Rosario",25),("BsAs","Rosario",30)] ~?= False,
    "vuelos con un vuelo valido y otro invalido" ~: vuelosValidos [("BsAs","Rosario",30), ("BsAs","BsAs",30)] ~?= False,
    "vuelo válido primero con vuelos inválidos despues" ~: vuelosValidos [("BsAs","Temperley",30), ("BsAs","Rosario",0), ("BsAs","BsAs",10), ("BsAs","Rosario",(-10))] ~?= False
    ]

testsEjciudadesConectadas = test [ -- Ejercicio 2
    "lista vacía, caso base" ~: ciudadesConectadas  [] "Rosario" ~?= [],
    "ciudad no conectada con ningun elemento" ~: ciudadesConectadas  [("BsAs", "Cordoba", 5.0), ("BsAs","Trelew", 10.0)] "Rosario" ~?= [],
    "ciudad conectada con un elemento" ~: ciudadesConectadas  [("BsAs", "Rosario", 5.0)] "Rosario" ~?= ["BsAs"],
 --   "ciudad con mas de un elemento" ~: expectPermutacion (ciudadesConectadas [("BsAs", "Rosario", 5.0), ("Rosario","Trelew", 10.0)] "Rosario") , (ciudadesConectadas [("Trelew", "Rosario", 5.0), ("Rosario","BsAs", 10.0)] "Rosario") ,
    "ciudad conectada con ciudades repetidas" ~: ciudadesConectadas  [("BsAs", "Rosario", 5.0), ("Rosario","BsAs", 10.0)] "Rosario" ~?= ["BsAs"],
    "ciudad conectada con una sola ciudad" ~: ciudadesConectadas  [("Cordoba","Trelew", 10.0),("BsAs", "Rosario", 5.0)] "Rosario" ~?= ["BsAs"]
    ]

testsEjmodernizarFlota = test [ -- Ejercicio 3
    "lista vacía, con caso base" ~: modernizarFlota [] ~?= [],
    "flota modernizada con un elemento" ~: modernizarFlota [("BsAs", "Rosario", 10.0)] ~?= [("BsAs", "Rosario", 9.0)],
    "flota modernizada con dos elementos" ~: modernizarFlota [("BsAs", "Rosario", 10.0), ("Trelew","BsAs", 20.0)] ~?= [("BsAs", "Rosario", 9.0),("Trelew","BsAs", 18.0)]
    ]

testsEjciudadMasConectada = test [ -- Ejercicio 4
    "ciudad mas conectada que aparece dos veces" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Temperley", "Trelew", 15.0), ("Rosario", "Córdoba", 7.0)] ~?= "Rosario",
    "una sola ciudad" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0)] ~?= "BsAs",
    "ciudad mas conectada empatan dos ciudades" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Cordoba", "Trelew", 20.0), ("Rosario", "Córdoba", 7.0)] ~?= "Rosario",
    "ciudad mas conectada empatan varias ciudades" ~: ciudadMasConectada [("BsAs", "Rosario", 10.0), ("Cordoba", "BsAs", 20.0), ("Rosario", "Córdoba", 7.0)] ~?= "Rosario"
    ]

testsEjsePuedeLlegar = test [ -- Ejercicio 5
    "Se puede llegar caso verdadero con una escala" ~: sePuedeLlegar [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Córdoba" ~?= True,
    "No se puede llegar" ~: sePuedeLlegar [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "Trelew" "Córdoba" ~?= False,
    "Se puede llegar sin escala" ~: sePuedeLlegar [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "Córdoba" "BsAs" ~?= True,
    "Se puede llegar con escala antes en la lista" ~: sePuedeLlegar [("Rosario", "Córdoba", 5.0),("BsAs", "Rosario", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Córdoba" ~?= True
    ]

testsEjduracionDelCaminoMasRapido = test [ -- Ejercicio 6
    "duración del camino más rápido con una escala" ~: duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" "Córdoba" ~?= 10.0,
    "duracion del camino mas rapido cuando hay dos caminos" ~:duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("BsAs", "mendoza", 5.0),("mendoza","Cordoba",6.5),("Rosario","Cordoba",4.0)] "BsAs" "Cordoba" ~?= 9.0,
    "duracion del camino mas largo con ruta directa"~:duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("Rosario", "mendoza", 5.0),("mendoza","tucuman",6.5),("BsAs","Cordoba",2.0)] "BsAs" "Cordoba" ~?=2.0,
    "duracion del camino mas largo con mas de una ruta directa con diferente duracion" ~:duracionDelCaminoMasRapido [("BsAs", "Cordoba", 5.0), ("Rosario", "mendoza", 5.0),("BsAs","Cordoba",3.0)] "BsAs" "Cordoba" ~?=3.0,
    "duracion del camino mas largo con ruta directa y escala"~:duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("Rosario", "Cordoba", 5.0),("BsAs","Cordoba",6.5)] "BsAs" "Cordoba" ~?=6.5,
    "duracion del camino mas largo con ruta directa y escala"~:duracionDelCaminoMasRapido [("BsAs", "Rosario", 5.0), ("Rosario", "Cordoba", 5.0),("BsAs","Cordoba",12.0)] "BsAs" "Cordoba" ~?=10.0
    ]
    
testsEjpuedoVolverAOrigen = test [ -- Ejercicio 7
    "puedo volver a origen caso verdadero con una escala" ~: puedoVolverAOrigen [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" ~?= True,
    "puedo volver a origen  caso verdadera con ruta directa"  ~: puedoVolverAOrigen [("BsAs", "Rosario", 5.0), ("Rosario", "BsAs", 5.0), ("Córdoba", "BsAs", 8.0)] "BsAs" ~?= True,
    "puedo volver al origen caso verdadero con mas de una escala"  ~: puedoVolverAOrigen [("BsAs", "Rosario", 5.0), ("Rosario", "Córdoba", 5.0), ("Córdoba", "Tucuman", 8.0),("Tucuman","BsAs",8.8)] "BsAs" ~?= True
    ]



-- Funciones extras

-- margetFloat(): Float
-- asegura: res es igual a 0.00001
margenFloat = 0.00001

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)


-- expectlistProximity (actual: [Float], expected: [Float]): Test
-- asegura: res es un Test Verdadero si y sólo si:
--                  |actual| = |expected|
--                  para todo i entero tal que 0<=i<|actual|, |actual[i] - expected[i]| < margenFloat()
expectlistProximity:: [Float] -> [Float] -> Test
expectlistProximity actual expected = esParecidoLista actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esParecidoLista :: [Float] -> [Float] -> Bool
esParecidoLista actual expected = (length actual) == (length expected) && (esParecidoUnaAUno actual expected)

esParecidoUnaAUno :: [Float] -> [Float] -> Bool
esParecidoUnaAUno [] [] = True
esParecidoUnaAUno (x:xs) (y:ys) = (aproximado x y) && (esParecidoUnaAUno xs ys)

aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat


-- expectAnyTuplaAprox (actual: CharxFloat, expected: [CharxFloat]): Test
-- asegura: res un Test Verdadero si y sólo si:
--                  para algun i entero tal que 0<=i<|expected|,
--                         (fst expected[i]) == (fst actual) && |(snd expected[i]) - (snd actual)| < margenFloat()

expectAnyTuplaAprox :: (Char, Float) -> [(Char, Float)] -> Test
expectAnyTuplaAprox actual expected = elemAproxTupla actual expected ~? ("expected any of: " ++ show expected ++ "\nbut got: " ++ show actual)

elemAproxTupla :: (Char, Float) -> [(Char, Float)] -> Bool
elemAproxTupla _ [] = False
elemAproxTupla (ac,af) ((bc,bf):bs) = sonAprox || (elemAproxTupla (ac,af) bs)
    where sonAprox = (ac == bc) && (aproximado af bf)



-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = esPermutacion actual expected ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

esPermutacion :: Ord a => [a] -> [a] -> Bool
esPermutacion a b = (length a == length b) && (sort a == sort b)