#import numpy as np
from random import *
# import matplotlib.pyplot as plt
# import tools as tls
import config
import time


def peut_placer(grille, bateau, position, direction) :
    """ list(list(int)) * int * (int, int) * int -> bool
    Rend vrai s’il est possible de placer le bateau sur
    la grille à la position et dans la direction
    donnée.

    Toutes les cases que doit occuper le bateau sont libres.

    Par convention, la position d'un bateau sera sa case la plus à gauche s'il
    est horizontal, et sa case la plus en haut dans le cas où il est vertical.

     -- direction : 1 si horizontal, 2 si vertical

    """
    # x : int
    # y : int
    x, y = position

    # h : int
    h = 0

    # v : int
    v = 0

    # Pour i dans [0, longueur du bateau[ :
    for i in range((config.reference[bateau])[1]) :
        # Si la direction est horizontale :
        if direction == 1 :
            # h est incrémenté, il sera ajouté à y plus tard de façon à se
            # déplacer horizontalement
            h = i
        # Si vertical :
        else :
            # v est incrémenté, il sera ajouté à x plus tard de façon à se
            # déplacer verticalement
            v = i
        # Si l'une des cases est occupée ou est hors-limites :
        if x+v >= (len(grille)) or y+h >= (len(grille[0])) or grille[x+v][y+h] != 0 :
            return False

    return True

def place(grille, bateau, position, direction) :
    """ list(list(int)) * int * (int, int) * int -> bool
    Rend la grille modifiée (s’il est possible de placer le bateau).
    """
    x, y = position

    # h : int
    h = 0
    # v : int
    v = 0
    # Pour i dans [0, longueur du bateau[ :
    for i in range((config.reference[bateau])[1]) :
        # Si la direction est horizontale :
        if direction == 1 :
            # h est incrémenté, il sera ajouté à y plus tard de façon à se
            # déplacer horizontalement
            h = i

        # Si vertical :
        else :
            # v est incrémenté, il sera ajouté à x plus tard de façon à se
            # déplacer verticalement
            v = i

        grille[x+v][y+h] = bateau

    return grille


def place_alea(grille, bateau) :
    """ list(list(int)) * int  -> void
    Place aléatoirement le bateau dans la grille : la fonction tire uniformément
    une position et une direction aléatoires et tente de placer le bateau ; s’il
    n’est pas possible de placer le bateau, un nouveau tirage est effectué et ce
    jusqu’à ce que le positionnement soit admissible.

    TODO : Que se passe-t-il quand aucune place n'est disponible ?
    """
    x = randint(0, 9)
    y = randint(0, 9)
    d = randint(1,2)
    while not (peut_placer(grille, bateau, (x,y), d)) :
        x = randint(0, 9)
        y = randint(0, 9)
        d = randint(1,2)
    place(grille, bateau, (x,y), d)



def genere_grille():
    """ void -> list(list(int))
    Rend une grille avec les bateaux disposés de manière aléatoire
    """
    return genere_grille_list([i for i in range(1, 6)])

def genere_grille_list(listNum=[i for i in range(1,6)]):
    """ list(int) -> list(list(int))
    Rend une grille avec les bateaux disposés de manière aléatoire
    """
    # matrice : list(list(int))
    matrice = genere_grille_vide()
    for i in listNum:
        place_alea(matrice, i)
    return matrice

def genere_grille_vide() :
    """ void -> list(list(int))
    Renvoie une grille vide
    """
    return [[0 for y in range(10)] for x in range(10)]




""" TESTS """
def main() :

    print(peut_placer(genere_grille_vide(), 1, (0, 0), 1))
    print(peut_placer(genere_grille_vide(), 1, (9, 9), 1))

    print(peut_placer(genere_grille_vide(), 1, (9, 0), 1))
    print(peut_placer(genere_grille_vide(), 2, (9, 0), 1))
    print(peut_placer(genere_grille_vide(), 1, (0, 9), 1))
    print(peut_placer(genere_grille_vide(), 2, (0, 9), 1))


if __name__ == "__main__":
    main()
