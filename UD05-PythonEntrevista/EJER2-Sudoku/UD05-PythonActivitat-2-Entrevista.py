""" Activitat_2_Entrevista
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""

sudoku = open("Sudoku.in","r")#obrim l'archiu "Sudoku.in" i el guardem a una variable.

sudokulines = sudoku.readlines()#llegim les linies del sudoku i les guardem.

def letras(x):#declarem una funció que llevarà tot alló que no siguen numeros.
    numeros = "0123456789"
    res = []
    for i in range(len(x)):
        if(numeros.find(x[i]) != -1):#si no es un numero se excluirà de la llista i pasara a la següent possició.
            res.append(x[i])
    return res

sudokuclean = list(map(letras,sudokulines))#amb map() apliquem la funció y a més ho comvertim a llist amb lis().

def tamanyo(x):#declarem una funció que ens comprobarà que el tamany de el sudoku es correcte.
    if(isinstance(x,list)):#comprobem que siga una llista.
        for i in range(len(x)):
            if(isinstance(x[i],list)):
                if(len(x)==9 and len(x[i])==9):#si te "9 files y 9 columnes", retornarà True.
                    return True
                else:
                    return False

def esSudokuCorrecte(x):#declarem la funció esSudokuCorrecte, que es la que demana l'exercisi que te que comprobar que està bé.
    if(tamanyo(x) == True):
        num = 0
        for i in range(len(x)):
            for j in range(len(x[i])):
                num +=1 
        if(num == 81): #si en total tenim 81 numeros será correcte ja que habem contat si la cantitat de numeros es 81.
            return "Correcte"
        else: 
            return "Incorrecte"
    else:
        print("Incorrecte")

print(esSudokuCorrecte(sudokuclean))#imprimim el resultat final pasant la funció amb la llista que habem fet abans.

sudoku.close()#per finalitzar tanquem "l'archiu".