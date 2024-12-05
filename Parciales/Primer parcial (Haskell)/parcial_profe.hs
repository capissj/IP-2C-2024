module Solucion where

-- Ejercicio 1
mediaMovilN :: [Integer] -> Integer -> Float
mediaMovilN (x:xs) n | largo (x:xs) == n = fromInteger(sumar (x:xs)) / (fromInteger n) 
                     | otherwise = mediaMovilN xs n  

largo :: (Ord t) => [t] -> Integer
largo [] = 0
largo (x:xs) = 1 + largo xs

sumar :: [Integer]-> Integer 
sumar [] = 0
sumar (x:xs) = x + sumar xs


-- Ejercicio 2
esAtractivo :: Integer -> Bool
esAtractivo 1 = False
esAtractivo n = esPrimo (cantidadDivisoresPrimos n)

cantidadDivisoresPrimos :: Integer -> Integer
cantidadDivisoresPrimos n = contarDivisoresPrimosDesde 2 n 

contarDivisoresPrimosDesde :: Integer -> Integer -> Integer
contarDivisoresPrimosDesde d n | d == n && esPrimo d = 1
                               | d == n && not (esPrimo d) = 0
                               | (esPrimo d) && loDivide = 1 + contarDivisoresPrimosDesde d (div n d)
                               | otherwise = contarDivisoresPrimosDesde (d+1) n
                               where loDivide = mod n d == 0

esPrimo :: Integer -> Bool
esPrimo x = cantidadDivisoresHasta x x == 2

-- Recibe d y n, cuenta la cantidad de divisores de n que son menores o iguales a d.
cantidadDivisoresHasta :: Integer -> Integer -> Integer
cantidadDivisoresHasta 1 n = 1 -- 1 siempre divide
cantidadDivisoresHasta d n | loDivide = 1 + cantidadDivisoresHasta (d-1) n 
                           | otherwise = cantidadDivisoresHasta (d-1) n 
                           where loDivide = mod n d == 0 


-- Ejercicio 3
palabraOrdenada :: String -> Bool
palabraOrdenada [] = True 
palabraOrdenada [x] = True 
palabraOrdenada (x:y:xs) | x == ' ' && y == ' ' = palabraOrdenada xs
                         | x == ' ' = palabraOrdenada (y:xs)
                         | y == ' ' = palabraOrdenada (x:xs)
                         | otherwise = x <= y && palabraOrdenada (y:xs)


-- Ejercicio 4
-- Debe haber misma cantidad de apariciones en ambos Strings de todos los elementos no blancos. Además, no deben ser iguales
similAnagrama :: String -> String -> Bool
similAnagrama s t = mismaCantidadDeNoBlancos s s t && mismaCantidadDeNoBlancos t s t && s /= t

-- El primer parametro indica que caracteres resta chequear. Los otros dos param son los strings originales
mismaCantidadDeNoBlancos :: String -> String -> String -> Bool
mismaCantidadDeNoBlancos [] _ _ = True
mismaCantidadDeNoBlancos (x:xs) s t | x == ' ' = mismaCantidadDeNoBlancos xs s t 
                                    | otherwise = mismaCantidadX && mismaCantidadDeNoBlancos xs s t 
                                    where mismaCantidadX = cantAp x s == cantAp x t 

cantAp :: Char -> String -> Int
cantAp _ [] = 0
cantAp letra (x:xs) | letra == x = 1 + cantAp letra xs
                    | otherwise = cantAp letra xs



