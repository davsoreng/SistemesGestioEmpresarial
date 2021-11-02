""" Activitat_3
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
# creem una llista
import hashlib
usrpass = []
# creem una funció per a demanr el usuari y la contraseña
def sigin(x):
    i = 0
    while(i < 5):
        user = input("Escribe Usuario: ")
        x.append(user)
        passw = input("Escribe Password: ")
        x.append(hash(passw))
        i += 1
    return x
# cridem a la funció
print(sigin(usrpass))
# fem un diccionari
passusr = {}
#creem la funció
def logout(x):
    i = 0
    while(i < 10):
        user = input("Escribe Usuario: ")
        passw = input("Escribir Contraseña: ")
        x[user] = i
        i += 1
        x[hash(passw)] = i
        i += 1
    return x
#cridem a la funció
print(logout(passusr))
