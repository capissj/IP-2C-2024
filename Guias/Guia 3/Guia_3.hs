doubleMe :: Int -> Int
doubleMe x = x+x

-- Problema 1

f1 :: Int -> Int
f1 x | x==1 = 8
     | x==4 = 131
     | x==16 = 16

g1 :: Int -> Int
g1 x | x==8 =16
     | x==16 =4
     | x==131 =1

h1 :: Int -> Int
h1 x = f1(g1(x))

k1 :: Int -> Int
k1 x = g1(f1(x))

-- Problema 2

absoluto :: Float -> Float
absoluto x | x >= 0 = x 
           | otherwise = -x

maximoAbsoluto :: Float -> Float -> Float 
maximoAbsoluto x y | (absoluto x) < (absoluto y) = y
                   | otherwise = x

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | otherwise = z

algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y = x==0 || y==0

ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y = x == 0 && y == 0 

ambosSonCero :: Float -> Float -> Bool
ambosSonCero x y | x == 0 && y == 0 = True
                 | otherwise = False

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x > 3 && x <= 7 && y > 3 && y <= 7 = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x == y = z
                    | y == z = x
                    | x == z = y
                    | otherwise = x+y+z

esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y == 0 = True --mod te devuelve el resto
                 | otherwise = False

digitoUnidades :: Int -> Int 
digitoUnidades x = div x 10 --div tira el resto a la bosta

digitoDecenas :: Int -> Int
digitoDecenas x = mod (div x 10) 10

-- Problema 3

estanRelacionados :: Int -> Int -> Bool
estanRelacionados x y | x == 0 && y == 0 = False
                      | mod x y == 0 = True
                      | otherwise = False

-- Problema 4

prodInt :: (Int, Int) -> (Int, Int) -> (Int, Int)
prodInt (x1, y1) (x2, y2) = (x1 * x2, y1 * y2)

todoMenor :: (Int, Int) -> (Int, Int) -> Bool
todoMenor (x1, y1) (x2, y2) | x1 < x2 && y1 < y2 = True
                            | otherwise = False

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x1, y1) (x2, y2) = sqrt((x2 - x1)^2+(y2 - y1)^2)

sumaTernas :: (Int, Int, Int) -> Int
sumaTernas (x, y ,z) = x + y + z

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x, y, z) n | mod x n == 0 && mod y n == 0 && mod z n == 0 = x+y+z
                               | mod x n == 0 && mod y n == 0 = x+y
                               | mod x n == 0 && mod z n == 0 = x+z
                               | mod x n == 0 = x
                               | mod y n == 0 && mod z n == 0 = y+z 
                               | mod y n == 0 = y
                               | mod z n == 0 = z
                               | otherwise = 0
                              
posPrimerPar :: (Int, Int, Int) -> Int 
posPrimerPar (x,y,z) | mod x 2 == 0 = 1
                     | mod y 2 == 0 = 2
                     | mod z 2 == 0 = 3
                     | otherwise = 4

crearPar :: a -> b -> (a, b)
crearPar x y = (x, y)

invertir :: (a, b) -> (b, a)
invertir (x,y) = (y,x)

type Punto2D = (Float, Float)

prodIntPunto2D :: Punto2D -> Punto2D -> Punto2D
prodIntPunto2D (x1, y1) (x2,y2) = (x1*x2, y1*y2)

todoMenorPunto2D :: Punto2D -> Punto2D -> Bool
todoMenorPunto2D (x1, y1) (x2, y2) | x1 < x2 && y1 < y2 = True
                                   | otherwise = False

distanciaPuntosPunto2D :: Punto2D -> Punto2D -> Float
distanciaPuntosPunto2D (x1, y1) (x2, y2) = sqrt((x2 - x1)^2+(y2 - y1)^2)

-- Problema 5

todosMenores :: (Int, Int, Int) -> Bool
todosMenores (x, y, z) | ((f5(x) > g5(x)) && (f5(y) > g5(y)) && (f5(z) > g5(z))) = True
                       | otherwise = False
f5 :: Int -> Int
f5 n | n <= 7 = n^2
     | otherwise = 2*n-1
g5 :: Int -> Int
g5 n | mod n 2 == 0 = div n 2
     | otherwise = 3*n+1

-- No sé testearlo dinámicamente xD, parece estar todo bien estáticamente :P (hacelo despues gordo)

-- Problema 6

type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto  
bisiesto n | mod n 400 == 0 = True
           | mod n 100 == 0 = False
           | mod n 4 == 0 = True 
           | otherwise = False

-- Problema 7 

type Coordenada3d = (Float, Float, Float)

distanciaManhattan :: Coordenada3d -> Coordenada3d -> Float
distanciaManhattan (x1,y1,z1) (x2,y2,z2) = absoluto (x1 - x2) + absoluto (y1 - y2) + absoluto (z1 - z2)
-- Cambié los tipos de datos de absoluto y de maximoAbsoluto a Float para poder volver a usarlos

-- Problema 8 

comparar :: Int -> Int -> Int
comparar x y | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
             | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
             | otherwise = 0
             where sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10