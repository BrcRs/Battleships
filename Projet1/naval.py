#import numpy as np
from random import *
import matplotlib.pyplot as plt
import time

"""
Par convention, la position d'un bateau sera sa case la plus à gauche s'il est
horizontal, et sa case la plus en haut dans le cas où il est vertical.
"""
reference = {
    0 : ['vide', 0],
    1 : ['porte-avions', 5],
    2 : ['croiseur', 4],
    3 : ['contre-torpilleurs', 3],
    4 : ['sous-marin', 3],
    5 : ['torpilleur', 2],
    6 : ['touché', -1]
}

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
    Rend la grille modifiée (s’il est possible de placer le bateau).
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
    Place aléatoirement le bateau dansla grille : la fonction tire uniformément
    une position et une direction aléatoires et tente de placer le bateau ; s’il
    n’est pas possible de placer le bateau, un nouveau tirage est effectué et ce
    jusqu’à ce que le positionnement soit admissible.

    TODO : Que se passe-t-il quand aucune place n'est disponible ?
    """
    x = randint(0, 9)
    y = randint(0, 9)
    d = randint(1,2)
    while not (peut_placer(grille, bateau, (x,y), d)) :
        # print(".", end="")
        x = randint(0, 9)
        y = randint(0, 9)
        d = randint(1,2)
        # print("Placer " + str(bateau) + " en " + str((x, y)) + " avec d = " + str(d) + " dans \n" + affiche_mat(grille) + "\n ?")
        # time.sleep(0.5)
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

def genere_grille_list(listNum):
    """ list(int) -> list(list(int))
    Rend une grille avec les bateaux disposés de manière aléatoire
    """
    matrice = [[0 for y in range(10)] for x in range(10)]
    for i in listNum:
        # if len(listNum) == 1 :
            # print(i)
            # time.sleep(0.001)
        place_alea(matrice, i)
    return matrice

def genere_grille_vide() :
    """ void -> list(list(int))
    Renvoie une grille vide
    """
    return [[0 for y in range(10)] for x in range(10)]

def pos_un_bateau(grille, num) :
    """ list(list(int)) * int -> int
    Rend le nombre de possibilité de placer un bateau dans une grille donnée
    """
    cpt = 0
    for i in range(10):
        for j in range(10):
            if (peut_placer(grille, num, (i,j), 1)):
                cpt=cpt+1
            if (peut_placer(grille, num, (i,j), 2)):
                cpt=cpt+1
    return cpt

def pos_des_bateauxrec(grille, liste, cpt) :
    """ list(list(int)) * list(int) * int -> int
    Rend le nombre de possibilité de placer des bateaux dans une grille
    """
    # print("=- APPEL pos_des_bateauxrec -=\navec :\ngrille :\n"+affiche_mat(grille)+"\nliste :\n"+str(liste)+"\ncpt :\n"+str(cpt))
    # time.sleep(0.005125)
    if len(liste) == 0 :
        return 1
    else :
        for i in range(10):
            for j in range(10):
                if (peut_placer(grille, liste[0], (i,j), 1)):
                    cpt += pos_des_bateauxrec(place(copyMat(grille), liste[0], (i,j), 1), liste[1:], 0)
                if (peut_placer(grille, liste[0], (i,j), 2)):
                    cpt += pos_des_bateauxrec(place(copyMat(grille), liste[0], (i,j), 2), liste[1:], 0)
        # print("return cpt =", cpt)
        # time.sleep(1)
        return cpt

def copyMat(grille) :
    nouvGrille = genere_grille_vide()
    for i in range(len(grille)) :
        for j in range(len(grille[0])) :
            nouvGrille[i][j] = grille[i][j]
    return nouvGrille

def pos_des_bateaux(liste):
    """ list(int) -> int
    Rend le nombre de possibilité de placer des bateaux dans une grille vide
    """
    return pos_des_bateauxrec(genere_grille_vide(), liste, 0)

def affiche_mat(grille) :
    string = ""
    for i in range(len(grille)) :
        for j in range(len(grille[0])) :
            if (grille[i][j] == 0) :
                string += " \t"

            else :
                string += str(grille[i][j]) + "\t"
        string += "\n"
    return string

def grilleAleaEgale(grille, listNum) :
    """ list(list(int)) * list(int) -> int
    Prend en paramètre une grille, génère des grilles aléatoirement jusqu’à ce
    que la grille générée soit égale à la grille passée en paramètre et qui
    renvoie le nombre de grilles générées.
    """
    grilleGeneree = genere_grille_list(listNum)
    cpt = 1
    # print(affiche_mat(grille))
    # print()
    # print(affiche_mat(grilleGeneree))
    # print("=" * 60)
    while not eq(grille, grilleGeneree) :
        grilleGeneree = genere_grille_list(listNum)
        cpt += 1
        # print("\n" * 2)
        # print(affiche_mat(grille))
        # print("- " * 30)
        # print(affiche_mat(grilleGeneree))
        # print("=" * 60)
        # time.sleep(0.01)

    return cpt

def test_grilleAleaEgale(sec, listNum) :
    """ Pour une durée donnée, itère autant que possible sur la fonction
    grilleAleaEgale pour donner au final une moyenne des résultats obtenus.

    Entrée :
     --     sec : durée en secondes (int)
     -- listNum : liste de bateau (list(int))

    Sortie :
     -- (int)
    """
    print()
    print("Test grilleAleaEgale ("+str(sec)+"s, "+ str(listNum) +")")
    cpt = 0
    nb = 1
    res = 0
    start_time = time.clock()
    end_time = 0
    while (True) :
        end_time = time.clock()
        if (end_time - start_time > sec) :
            break
        cpt += grilleAleaEgale(genere_grille_list(listNum), listNum)
        nb += 1
    res = (cpt // nb)
    print("Moyenne pour grilleAleaEgale avec "+ str(listNum) +" : " + str(res))
    print("(" + str(nb) + " itérations)")
    print("("+ str(round(end_time - start_time)) +"s)")
    return res

def approx_nbGrille1(listNum) :
    """ Renvoie une approximation du nombre de grilles différentes possibles
    contenant la liste de bateaux passée en paramètre.

    Une manière un peu bourrine consiste à multiplier les résultats respectifs
    de la fonction 'pos_un_bateau(...) appliquée aux différents bateaux de
    'listNum.
    """
    res = 1
    for i in listNum :
        res *= pos_un_bateau(genere_grille_vide(), i)
    return res

def approx_nbGrille2(listNum) :
    """ Renvoie une approximation du nombre de grilles différentes possibles
    contenant la liste de bateaux passée en paramètre.

    Une manière consiste à calculer le nombre de grilles possibles en plaçant le
    premier bateau, puis placer ce bateau dans une nouvelle grille, puis
    calculer le nombre de grilles possibles en plaçant le second bateau dans
    cette nouvelle grille et ainsi de suite.
    """
    res = 1
    grilleCour = genere_grille_vide()
    for i in listNum :
        res *= pos_un_bateau(grilleCour, i)
        place_alea(grilleCour, i)

    return res

def maxLen(liste) :
    maxi = 0
    for x in liste :
        maxi = max(len(x), maxi)
    return maxi

def affiche_tabl(liste, colSize=10) :
    """ Affiche d'une façon élégante une liste d'éléments sous la forme d'un
    tableau
    """

    listeCopy = liste.copy()

    sizes = [0] * len(liste[0])
    for i in range(len(listeCopy)) :
        for j in range(len(listeCopy[i])) :
            sizes[j] = max(sizes[j], len(str(listeCopy[i][j])))


    listeCopy.insert(1, ["-" * (sizes[i]) for i in range(len(liste[0]))])
    form = ""


    form += "┌"
    for j in range(len(listeCopy[i])) :
        form += "─" * (sizes[j] + 2)
    form += "─" * (len(listeCopy[0]) - 1)
    form += "┐\n"

    for i in range(len(listeCopy)) :
        form += "│"
        for j in range(len(listeCopy[i])) :
            form += " "
            form += str(listeCopy[i][j]) + " " * ((sizes[j]) - len(str(listeCopy[i][j])))
            form += " │"
        form += "\n"

    form += "└"
    for j in range(len(listeCopy[i])) :
        form += "─" * (sizes[j] + 2)
    form += "─" * (len(listeCopy[0]) - 1)
    form += "┘"
    print(form)

def frame_bataille(mat) :
    string = "\n" * 10

    string += "┌" + "───" * len(mat[0]) + "┐\n"

    for i in range(len(mat)) :
        string += "│"
        for j in range(len(mat[0])) :
            if mat[i][j] == 0 :
                string += "   "

            elif mat[i][j] == -1 :
                string += " X "
            else :
                string += " O "
        string += "│\n"


    string += "└" + "───" * len(mat[0]) + "┘\n"

    return string


## TESTS

def main() :

    print(peut_placer(matricetest, 1, (0, 0), 1))
    print(peut_placer(matricetest, 1, (9, 9), 1))

    print(peut_placer(matricetest, 1, (9, 0), 1))
    print(peut_placer(matricetest, 2, (9, 0), 1))
    print(peut_placer(matricetest, 1, (0, 9), 1))
    print(peut_placer(matricetest, 2, (0, 9), 1))
    print(pos_un_bateau(genere_grille_vide(), 5))

    print()
    colNames = ["", "2", "3", "4", "5"]
    li1 = [
    "pos_un_bateau",
    pos_un_bateau(genere_grille_vide(), 1),
    pos_un_bateau(genere_grille_vide(), 2),
    pos_un_bateau(genere_grille_vide(), 3),
    pos_un_bateau(genere_grille_vide(), 5)
    ]


    affiche_tabl([  colNames,
                    li1
                    ], 21)

    print()
    colNames = ["Fonction\\Nombre de bateaux", "1", "2", "3"]
    li1 = [
    "pos_des_bateaux",
    pos_des_bateaux([5]),
    pos_des_bateaux([5,4]),
    "pos_des_bateaux([5,4,3])",
    ]


    affiche_tabl([  colNames,
                    li1
                    ], 21)


    print()
    colNames = ["Valeurs à tester", "pos_des_bateaux", "approx_nbGrille1", "approx_nbGrille2"]
    li1 = [
    "[5, 4]",
    pos_des_bateaux([5,4]),
    approx_nbGrille1([5,4]),
    approx_nbGrille2([5,4])
    ]
    li2 = [
    "[3, 4]",
    pos_des_bateaux([3,4]),
    approx_nbGrille1([3,4]),
    approx_nbGrille2([3,4])
    ]
    li3 = [
    "[2, 4]",
    pos_des_bateaux([2,4]),
    approx_nbGrille1([2,4]),
    approx_nbGrille2([2,4])
    ]
    li4 = [
    "[5, 3]",
    pos_des_bateaux([5,3]),
    approx_nbGrille1([5,3]),
    approx_nbGrille2([5,3])
    ]

    affiche_tabl([  colNames,
                    li1,
                    li2,
                    li3,
                    li4
                    ], 21)

    # print(pos_des_bateaux([5, 4, 3])) # Trop long

    # test_grilleAleaEgale(15, [5])
    # test_grilleAleaEgale(15, [5, 4])
    # test_grilleAleaEgale(15, [0, 0])
    # test_grilleAleaEgale(15, [4])


if __name__ == "__main__":
    main()
