-- Problema 1 A

longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- Problema 1 B

ultimo :: [t] -> t 
ultimo (x:xs) | longitud xs == 0 = x 
              | otherwise = ultimo xs

-- Problema 1 C

principio :: [t] -> [t]
principio (x:xs) | longitud xs == 0 = []
                 | otherwise = x : principio xs 

-- Problema 1 D

reverso :: (Eq t) => [t] -> [t]
reverso (x:xs) | xs == [] = [x]
               | otherwise = reverso xs ++ [x] {-
iesimoDigito :: Int -> [t] -> t 
iesimoDigito i (xs) -}
-- Problema 2 A

pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece n [] = False
pertenece n (x:xs) | x == n = True
                   | otherwise = pertenece n xs

-- Problema 2 B

todosIguales :: (Eq t) => [t] -> Bool 
todosIguales [x] = True
todosIguales (x:y:xs) | y /= x = False
                      | otherwise = todosIguales (y:xs) 
{- Otra manera de hacerlo, que no sirve si le doy una lista con un elemento :D
todosIguales (x:xs) | xs == [] = True 
                      | head xs /= x = False
                      | otherwise = todosIguales (xs) -}

-- Problema 2 C 

todosDistintos :: (Eq t) => [t] -> Bool 
todosDistintos (x:xs) | longitud xs == 0 = True 
                      | pertenece x xs == True = False 
                      | otherwise = todosDistintos xs

-- Problema 2 D 

hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos (x:xs) | xs == [] = False 
                    | pertenece x xs == True = True
                    | otherwise = hayRepetidos xs

-- Problema 2 E

quitar :: (Eq t) => t -> [t] -> [t]
quitar e [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = [x] ++ quitar e xs

-- Problema 2 F

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e (x:xs) | e == x = [] ++ quitarTodos e (xs)
                     | otherwise = [x] ++ quitarTodos e xs

-- Problema 2 G

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece x xs = [x] ++ quitarTodos x (eliminarRepetidos xs)
                         | otherwise = [x] ++ eliminarRepetidos xs

-- Problema 2 H

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos (x:xs) (y:xy) | pertenece x (y:xy) && pertenece y (x:xs) = mismosElementos xs xy
                              | otherwise = False

-- Problema 2 I

capicua :: (Eq t) => [t] -> Bool
capicua (x:xs) | longitud xs == 1 = True 
               | x /= ultimo xs = False
               | otherwise = capicua (drop 1 (reverso xs))

-- Problema 3 A

sumatoria :: [Int] -> Int 
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- Problema 3 B

productoria :: [Int] -> Int
productoria [] = 1
productoria (x:xs) = x * productoria xs

-- Problema 3 C

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x >= y = maximo (x:xs) 
                | otherwise = maximo (y:xs)

-- Problema 3 D

sumarN :: Int -> [Int] -> [Int]
sumarN n [] = [] 
sumarN n (x:xs) = [n + x] ++ sumarN n xs

-- Problema 3 E

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = [x + x] ++ sumarN x xs

-- Problema 3 D

sumarUltimo :: [Int] -> [Int]
sumarUltimo [] = []
sumarUltimo (x:xs) = [ultimo xs + x] ++ sumarN (ultimo xs) xs  

-- Problema 3 E 

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = [x] ++ pares xs
             | otherwise = pares xs

-- Problema 3 F

multiploDeN :: Int -> [Int] -> [Int]
multiploDeN n [] = []
multiploDeN n (x:xs) | mod x n == 0 = [x] ++ multiploDeN n xs
                     | otherwise = multiploDeN n xs

-- Problema 3 G

ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar xs  = ordenar (quitar (maximo xs) xs) ++ [maximo xs]

-- Problema 4

