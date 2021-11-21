import requests

#Setting the query by the command line
especie = input("Text a specie (With the first capital letter): ")
dades = {"species":especie}

#Getting the number of pages of the characters
dadespagina = requests.get("https://rickandmortyapi.com/api/character",dades)

dadesPerLesPagines = dadespagina.json() #creem el the json

elements =  dadesPerLesPagines["info"] #desde el json extraurem l'informació

pagines = int(elements["pages"])

print("")

total = 0
for i in range((pagines+1)):
    URL = ""
    if i == 0:
        URL = "https://rickandmortyapi.com/api/character"
    else:
        URL = "https://rickandmortyapi.com/api/character?page=" + str(i)
    
    data = requests.get(URL)

    #extragem el json del URL.
    dataJ = data.json()

    for element in dataJ["results"]:
        if element["species"] == especie:
            print("Name: " + element["name"] + ", specie: " + element["species"] + "\n")
            total+=1

print("\n Total: " + str(total))