import Solucion
import Test.HUnit

main = runTestTT allTests

allTests = test[
    "esAtractivo 1" ~: esAtractivo 1 ~?= False,
    "esAtractivo con n=2, 1 sólo divisor primo" ~: esAtractivo 2 ~?= False,
    "esAtractivo con n=9 igual a un primo elevado a un número q>1, q primo" ~: esAtractivo 9 ~?= True,
    "esAtractivo con n=81 igual a un primo elevado a un número q>1, q no primo" ~: esAtractivo 81 ~?= False,
    "esAtractivo con n=18 divisible por un primo elevado a un número q>1, q primo, y esAtractivo n = True" ~: esAtractivo 18 ~?= True,
    "esAtractivo con n=15 y más de un divisor primo, con res = True" ~: esAtractivo 15 ~?= True,
    "esAtractivo con n=210 y más de un divisor primo, con res = False" ~: esAtractivo 210 ~?= False
    ]

