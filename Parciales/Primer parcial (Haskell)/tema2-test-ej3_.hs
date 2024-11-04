import Solucion
import Test.HUnit

main = runTestTT allTests

allTests = test[
        "palabraOrdenada con |palabra| = 0" ~: palabraOrdenada "" ~?= True,
        "palabraOrdenada con |palabra| = 1, minúscula" ~: palabraOrdenada "y" ~?= True,
        "palabraOrdenada todo mayúscula sin símbolos ni ñ, letras no necesariamente continuas, res= true" ~: palabraOrdenada "EGHPTWZ" ~?= True,
        "palabraOrdenada todo símbolos sin letras, res= false" ~: palabraOrdenada "+-}{'/?" ~?= False ,
        "palabraOrdenada todo símbolos sin letras, res= true" ~: palabraOrdenada "!#&" ~?= True,--borrar?
        "palabraOrdenada con |palabra| > 0 pero solo espacios" ~: palabraOrdenada "   " ~?= True,
        "palabraOrdenada con palabra con una letra y varios espacios" ~: palabraOrdenada "  ñ   " ~?= True,
        "palabraOrdenada todo mayúscula sin símbolos ni ñ y con espacios, letras continuas, res= true" ~: palabraOrdenada " EFG HIJ  " ~?= True, --sacar?
        "palabraOrdenada todo mayúscula sin símbolos ni ñ y con espacios, letras no necesariamente continuas, res= true" ~: palabraOrdenada "   EGHPTWZ " ~?= True,
        "palabraOrdenada todo símbolos sin letras y con espacios, res= true" ~: palabraOrdenada " ! # & " ~?= True,
        "palabraOrdenada todo letras sin espacios nada ordenada, res= false" ~: palabraOrdenada "dcba" ~?= False,
        "palabraOrdenada todo letras sin espacios casi ordenada, res= false" ~: palabraOrdenada "abcded" ~?= False,
        "palabraOrdenada todo letras con espacios casi ordenada, res= false" ~: palabraOrdenada "ab  c d ea  " ~?= False,
        "palabraOrdenada todo letras iguales sin espacios, res= True" ~: palabraOrdenada "bbbbbbb" ~?= True,
        "palabraOrdenada todo letras iguales con espacios, res= True" ~: palabraOrdenada "bb  b bbb" ~?= True

    ]

