""" Activitat_6
    AUTOR: David Soriano Enguidanos
    ASIGNATURA: SGE
"""
#cree la llista amb varies altures i pesos
tallweight = [
    ("1.10","30"),
    ("1.30","50"),
    ("1.10","60"),
    ("1.70","30"),
    ("1.80","75")
]
"""
    ara imprimis el sorted de "tallweight" que la ordene de major a menor,
    pero que si la altura te 2 valor igual que pase a ordenar en pes.
"""
print(sorted(tallweight, key=lambda llave:(llave[0], llave[1]), reverse=True))
"""
    El que fa la Key function es tornar els valors perr a poder indicar
    com es te que ordenar.
"""
