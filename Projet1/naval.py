#import numpy as np
from random import *
import matplotlib.pyplot as plt
import time

# x_ascii : boolean, vrai si les caractères de l'ascii étendu sont autorisés
x_ascii = True

""" reference : dict(int : (str, int))
Structure qui pour un type de case associe un nom et une valeur : sa taille si
c'est un bateau.
"""
reference = {
    0 : ('vide', 0),
    1 : ('porte-avions', 5),
    2 : ('croiseur', 4),
    3 : ('contre-torpilleurs', 3),
    4 : ('sous-marin', 3),
    5 : ('torpilleur', 2),
    6 : ('tiré', -1),
    7 : ('touché', -2)
}


""" symbols : dict(str, char)
Associe un symbole à un type de case.
"""
symbols = {}
if x_ascii :
    symbols = {
        "miss" : "X",
        "hit" : "!",
        "boat" : "■",
        "corner_high_left" : "┌",
        "corner_high_right" : "┐",
        "corner_low_left" : "└",
        "corner_low_right" : "┘",
        "vertical_bar" : "│",
        "horizontal_bar" : "─"
    }
else :
    symbols = {
        "miss" : "X",
        "hit" : "!",
        "boat" : "O",
        "corner_high_left" : "+",
        "corner_high_right" : "+",
        "corner_low_left" : "+",
        "corner_low_right" : "+",
        "vertical_bar" : "|",
        "horizontal_bar" : "~"
    }


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
    for i in range((reference[bateau])[1]) :
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
    for i in range((reference[bateau])[1]) :
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

def affiche(grille) :
    """ list(list(int)) * int  -> void
    Affiche la grille de jeu (utiliser imshow du module matplotlib.pyplot).
    """
    plt.grid(True)
    plt.imshow(grille)
    plt.show()

def eq(grilleA,grilleB) :
    """ list(list(int)) * list(list(int)) -> bool
    Teste l’égalité entre deux grilles
    """
    for i in range (len(grilleA)):
        for j in range (len(grilleA[0])):
            if grilleA[i][j] != grilleB[i][j]:
                return False
    return True

# def genere_grille():
#     """ void -> list(list(int))
#     Rend une grille avec les bateaux disposés de manière aléatoire
#     """
#     return genere_grille_list([i for i in range(1, 6)])

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

def pos_des_bateauxrec(grille, liste) :
    """ list(list(int)) * list(int) -> int
    Rend le nombre de possibilité de placer des bateaux dans une grille
    récursivement
    """
    cpt = 0
    if len(liste) == 0 :
        return 1
    else :
        for i in range(10):
            for j in range(10):
                """
                Si placer le premier bateau de la liste en (i,j) dans la grille
                horizontalement est possible :
                """
                if (peut_placer(grille, liste[0], (i,j), 1)):
                    """
                    On ajoute à cpt le résultat de pos_des_bateauxres appliqué
                    à la grille avec le premier bateau de la liste placé en
                    (i,j) horizontalement
                    """
                    cpt += pos_des_bateauxrec(place(copyMat(grille), liste[0], (i,j), 1), liste[1:])
                if (peut_placer(grille, liste[0], (i,j), 2)):
                    """
                    On ajoute à cpt le résultat de pos_des_bateauxres appliqué
                    à la grille avec le premier bateau de la liste placé en
                    (i,j) verticalement
                    """
                    cpt += pos_des_bateauxrec(place(copyMat(grille), liste[0], (i,j), 2), liste[1:])
        return cpt

def copyMat(grille) :
    """ list(list(int)) -> list(list(int))
    Renvoie la copie de grille
    """
    nouvGrille = genere_grille_vide()
    for i in range(len(grille)) :
        for j in range(len(grille[0])) :
            nouvGrille[i][j] = grille[i][j]
    return nouvGrille

def pos_des_bateaux(liste):
    """ list(int) -> int
    Rend le nombre de possibilité de placer des bateaux dans une grille vide
    """
    return pos_des_bateauxrec(genere_grille_vide(), liste)

def affiche_mat(grille) :
    """ list(list(alpha)) -> str
    Renvoie une chaine de caractère représentant la matrice passée en paramètre.
    """
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
    # grilleGeneree : list(list(int))
    grilleGeneree = genere_grille_list(listNum)

    # cpt : int
    cpt = 1

    while not eq(grille, grilleGeneree) :
        grilleGeneree = genere_grille_list(listNum)
        cpt += 1

    return cpt

