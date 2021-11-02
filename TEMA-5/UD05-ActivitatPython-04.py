""" Activitat_4
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
#
""" creem la funció iss, que ens demanarà un nom, 
    i tindrem que comprobar si la variable x esta buida o no, 
    per a comprobaro utilitzarem "is".
"""
def iss(): #definim la funció iss
    x = input("Escribe tu nombre: ")#Demanen el nom
    if x is "":#amb un if comprobem que la variable x es igual a ""
        print("Nombre está vacio.")#en cas de que no siga igual a "" mostrem per pantalla de que el nom está buit.
    else:
        print("Tu nombre es: "+x)#en cas de que siga igual a "" imprimim el nom.
    print("\n")
#cridem a la funció iss.
iss()
""" creem la funció not, que ens demanarà l'edad, 
    i tindrem que comprobar si la variable x esta buida o no, 
    per a comprobaro utilitzarem "not".
"""
def nott(): #definim la funció nott
    x = input("Escribe tu edad: ")#Demanen l'edad
    if not x == "": #si x no es igual a "", imprimim l'edad
        print("Tu edad es "+x)
    else:#sino mostrem per pantalla de que l'edad está buida.
        print("Edad está vacio")
    print("\n")
#cridem a la funció nott.
nott()
""" creem la funció inn, que ens demanarà l'altura, 
    i tindrem que comprobar si la variable x esta buida o no, 
    per a comprobaro utilitzarem "inn".
"""
def inn(): #definim la funció inn
    print("A l'hora d'escriure l'altrua, deus escriurela de 10 en 10, per exemple 1.10/1.20/1.30...")
    altures = ["0.00","0.10","0.20","0.30","0.40","0.50","0.60","0.70","0.80","0.90","1.00","1.10","1.20","1.30","1.40","1.50","1.60","1.70","1.80","1.90","2.00","2.10","2.20"]
    x = input("Escribe tu altura: ")#Demanen l'altura
    if x in altures: #si x no es igual a "", imprimim l'altura
        print("Tu altura es "+x)
    else:#sino mostrem per pantalla de que l'altura está buida.
        print("Altura está vacio")
    print("\n")
#cridem a la funció inn.
inn()

