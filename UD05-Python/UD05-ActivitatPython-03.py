""" Activitat_3
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
#importem haslib, que ens servirá per a poder fer l'encriptació.
import hashlib
# creem una llista
usrpass = []
#creem un bucle for en un range de 5
for i in range(5):
    usrpass.append([])#açi anyadim a la posició "i" els "[]"
    for j in range(1):#i ara repetirem aquest bucle 1 vegada
        user = input("Escribe Usuario: ")#demanem un usuari que guardema a "user"
        usrpass[i].append(user)#a la posició de i en usrpass anyadim l'usuari
        passw = input("Escribe Password: ")#demanem una contrasenya que guardem a "passw"
        usrpass[i].append(hash(passw))#a la posició de i en usrpass anyadim la controasenya cifrada
#imprimim la llista, per a comprobar qeu el resultat està be.
print(usrpass)
# fem un diccionari
passusr = {}
#creem un bucle for amb un range de 5
for i in range(5):
    user = input("Escribe Usuario: ")#demanem un usuari que guardema a "user"
    passw = input("Escribir Contraseña: ")#demanem una contaseña que guardema a "passw"
    passusr[hash(passw)] = user#guardem en passusr, passw encriptada com
#imprimim el diccionari, per a comprobar qeu el resultat està be.
print(passusr)
