#Ejercicio 1 [2.25 puntos]

#problema: multiplos_de_primos (in v: seq(Z)) : Diccionario(Z, Z)

    #requiere:
    #{ Los elementos de v son positivos }
    #asegura:
    #{ Las claves de res son números primos, y cada valor corresponde con la cantidad de números en v tales que ese primo lo divide }
    #{ Si existe un número primo p tal que divide a algún número de v, entonces p es clave de res }
    #{ Los valores de res son positivos }



#Ejercicio 2 [2.25 puntos]

#problema: longitud_mas_grande
#(in A: seq(seq(Z))) : Z

    #requiere:
    #{ Hay al menos un uno en A }
    #asegura:
    #{ Sea v la secuencia de unos más larga que está contenida en algún A[i] para i válido, res es igual a la longitud de v }

#Ejercicio 3 [2.25 puntos]

#problema: resolver_cuentas
#(in p: Pila(string)) : seq(Z)

    #requiere:
    #{ Para cada elemento x de p vale esta_bien_formado(x) }
    #asegura:
    #{ res[i] es igual al resultado de la operación aritmética representada por el tope de la pila p luego de haber desapilado i elementos, para 0 <= i < longitud de p }
    #{ res tiene la misma cantidad de elementos que p }

#problema: esta_bien_formado
#(in s: string) : Bool

    #requiere:
    #{ - }
    #asegura:
    #{ res == True <==> Cada carácter de s es +, - o es un dígito; el último carácter de s es un dígito; no hay dos operadores consecutivos en s (los operadores son + y -) }

#Ejercicio 4 [2.25 puntos]

#problema: dame_el_que_falta
#(in s: seq(ZxZ)) : ZxZ

    #requiere:
    #{ El menor número que aparece en alguna tupla de s es igual a 1 }
    #{ Sea n el máximo número que aparece en alguna tupla de s, |s| = n * n - 1 }
    #{ s no tiene tuplas repetidas }
    #asegura:
    #{ Las componentes de res son valores entre 1 y n, inclusive }
    #{ res no pertenece a s }