""" Activitat_7
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
import random #imortem un metode de numeros aleatoris
import msvcrt #impote un metode per a esperar a que es pulse una tecla

class Car(object):
    
    matricula: int #declarem matricula
    color: str #declarem color

    #creem el constructor
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    #creem la funció de cambiar de color
    def cambicolor(self, color):
        self.color = color

    #creem la funció de crear cotxe
    def cotxeobv(self):
        print(self.matricula, self.color)

    #creem la funció per ficar la clau al cotxe y arrancar
    def arranque(self):
        print("Ordinador abordo informa: Iniciant sistema de arranque")
        print("Introduix la clau:(Presiona cuansevol teclas) ")
        msvcrt.getch()

    #cree llista amb colors per al cotxe
    colorCotxe = ['roig','blau','negre','rosa','cromat']
    cotxes: Car = []

    def imprimir(cotxes):
        top = min(len(cotxes),10)
        for i in range(top):
            cotxes[i].cotxeobv()

    def crearCotxe():
        ncotxes = int(input("Cuants cotxes vols: "))
        for i in range(ncotxes):
            matricula = i + 1
            color = colorCotxe[random.randint(0, len(colorCotxe)-1)]
            cotxes.append(Car(matricula, color))
        imprimir(cotxes)
    crearCotxe()



