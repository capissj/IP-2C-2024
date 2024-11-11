#Ej 11
def triangle ( a : int , b : int , c : int ) -> int :
    if ( a <= 0 or b <= 0 or c <= 0):
        return 4 # invalido
    if ( not (( a + b > c ) and ( a + c > b ) and ( b + c > a ))):
        return 4 # invalido
    if ( a == b and b == c ):
        return 1 # equilatero
    if ( a == b or b == c or a == c ):
        return 2 # isosceles
    return 3 # escaleno