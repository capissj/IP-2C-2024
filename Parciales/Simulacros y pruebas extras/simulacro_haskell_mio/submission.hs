module SolucionT2 where
--Funciones utiles :D
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e [] = False
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs

chequeoRepetidos :: [(String, String)] -> Bool
chequeoRepetidos [x] = True
chequeoRepetidos (x:y:xs) | x == y = False
                          | otherwise = chequeoRepetidos (y:xs)

quitar :: (Eq t) => t -> [t] -> [t]
quitar e [] = []
quitar e (x:xs) | e == x = xs
                | otherwise = [x] ++ quitar e xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e (quitar e xs) 
                     | otherwise = [x] ++ quitarTodos e xs 

eliminarRepetidos :: (Eq t) => [t] -> [t] 
eliminarRepetidos [] = []
eliminarRepetidos (x:y:xs) | pertenece x xs = [x] ++ quitarTodos x (eliminarRepetidos (y:xs))
                           | otherwise = [x] ++ eliminarRepetidos xs

tuplaValida :: (String, String) -> Bool 
tuplaValida (x,y) | x == y = False
                  | otherwise = True

tuValidas :: [(String, String)] -> Bool
tuValidas [] = True
tuValidas (x:xs) | tuplaValida x = tuValidas xs
                 | otherwise = False

quitarTuplas :: [(String, String)] -> [(String, String)]
quitarTuplas [] = []
quitarTuplas (x:xs) | not (tuplaValida x) = quitar x (quitarTuplas xs) 
                    | otherwise = [x] ++ quitarTuplas xs 

relacionesValidas :: [(String, String)] ->  Bool
relacionesValidas [] = False 
relacionesValidas (x:xs) | chequeoRepetidos xs && tuValidas xs = True
                         | otherwise = False

personas :: [(String, String)] -> [String]
personas [] = ["nadie"] 
personas (x:xs) = personas(quitarTuplas (eliminarRepetidos (x:xs)))
 

amigosDe :: String -> [(String, String)] -> [String]
amigosDe "nadie" [] = ["nadie"] 
amigosDe e (x:xs) 

personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [] = "yo" 