import Solucion
import Test.HUnit

main = runTestTT allTests

allTests = test[
    "mediaMovilN ultimo" ~: mediaMovilN [9, 98,7, 9, 98,7, 9, 98,7, 9, 98,7, 1, 2, 3, 4, 5] 1 ~?= 5.0,
    "mediaMovilN todos" ~: mediaMovilN [1, 2, 3, 4, 5] 5 ~?= 3.0,
    "mediaMovilN lista con ceros" ~: mediaMovilN [0, 0, 0, 0, 0, 0, 0, 0, 0] 3 ~?= 0.0,
    "mediaMovilN n=|l|-1" ~: mediaMovilN [1, 2, 3, 4, 5] 4 ~?= 3.5,
    "mediaMovilN ultimos 2" ~: mediaMovilN [6, 6, 7, 8, 1, 0, 0, 1, 1] 2 ~?= 1.0,
    "mediaMovilN lista de un elemento" ~: mediaMovilN [1] 1 ~?= 1.0
    ]