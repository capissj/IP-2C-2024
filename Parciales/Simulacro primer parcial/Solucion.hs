module Solucion where

-- Funciones auxiliares :P
primerComponenteTupla :: (String, String) -> String
primerComponenteTupla (x,y) = x
segundaComponenteTupla :: (String, String) -> String
segundaComponenteTupla (x,y) = y

contenido :: (Eq t) => t -> [t] -> Bool
contenido e [] = False
contenido e (x:xs) | e == x = True
                   | otherwise = contenido e xs

pertenece :: String -> [(String, String)] -> Bool
pertenece e [] = False
pertenece e (x:xs) | (e == primerComponenteTupla x) || (e == segundaComponenteTupla x) = True
                   | otherwise = pertenece e xs  

tuplaValida :: (String, String) -> Bool
tuplaValida (x,y) | x == y = False
                  | otherwise = True

validezTuplas :: [(String, String)] -> Bool
validezTuplas [] = True
validezTuplas (x:xs) | tuplaValida x = validezTuplas xs
                     | otherwise = False

verificoRepetidos :: [(String, String)] -> Bool
verificoRepetidos [x] = True
verificoRepetidos (x:xs) | contenido x xs = False
                         | otherwise = verificoRepetidos xs

invertirTupla :: (String, String) -> (String, String)
invertirTupla (x,y) = (y,x)

tuplasInvertidas :: [(String, String)] -> [(String, String)]
tuplasInvertidas [] = []
tuplasInvertidas (x:xs) = [invertirTupla x] ++ tuplasInvertidas xs

relacionesValidas :: [(String, String)] ->  Bool
relacionesValidas [] = True
relacionesValidas (x:xs) | verificoRepetidos ((x:xs) ++ tuplasInvertidas (x:xs)) && validezTuplas (x:xs) = True
                         | otherwise = False

listaPersonas :: [(String, String)] -> [String]
listaPersonas [] = []
listaPersonas (x:xs) = [primerComponenteTupla x, segundaComponenteTupla x] ++ listaPersonas xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e (x:xs) | e == x = [] ++ quitarTodos e xs
                     | otherwise = [x] ++ quitarTodos e xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | contenido x xs = [x] ++ quitarTodos x (eliminarRepetidos xs)
                         | otherwise = [x] ++ eliminarRepetidos xs 

personas :: [(String, String)] -> [String]
personas [] = [] 
personas (x:xs) = eliminarRepetidos (listaPersonas (x:xs)) 

amigosDe :: String -> [(String, String)] -> [String]
amigosDe e [] = []
amigosDe e (x:xs) | primerComponenteTupla x == e = [segundaComponenteTupla x] ++ amigosDe e xs
                  | segundaComponenteTupla x == e = [primerComponenteTupla x] ++ amigosDe e xs 
                  | otherwise = amigosDe e xs


personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [] = "yo" 
