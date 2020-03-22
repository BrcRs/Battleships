import tools as tls
import naval as nvl
import display as dply
import time

def pos_un_bateau(grille, num) :
    """ list(list(int)) * int -> int
    Rend le nombre de possibilité de placer un bateau dans une grille donnée
    """
    cpt = 0
    for i in range(10):
        for j in range(10):
            if (nvl.peut_placer(grille, num, (i,j), 1)):
                cpt=cpt+1
            if (nvl.peut_placer(grille, num, (i,j), 2)):
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
                if (nvl.peut_placer(grille, liste[0], (i,j), 1)):
                    """
                    On ajoute à cpt le résultat de pos_des_bateauxres appliqué
                    à la grille avec le premier bateau de la liste placé en
                    (i,j) horizontalement
                    """
                    cpt += pos_des_bateauxrec(nvl.place(tls.copyMat(grille), liste[0], (i,j), 1), liste[1:])
                if (nvl.peut_placer(grille, liste[0], (i,j), 2)):
                    """
                    On ajoute à cpt le résultat de pos_des_bateauxres appliqué
                    à la grille avec le premier bateau de la liste placé en
                    (i,j) verticalement
                    """
                    cpt += pos_des_bateauxrec(nvl.place(tls.copyMat(grille), liste[0], (i,j), 2), liste[1:])
        return cpt

def pos_des_bateaux(liste):
    """ list(int) -> int
    Rend le nombre de possibilité de placer des bateaux dans une grille vide
    """
    return pos_des_bateauxrec(nvl.genere_grille_vide(), liste)


def grilleAleaEgale(grille, listNum) :
    """ list(list(int)) * list(int) -> int
    Prend en paramètre une grille, génère des grilles aléatoirement jusqu’à ce
    que la grille générée soit égale à la grille passée en paramètre et qui
    renvoie le nombre de grilles générées.
    """
    # grilleGeneree : list(list(int))
    grilleGeneree = nvl.genere_grille_list(listNum)

    # cpt : int
    cpt = 1

    while not tls.eq(grille, grilleGeneree) :
        grilleGeneree = nvl.genere_grille_list(listNum)
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
        cpt += grilleAleaEgale(nvl.genere_grille_list(listNum), listNum)
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
        res *= pos_un_bateau(nvl.genere_grille_vide(), i)
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
    grilleCour = nvl.genere_grille_vide()
    for i in listNum :
        res *= pos_un_bateau(grilleCour, i)
        nvl.place_alea(grilleCour, i)

    return res

""" TESTS """
def main() :

    print(pos_un_bateau(nvl.genere_grille_vide(), 5))

    print()
    colNames = ["", "2", "3", "4", "5"]
    li1 = [
        "pos_un_bateau",
        pos_un_bateau(nvl.genere_grille_vide(), 1),
        pos_un_bateau(nvl.genere_grille_vide(), 2),
        pos_un_bateau(nvl.genere_grille_vide(), 3),
        pos_un_bateau(nvl.genere_grille_vide(), 5)
    ]


    dply.affiche_tabl([  colNames,
                    li1])


    print()
    colNames = ["Fonction\\Nombre de bateaux", "1", "2", "3", "4", "5"]
    li1 = [
        "pos_des_bateaux",
        pos_des_bateaux([5]),
        pos_des_bateaux([5,4]),
        "pos_des_bateaux([5,4,3])",
        "pos_des_bateaux([5,4,3,2])",
        "pos_des_bateaux([5,4,3,2,1])"
    ]


    dply.affiche_tabl([  colNames,
                    li1])



    print()
    # colNames = ["test_grilleAleaEgale pour 15s\\Nombre de bateaux", "1", "2", "3", "4", "5"]
    # li1 = [
    #     "(Nb d'itérations, nb de grilles)",
    #     test_grilleAleaEgale(15, [5]),
    #     test_grilleAleaEgale(15, [5, 4]),
    #     test_grilleAleaEgale(15, [5, 4, 3]),
    #     "test_grilleAleaEgale(60, [5, 4, 3, 2])",
    #     "test_grilleAleaEgale(60, [5, 4, 3, 2, 1])"
    # ]
    #
    # dply.affiche_tabl([  colNames,
    #                 li1])



    print()
    colNames = ["Valeurs à tester", "pos_des_bateaux", "approx_nbGrille1", "approx_nbGrille2"]

    li1 = [
        "[5]",
        pos_des_bateaux([5]),
        approx_nbGrille1([5]),
        approx_nbGrille2([5])
    ]
    li2 = [
        "[5, 4]",
        pos_des_bateaux([5, 4]),
        approx_nbGrille1([5, 4]),
        approx_nbGrille2([5, 4])
    ]
    li3 = [
        "[5, 4, 3]",
        "/",
        # pos_des_bateaux([5, 4, 3]),
        approx_nbGrille1([5, 4, 3]),
        approx_nbGrille2([5, 4, 3])
    ]
    li4 = [
        "[5, 4, 3, 2]",
        "/",
        # pos_des_bateaux([5, 4, 3, 2]),
        approx_nbGrille1([5, 4, 3, 2]),
        approx_nbGrille2([5, 4, 3, 2])
    ]
    li5 = [
        "[5, 4, 3, 2, 1]",
        "/",
        # "pos_des_bateaux([5, 4, 3, 2, 1])",
        approx_nbGrille1([5, 4, 3, 2, 1]),
        approx_nbGrille2([5, 4, 3, 2, 1])
    ]
    dply.affiche_tabl([  colNames,
                    li1,
                    li2,
                    li3,
                    li4,
                    li5])

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

    dply.affiche_tabl([  colNames,
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
