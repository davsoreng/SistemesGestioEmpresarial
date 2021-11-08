""" Activitat_2
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
# Almaçenem en unes variables 2 números diferents.
numero1 = 4
numero2 = 6
# Crearem una funcion per a sumar.
def suma(x, y):
    return x+y
# Cridem a la funció pasant les 2 variables.
print(suma(numero1, numero2))#cridant a la funció i pasant-li dues varibales i ademes imprimint-ho per consola
#
print("---------------------------------------")
#
# Seguidament anem a crear una llista amb diferents valors
valors = [2, 5, 12, 3, 7, 20]
# Crearem una fucnió per a doblar la cantitat dels valors de la llista.
def incremeto(x):
    for i, j in enumerate(x):
        x[i] = j * 2
    print(x)
# Ara comprobarem el resultat cridant a la funció i pasant-li la llista.
incremeto(valors)#cridem a la funció i li pasem la llista creada abans
#
print("---------------------------------------")
#
""" Ara crearem una nova funció que reba una llista, 
    i que se que copie en una nova doblant els valors,
    i que la llista principal no se modifique.
"""
#creem la funció per a multiplicar per 2 en la nova llista.
def llista(x):
    valorsNous = x[:]
    for i, j in enumerate(valorsNous):
        valorsNous[i] = j * 2
    return valorsNous
# Ara anem a comprobar el resultat
print(llista(valors))#cridant a la funció i pasant-li la llista i ademes imprimint-ho per consola
