""" Activitat_1_Entrevista
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
import functools
#Anem a crear una funció lambda amb una paraula.
frase = (lambda x="micro",z="ondas":x + z)
#Pasarem a la variable frase un argument.
print(frase("cafetera"))#Comprobem si s'ha cambiat el resultat del lambda.
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print("--------------------------------")
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#Almacenem en una variable el input del numeros que habem escrit.
numeros = input("Escriu numeros separats amb espais: ")
#declarem un llista
listNumeros = []
#ara amb els numeros s'almatzenaran a una llista per cada espai ficat.
listNumeros = numeros.split(" ")
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print("--------------------------------")
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#definic una funció que validará si la llista te lletres
def lletres(x):
    num = "0123456789"
    resultat = ""
    for i in range(len(x)):
        if(num.find(x[i]) == -1): #en cas de que tinga lletres manarà un avis e ixirà del programa
            print("La llista no pot contindre lletres.")
            exit()
        else:
            resultat += x[i]
    return resultat
#ara amb map(), pasarem la funció que volem fer i amb quina llista anem a treballar
#a més utilitzarem list() per a guardar les dades a la variable en forma de llista
resultatNumeros = list(map(lletres, listNumeros))
#e imprimim la llista
print(resultatNumeros)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print("--------------------------------")
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#ara convertirem totes les cadenes a numeros
resultatInt = list(map(int,resultatNumeros))
''' en una funció lamba comprobem quines son els numeros major o igual a 10,
    amb filter() excluirem als numeros que no cumplixquen la funció lamba
    i per a terminar amb list() convertirem el resultat en forma de llista.
'''
filtrarNum = list(filter(lambda n: n >= 10, resultatInt))
#i imprimim el resultat
print(filtrarNum)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print("--------------------------------")
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#ara amb una funció lamba() i reduce() multipliquem els numeros de la llista
filtrarNum = functools.reduce(lambda a, b: a*b, filtrarNum)
#e imprimim el resultat
print(filtrarNum)