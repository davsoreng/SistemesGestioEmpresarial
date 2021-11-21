""" Activitat_3_Entrevista
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
text = input("Type a string: ")#demanem una cadena de text

def numeroPatrons(text):#definim una funció
    #amb count() aniremguardant el numero de vegades que es repeteix el patró
    comboCounter = 0
    comboCounter += text.count("101")
    comboCounter += text.count("ABC")
    comboCounter += text.count("HO")
    letters = list(text)#guardem en una llista totes les lletres del text que habem demanat
    zero = ""
    for i in letters:
        zero += i
        if(i!="0"):
            zero = ""
        if(zero=="00"):
            comboCounter+=1
            zero = "0"
    return comboCounter
print("Counter= " + str(numeroPatrons(text)))