def test_grilleAleaEgale(sec, listNum) :
    """ Pour une durée donnée, itère autant que possible sur la fonction
    grilleAleaEgale pour donner au final une moyenne des résultats obtenus.
    Fait des affichages informatifs en cours de route.

    Entrée :
     --     sec : durée en secondes (int)
     -- listNum : liste de bateau (list(int))

    Sortie :
     -- (int)
    """
    print()
    print("Test grilleAleaEgale ("+str(sec)+"s, "+ str(listNum) +")")
    # cpt : int, somme des résultats des appels successifs à grilleAleaEgale
    cpt = 0

    # nb : int, nombre d'itérations
    nb = 1

    # res : int, moyenne des résultats des appels successifs à grilleAleaEgale
    res = 0

    # start_time : double?
    start_time = time.clock()

    # end_time : double?
    end_time = 0.0

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
    return res, nb

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
    """ Etant donnée une liste de listes, renvoie la longueur de la liste
    contenue la plus longue.
    """
    maxi = 0
    for x in liste :
        maxi = max(len(x), maxi)
    return maxi

def affiche_tabl(mat, invert=False, replace=("0", "0")) :
    """ Affiche d'une façon élégante une matrice d'éléments sous la forme d'un
    tableau.

    Entrée :
     --   mat : list(list(alpha))
     --  invert : boolean
            Si égal à True, les lignes deviennent colonnes et inversement.
     -- replace : (str, str)
            Pendant la construction du tableau, si un élément est égal à
            replace[0] après avoir été converti en str, est remplacé par
            replace[1].

    Sortie :
     -- : void
    """
    # matyCopy : list(list(alpha))
    matCopy = mat.copy()

    """ Processus d'inversion """
    if invert :
        matCopy2 = [[] for j in range(len(matCopy[0]))]
        for i in range(len(matCopy)) :
            for j in range(len(matCopy[i])) :
                matCopy2[j].append(matCopy[i][j])
        matCopy = matCopy2
    """                       """

    # sizes : list(int), liste des tailles des colonnes
    sizes = [0] * len(matCopy[0])

    """ Mise à jour des tailles optimales des colonnes """
    for i in range(len(matCopy)) :
        for j in range(len(matCopy[i])) :
            # sizes[j] prend pour valeur la longueur du plus long élément de la
            # colonne j
            sizes[j] = max(sizes[j], len(str(matCopy[i][j])))
    """                                                """

    """ Insertion d'une ligne de séparation (pour les intitulés de colonnes) """
    matCopy.insert(1, ["-" * (sizes[i]) for i in range(len(matCopy[0]))])

    # tab : str, résultat
    tab = symbols["corner_high_left"]

    for j in range(len(matCopy[i])) :
        tab += symbols["horizontal_bar"] * (sizes[j] + 2)

    tab += symbols["horizontal_bar"] * (len(matCopy[0]) - 1) +\
            symbols["corner_high_right"]+"\n"

    for i in range(len(matCopy)) :
        tab += symbols["vertical_bar"]

        for j in range(len(matCopy[i])) :
            tab += " "

            if str(matCopy[i][j]) == replace[0] :
                tab += replace[1] + " " * ((sizes[j]) - len(str(matCopy[i][j])))

            else :
                tab += str(matCopy[i][j]) + " " * ((sizes[j]) - len(str(matCopy[i][j])))
            tab += " " + symbols["vertical_bar"]
        tab += "\n"
    tab += symbols["corner_low_left"]

    for j in range(len(matCopy[i])) :
        tab += symbols["horizontal_bar"] * (sizes[j] + 2)

    tab += symbols["horizontal_bar"] * (len(matCopy[0]) - 1) \+
    symbols["corner_low_right"]

    print(tab)

def afficherLegende() :
    """ Affiche une légende des symboles utilisés."""
    print("    '"+symbols["hit"]+"' : bateau touché\n    '"+symbols["boat"]+"' : bateau\n    '"+symbols["miss"]+"' : coup raté\n")

