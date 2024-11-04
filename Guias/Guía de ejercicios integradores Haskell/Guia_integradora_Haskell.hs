module Guia6 where

generarStock :: [String] -> [(String, Int)]
generarStock [] = []
generarStock (x:xs) = (x, apariciones (x:xs) x) : generarStock (quitarTodos xs x) 

apariciones :: [String] -> String -> Int 
apariciones [] _ = 0 
apariciones (x:xs) s | s == x = 1 + apariciones xs s 
                     | otherwise = apariciones xs s

quitarTodos :: (Eq t) => [t] -> t -> [t]
quitarTodos [] _ = []
quitarTodos (x:xs) e | e == x = [] ++ quitarTodos xs e
                     | otherwise = [x] ++ quitarTodos xs e

producto :: (String, Int) -> String 
producto (x,y) = x 
stockProducto :: (String, Int) -> Int 
stockProducto (x,y) = y

listaDeProductos :: [(String, Int)] -> String -> Int 
listaDeProductos [] _ = 0
listaDeProductos (x:xs) p | p == producto x = stockProducto x 
                          | otherwise = listaDeProductos xs p 

precio :: (String, Float) -> Float 
precio (x,y) = y
productoPrecio :: (String, Float) -> String 
productoPrecio (x,y) = x


dineroEnStock :: [(String, Int)] -> [(String, Float)] -> Float 
dineroEnStock [] xy = 0
dineroEnStock (x:xs) (y:xy) = precioDeUnProducto (x:xs) (y:xy) + dineroEnStock xs (y:xy)

precioDeUnProducto :: [(String, Int)] -> [(String, Float)] -> Float 
precioDeUnProducto [x] [] = 0
precioDeUnProducto (x:xs) (y:xy) | producto x == productoPrecio y = fromIntegral (stockProducto x) * (precio y)
                                 | otherwise = precioDeUnProducto (x:xs) (xy)

aplicarOferta :: [(String, Int)] -> [(String, Float)] -> [(String, Float)]
aplicarOferta [] [] = []

masDe10Productos :: [(String, Int)] -> [(String, Int)] 