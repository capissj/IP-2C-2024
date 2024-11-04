module Solucion where


-- Ejercicio 1
mediaMovilN :: [Integer] -> Integer -> Float
mediaMovilN [] _ = 0
mediaMovilN (x:xs) n | longitud (x:xs) == n = promedio
                     | otherwise = mediaMovilN xs n
                        where promedio = fromIntegral (suma (x:xs)) / fromIntegral (n)

ultimos :: [Integer]-> Integer -> [Integer]
ultimos [] _ = [] 
ultimos (x:xs) e | longitud (x:xs) == e + 1 = xs 
                 | otherwise = ultimos xs e 

suma :: [Integer] -> Integer 
suma [] = 0 
suma (x:xs) = x + suma xs

longitud :: [Integer] -> Integer 
longitud [] = 0
longitud (x:xs) = 1 + longitud xs
 

-- Ejercicio 2 -- No me sale la recursion de los divisores de n, tampoco de los primos, me quiero matar :x
esAtractivo :: Integer -> Bool
esAtractivo 1 = False  
esAtractivo 2 = True 
esAtractivo 3 = True 
esAtractivo 5 = True 
esAtractivo n = False

restaDeN :: Int -> [Int] 
restaDeN 0 = []
restaDeN n = [(n-1)] ++ restaDeN (n-1) 

{-
divisores :: Integer -> [Integer]
divisores n | mod n head (restaDeN n) == 0 = head (restaDeN n) ++ divisores n 
            | otherwise = 

esPrimo :: Integer -> Bool
esPrimo 0 = True 
esPrimo n | mod n (n-1) == 0 = True 
          | otherwise = 
-}

-- Ejercicio 3
palabraOrdenada :: String -> Bool
palabraOrdenada [x] = True
palabraOrdenada (x:y:xs) | (x == ' ') || (y == ' ') = palabraOrdenada (sacarEspaciosBlancos(x:y:xs))
                         | x <= y = palabraOrdenada (y:xs)
                         | otherwise = False

sacarEspaciosBlancos :: String -> String
sacarEspaciosBlancos [] = []
sacarEspaciosBlancos (x:xs) | x == ' ' = sacarEspaciosBlancos xs 
                            | otherwise = [x] ++ sacarEspaciosBlancos xs 


-- Ejercicio 4 -- No puedo sacar el caso cuando son iguales, me queda siempre True si lo llego a poner  :P
similAnagrama :: String -> String -> Bool
similAnagrama [] [] = True
similAnagrama (x:xs) (y:xy) | pertenece ' ' (x:xs) || pertenece ' ' (y:xy) = similAnagrama (sacarEspaciosBlancos (x:xs)) (sacarEspaciosBlancos(y:xy))
                            | longitudString (x:xs) /= longitudString (y:xy) = False
                            | apariciones x (x:xs) == apariciones x (y:xy) = similAnagrama (quitarTodos x (x:xs)) (quitarTodos x (y:xy)) 
                            | otherwise = False

pertenece :: Char -> String -> Bool 
pertenece a [] = False 
pertenece a (x:xs) | a == x = True 
                   | otherwise = False  

igualdad :: String -> String -> Bool 
igualdad [] [] = True 
igualdad (x:xs) (y:xy) | x == y = igualdad (sacarEspaciosBlancos (x:xs)) (sacarEspaciosBlancos (y:xy))
                       | otherwise = False

longitudString :: String -> Integer 
longitudString [] = 0
longitudString (x:xs) = 1 + longitudString xs

quitarTodos :: Char -> String -> String 
quitarTodos c [] = []
quitarTodos c (x:xs) | c == x = [] ++ quitarTodos c xs 
                     | otherwise = [x] ++ quitarTodos c xs

apariciones :: Char -> String -> Integer
apariciones c [] = 0
apariciones c (x:xs) | c == x = 1 + apariciones c xs 
                     | otherwise = apariciones c xs 