def frame_bataille(mat, humain=False, cacher=False) :
    """ Retourne une chaine de caractère représentant un plateau de jeu de
    bataille navale, encadré.

    Entrée :
    --   mat : list(list(alpha))
    --  humain : boolean
            Si égal à True, ajoutera aux axes une graduation allant de A à J
            pour la verticale et de 1 à 10 pour l'horizontale
            (origine : haut gauche)
    --  cacher : boolean
            Si égal à True, cachera les cases bateaux, mais indiquera le nmbre
            de bateaux restants
    Sortie :
    -- res : str
    """
    # bats : set(), bateaux restants
    bats = set()

    # res : str, resultat
    res = ""
    """ Ajout de la graduation horizonale """
    if humain :
        res += "   "
        for i in range(10) :
            res += " " + str(i +1) + " "
        res += "\n  "

    # res += "┌" + "───" * len(mat[0]) + "┐\n"
    res += symbols["corner_high_left"] + symbols["horizontal_bar"] * 3 * len(mat[0]) + symbols["corner_high_right"] +"\n"

    for i in range(len(mat)) :
        if humain :
            # res += chr(ord('A') + i) + " │"
            res += chr(ord('A') + i) + " " + symbols["vertical_bar"]

        else :
            # res += "│"
            res += symbols["vertical_bar"]
        for j in range(len(mat[0])) :
            if mat[i][j] == 0 :
                res += "   "

            elif mat[i][j] == -1 :
                # res += " X "
                res += " "+symbols["miss"]+" "
            elif mat[i][j] == -2 :
                # res += " ! "
                res += " "+symbols["hit"]+" "
            elif cacher :
                bats.add(mat[i][j])
                res += "   "
            else :
                # res += " ■ "
                res += " "+symbols["boat"]+" "
        # res += "│\n"
        res += symbols["vertical_bar"]+"\n"

    if humain :
        # res += "  └" + "───" * len(mat[0]) + "┘\n"
        res += "  "+symbols["corner_low_left"] + symbols["horizontal_bar"] * 3 * len(mat[0]) + symbols["corner_low_right"] +"\n"
        if cacher :
            res += "Nombre de bateaux restants : " + str(len(bats))
    else :
        # res += "└" + "───" * len(mat[0]) + "┘\n"
        res += symbols["corner_low_left"] + symbols["horizontal_bar"] * 3 * len(mat[0]) + symbols["corner_low_right"] +"\n"

    return res

def test_tirage(nbCorrect, nbTotal) :
    vict = True
    list = [i for i in range(nbTotal)]
    res = []
    nb = 0
    for i in range(nbTotal) :
        nb+=1
        x = randint(0, len(list) - 1)
        res.append(list[x])
        list.remove(list[x])
        for j in range(nbCorrect) :
            if j not in res :
                vict = False
                break
        if vict :
            break
        else :
            vict = True
    return nb


## TESTS

def main() :

    # cpt = 0
    # for i in range(1000000) :
    #
    #     cpt+=(test_tirage(2, 5))
    # print("moyenne ~~~ = ", str(cpt/1000000))

    print(peut_placer(genere_grille_vide(), 1, (0, 0), 1))
    print(peut_placer(genere_grille_vide(), 1, (9, 9), 1))

    print(peut_placer(genere_grille_vide(), 1, (9, 0), 1))
    print(peut_placer(genere_grille_vide(), 2, (9, 0), 1))
    print(peut_placer(genere_grille_vide(), 1, (0, 9), 1))
    print(peut_placer(genere_grille_vide(), 2, (0, 9), 1))
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
                    li1])


    print()
    colNames = ["Fonction\\Nombre de bateaux", "1", "2", "3"]
    li1 = [
        "pos_des_bateaux",
        pos_des_bateaux([5]),
        pos_des_bateaux([5,4]),
        "pos_des_bateaux([5,4,3])",
    ]


    affiche_tabl([  colNames,
                    li1])



    print()
    colNames = ["test_grilleAleaEgale pour 15s\\Nombre de bateaux", "1", "2", "3", "4", "5"]
    li1 = [
        "(Nb d'itérations, nb de grilles)",
        test_grilleAleaEgale(15, [5]),
        test_grilleAleaEgale(15, [5, 4]),
        test_grilleAleaEgale(15, [5, 4, 3]),
        "test_grilleAleaEgale(60, [5, 4, 3, 2])",
        "test_grilleAleaEgale(60, [5, 4, 3, 2, 1])"
    ]

    affiche_tabl([  colNames,
                    li1])



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
                    li4])


    # print(pos_des_bateaux([5, 4, 3])) # Trop long

    # test_grilleAleaEgale(15, [5])
    # test_grilleAleaEgale(15, [5, 4])
    # test_grilleAleaEgale(15, [0, 0])
    # test_grilleAleaEgale(15, [4])


if __name__ == "__main__":
    main()
