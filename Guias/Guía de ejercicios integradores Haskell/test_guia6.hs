import Test.HUnit
import Data.List
import Guia6

runCatedraTests = runTestTT allTests

allTests = test [
    "dineroEnStock" ~: testsEjdineroEnStock
    ]
testsEjdineroEnStock = test [
    "lista vacia, caso base" ~: vuelosValidos [] [] ~?= 0,
    "precios con tres productos desordenados" ~: dineroEnStock [("Teclado", 20),("Mouse", 5),("Auriculares",3)] [("Mouse", 6),("Auriculares", 10),("Teclado",1.5)] ~?= 90
    ]