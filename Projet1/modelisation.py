import Joueur as jr
import Bataille as btl
import naval as nvl

import time

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def partie(joueur, afficher=False, laps=1, clear=True) :
    # tirage aléatoire d'une grille
    jeu = btl.Bataille()
    cpt = 0

    if (afficher) :
        if clear :
            cls()
        jeu.affiche()
        time.sleep(laps)
    # Tant que le joueur n'a pas gagné :
    while (not jeu.victoire()) :
        cpt += 1
        # Toucher une position selon la stratégie du joueur (hasard ou
        # heuristique ou autre)
        joueur.joue(jeu)

        if (afficher) :
            if clear :
                cls()
            jeu.affiche()
            time.sleep(laps)

    if afficher :
        print("Victoire du joueur en " + str(cpt) + " tours")
        print("Stratégie : " + joueur.__doc__)
    return cpt

def demo_jA() :
    partie(jr.JoueurAlea(), afficher=True, laps=0.25)

def demo_jH() :
    partie(jr.JoueurHeuristique(), afficher=True, laps=0.3)

def demo_jL() :
    partie(jr.JoueurLigne(), afficher=True, laps=0.3)

def demo_jP() :
    partie(jr.JoueurProba(), afficher=True, laps=0.25)


# def esperance(joueur) :
#     cpt = 0
#     coups = 0
#     for i in range(1000) :
#         cpt += 1
#         coups += partie(joueur, afficher=False)
#     return cpt, coups

def distrib(joueur) :

    coups = [0 for i in range(17, 101)]
    str = "\n["
    for i in range(1000) :
        if i%100 == 0 :
            cls()
            print(str + "#" * int(i/100) + " " * int(10 - i/100) + "]")
        coups[partie(joueur, afficher=False) - 17] += 1
        joueur.__init__()
    cls()
    return i+1, coups

def histo(liste, xBounds, yBounds) :
    xmin, xmax = xBounds
    ymin, ymax = yBounds

    string = ""

    string += "┌" + "─" * len(liste) + "┐\n"

    for i in range(ymax, ymin, -1) :
        string += "│"
        for j in range(xmin, xmax+1) :
            if liste[j-xmin] < i :
                string += " "
            else :
                string += "#"
        string += "│\n"


    string += "└" + "─" * len(liste) + "┘\n"

    return string

def stats_j(joueur) :
    cpt, coups = distrib(joueur)
    esp = 0
    for i in range(17, 101) :
        esp += i * coups[i-17]
    esp = esp/cpt
    print("\nEspérance du nombre de tours avant victoire pour "+joueur.nom+" : " + str(esp))
    input("\n\nAppuyez sur entrer...")

    upperbound = max(coups)

    # print(histo(coups, (17, 100), (0, upperbound)))
    nvl.affiche_tabl(
                    [
                    ["Tour"] + [i for i in range(17, 101)],
                    ["Nb de victoires"] + coups
                    ]
                    , 21, invert=True)

    print("(" + str(cpt) + " itérations)")
    # print("("+ str(round(end_time - start_time)) +"s)")

    return cpt, esp


def stats_jA() :
    return stats_j(jr.JoueurAlea())

def stats_jH() :
    return stats_j(jr.JoueurHeuristique())

def stats_jL() :
    return stats_j(jr.JoueurLigne())

def stats_jP() :
    return stats_j(jr.JoueurProba())



def main() :

    func = "Undefined"

    switcher =  {
        "1": demo_jA,
        "2": demo_jH,
        "3": demo_jL,
        "4": demo_jP,
        "11": stats_jA,
        "21": stats_jH,
        "31": stats_jL,
        "41": stats_jP,
        "0": exit
    }
    cls()
    request = "Choisissez une opération (tapez le nombre correspondant) :"

    print("\n-= Modélisation probabiliste du jeu de la bataille navale =-\n")

    while func == "Undefined" :
        print("~" * len(request))
        rep = input(
        request + "\n\
 1 - Démo JoueurAléatoire\n\
 2 - Démo JoueurHeuristique\n\
 3 - Démo Heuristique ligne\n\
 4 - Démo Probabiliste\n\
11 - Stats sur Aléa\n\
21 - Stats sur heuristique\n\
31 - Stats sur heuristique ligne\n\
41 - Stats sur probabiliste\n\
 0 - Quitter\n\
 >>> "
        )

        func = switcher.get(rep, "Undefined")

        if (func == "Undefined") :
            print("\nErreur : entrée invalide.\n")
            input("\n\nAppuyez sur entrer...")
            cls()

            rep = 0
            func = "Undefined"

        if int(rep) != 0 :
            print()
            # partie(func)
            func()
            input("\n\nAppuyez sur entrer...")
            cls()

            func = "Undefined"

if __name__ == "__main__" :
    main()
