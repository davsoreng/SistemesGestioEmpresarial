""" Activitat_12_Entrevista
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
from PIL import Image #importem Image que ens servirà per obrir una imatge
import pytesseract#i també importem pytesseract que servirà a més per a poder

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'

img = Image.open('imatge1.png')#obrim l'imatge.

result = pytesseract.image_to_string(img)#passem l'imatge a string.

with open('resultat1.txt', mode = 'w') as file:#per ultim passem el resultat del anterior string a l'archiu txt.
    file.write(result)