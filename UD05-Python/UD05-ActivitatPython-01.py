""" Activitat_1
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
#Crearem una llista anomenada "llisteta".
llisteta = []
#Anyadim a la llista un element anomenat "element1"
llisteta.append("element1")
#Ara anem a imprimir la llista per a comprobar si s'ha anyadit el nou element.
print(llisteta[0])
#Clonem la llista "llisteta".
novallista = llisteta[:]
#comprobem si funciona
print(novallista[0])
#A continuación anem a eliminar el element "element1" de la llista "llisteta".
del llisteta[0]
#Per a comprobar que no te valor anem a imprimir per consola el tamany de la llista.
print(len(llisteta)) #si tot ha funcionat be el resultat del print te que ser 0.
#Ara anem a crear una llista amb 4 element.
noms = ["David","Jose","Victor","Carpio","Pablo"]
#Ara crearem un altra llista per almaçenar els 4 ultims elements de la llista "noms".
novanoms = noms[-4:]
#comprobarem amb print si ha huncionat
print(novanoms)
#Ara anem a convertir les paraules d'una cadena separades per espai a una llista
paraula = "Hola bona nit a tots i totes."
separa = paraula.split(" ")
#Ara anem a comprobar el resultat.
print(separa)

"""
    Shallow Copy y Deep copy, la Deep Copy es caracteritza per fer una copia de una llista,
    sense que els camvies de la llista nova que te la copia afecten a la original,
    en canvi, la Shallow copy, es una referncia a la original, el fet d'aço es que si fem
    un canvi en la llista de la copia, la original també cambia.
"""