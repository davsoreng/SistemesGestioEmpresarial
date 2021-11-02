""" Activitat_5
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
import sys  #importem sys, que es per a llegir al moment de la execució de la applicació

datos = sys.argv #guarda els arguments a la llista "datos"

#fem un bucle for per a recorrer la llista hasta la ultima posició ocupada
for i in range(len(datos)):
    print("Has ecrito por consola: "+datos[i])

#definim una funció i li pasem dos datos, aquestos es sumaran y tornaran
def funcio(n1, n2):
    return n1 + n2

""" definim una funció, 
    li pasem els arguments i en un bucle for anem sumant a la varible n el resultat 
"""
def funcio(*args):
    n = 0
    for i in range(len(args)):
        n += args[i]
    return n

#cridem a les funcions pasants els datos y les imprimim.
print(funcio(1, 2, 3, 4, 5))
print(funcio(5, 5))
