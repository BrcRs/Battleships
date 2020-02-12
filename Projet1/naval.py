import numpy as np
from random import *
import matplotlib.pyplot as plt

"""
Par convention, la position d'un bateau sera sa case la plus à gauche s'il est
horizontal, et sa case la plus en haut dans le cas où il est vertical.
"""
reference ={0 : ['vide', 0],1 : ['porte-avions', 5],2 : ['croiseur', 4],3 : ['contre-torpilleurs', 3],4 : ['sous-marin', 3], 5 : ['torpilleur', 2]}

matricetest = [[0 for y in range(10)] for x in range(10)]

def peut_placer(grille, bateau, position, direction) :
    """ list(list(int)) * int * (int, int) * int -> bool
    Rend vrai s’il est possible de placer le bateau sur
    la grille (i.e. toutes les cases que doit occuper le
    bateau sont libres) à la position et dans la direction
    donnée (vous pouvez coder laposition comme un couple
    d’entier et la direction par 2 entiers, par exemple 1
    pour horizontal, 2 pour vertical).
    """
    x, y = position
    h = 0
    v = 0
    for i in range((reference[bateau])[1]) :
        if direction == 1 :
            h = i
        else :
            v = i
        if x+v >= (len(grille)) or y+h >= (len(grille[0])) or grille[x+v][y+h] != 0 :
            return False

    return True

def place(grille, bateau, position, direction) :
    """ list(list(int)) * int * (int, int) * int -> bool
    Rend la grille modi-fiée (s’il est possible de placer le bateau).
    """
    x, y = position
    h = 0
    v = 0
    for i in range((reference[bateau])[1]) :
        if direction == 1 :
            h = i
        else :
            v = i
        grille[x+v][y+h] = bateau

    return grille


def place_alea(grille, bateau) :
    """ list(list(int)) * int  -> void
    Place aléatoirement le bateau dansla grille : la fonction tire uniformément une position et une direction aléatoires et tente
    de placer le bateau ; s’il n’est pas possible de placer le bateau, un nouveau tirage est effectué et ce jusqu’à ce que le positionnement soit admissible
    """
    x = randint(0, 9)
    y = randint(0, 9)
    d = randint(1,2)
    while not (peut_placer(grille, bateau, (x,y), d)) :
        x = randint(0, 9)
        y = randint(0, 9)
        d = randint(1,2)
    place(grille, bateau, (x,y), d)

def affiche(grille) :
    """ list(list(int)) * int  -> void
    Affiche la grille de jeu (utiliserimshowdu modulematplotlib.pyplot).
    """
    plt.grid(True)
    plt.imshow(grille)
    plt.show()

def eq(grilleA,grilleB) :
    """ list(list(int)) * list(list(int)) -> bool
    Tester l’égalité entre deux grilles
    """
    for i in range (len(grilleA)):
        for j in range (len(grilleA[0])):
            if grilleA[i][j] != grilleB[i][j]:
                return False
    return True

def genere_grille():
    """ void -> list(list(int))
    Rend une grille avec les bateaux disposés de manière aléatoire
    """
    matrice = [[0 for y in range(10)] for x in range(10)]
    for i in range (1, 6):
        place_alea(matrice, i)
    return matrice


### TESTS

print(peut_placer(matricetest, 1, (0, 0), 1))
print(peut_placer(matricetest, 1, (9, 9), 1))

print(peut_placer(matricetest, 1, (9, 0), 1))
print(peut_placer(matricetest, 2, (9, 0), 1))
print(peut_placer(matricetest, 1, (0, 9), 1))
print(peut_placer(matricetest, 2, (0, 9), 1))
place_alea(matricetest, 1)
affiche(genere_grille())
# affiche(matricetest)
