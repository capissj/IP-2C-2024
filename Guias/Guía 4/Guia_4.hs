factorial :: Int -> Int
factorial n | n == 0 = 1
            | n > 0 = n * factorial  (n-1)

factorial2 :: Int -> Int
factorial2 0 = 1
factorial2 n = n * factorial  (n-1)

-- Problema 1

fibonacci :: Int -> Int
fibonacci n | (n == 0 || n == 1) = n
            | otherwise = fibonacci (n-1) + fibonacci (n-2)

-- Problema 2

parteEntera :: Float -> Integer 
parteEntera x | x < 1 = 0
              | otherwise = parteEntera (x-1) + 1

-- Problema 3

esDivisible :: Integer -> Integer -> Bool
esDivisible n x | n == 0 = True
                | n < x = False
                | x < 0 = esDivisible (n+x) x --No entiendo una goma xD
                | otherwise = esDivisible (n-x) x

-- Problema 4

sumaImpares :: Int -> Int 
sumaImpares n | n < 0 = 0
              | mod n 2 == 0 = sumaImpares(n-3) + n-1
              | otherwise = sumaImpares (n-2) + n

-- Problema 5

medioFact :: Int -> Int 
medioFact n | n <= 1 = 1
            | otherwise = medioFact(n-2) * n

-- Problema 6

todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = compararTodos n (mod n 10) 
compararTodos :: Int -> Int -> Bool
compararTodos n m | n < 10 = n == m
                  | otherwise = mod n 10 == m && compararTodos (div n 10) m

-- Problma 7

iesimoDigito :: Int -> Int -> Int
iesimoDigito n i | cantDigitos n == i = mod n 10
                 | otherwise = iesimoDigito (div n 10) i
cantDigitos :: Int -> Int
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

-- Problema 8

sumaDigitos :: Int -> Int 
sumaDigitos n | n < 10 = n
              | otherwise = mod n 10 + sumaDigitos (div n 10)

-- Problema 9

esCapicua :: Int -> Bool
esCapicua n | n < 10 = True
            | otherwise = primero n == ultimo n && esCapicua (sacarBordes n)
            where primero n = iesimoDigito n 1
                  ultimo n = iesimoDigito n (cantDigitos n)
                  sacarBordes n = div (mod n (10^(cantDigitos n - 1))) 10

-- Problema 10

f1 :: Int -> Int 
f1 i | i == 0 = 1
     | otherwise = 2^i + f1(i-1)

f2 :: Int -> Int -> Int
f2 q n | n == 1 = q
       | otherwise = q^n + f2 q (n-1)