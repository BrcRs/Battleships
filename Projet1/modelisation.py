import Joueur as jr
import Bataille as btl
import naval as nvl
import display as dply

import time

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def partie(joueur, afficher=False, laps=1, clear=True, humain=False) :
    """Fait jouer une IA à la bataille navale

    Entrée :
    -- joueur : Joueur
            Comme son nom ne l'indique pas, c'est l'IA.
    -- afficher : boolean
            Mettre à True fait afficher la grille en animation
    -- laps : int
            Laps de temps entre deux tours
    -- clear : boolean
            Fait appel à la commande clear du terminal entre deux affichages si
            mis à True.
    -- humain : boolean
            Affichera une graduation autour de la grille de jeu si égal à True.
    Sortie :
    -- : int
            Nombre de tours avant victoire.
    """
    # tirage aléatoire d'une grille
    jeu = btl.Bataille()
    cpt = 0

    if (afficher) :
        if clear :
            cls()
        jeu.affiche(humain)
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
            jeu.affiche(humain)
            time.sleep(laps)

    if afficher :
        print("-= Victoire du joueur en " + str(cpt) + " tours =-")
        print("Stratégie : " + joueur.__doc__)
    return cpt

def partieVs(j2) :
    """ Fait jouer un joueur humain contre un autre joueur ou une IA
    (dépend de la nature de j2)
    """
    multi = isinstance(j2, jr.JoueurHumain)
    effect = 0
    j1 = jr.JoueurHumain(j2)
    if multi :
        j2.setAdversaire(j1)
    laps = 1
    jeu_j2 = btl.Bataille()
    jeu_j1 = btl.Bataille()

    time.sleep(laps)
    cpt = 0
    while (not jeu_j2.victoire() and not jeu_j1.victoire()) :
        cpt += 1
        if multi :
            cls()
            input("\n=-- Tour de J1 :"+j1.nom+" --=\n(appuyez sur entrer quand vous êtes prêt...)")
        effect = 1
        while effect > 0 and not (jeu_j2.victoire() or jeu_j1.victoire()) :
            cls()
            print("\n ~~~===> JOUEUR 1\n")

            jeu_j2.affiche(humain=True, cacher=True)
            print()
            jeu_j1.affiche(humain=True)
            dply.afficherLegende()
            effect = j1.joue(jeu_j2)
            cls()
            print("\n ~~~===> JOUEUR 1\n")

            jeu_j2.affiche(humain=True, cacher=True)
            print()
            jeu_j1.affiche(humain=True)
            if effect > 0 :
                input("    Touché ! Vous pouvez rejouer !(appuyez sur entrer)\n")
            else :
                input("Manqué...(appuyez sur entrer)\n")
        if multi :
            cls()
            input("\n=-- Tour de J2 :"+j2.nom+" --=\n(appuyez sur entrer quand vous êtes prêt...)")
            effect = 1
            while effect > 0 and not (jeu_j2.victoire() or jeu_j1.victoire()) :
                cls()
                print("\n ~~~===> JOUEUR 2\n")
                jeu_j1.affiche(humain=True, cacher=True)
                print()
                jeu_j2.affiche(humain=True)
                dply.afficherLegende()
                effect = j2.joue(jeu_j1)
                cls()
                print("\n ~~~===> JOUEUR 2\n")

                jeu_j1.affiche(humain=True, cacher=True)
                print()
                jeu_j2.affiche(humain=True)
                if effect > 0 :
                    input("    Touché ! Vous pouvez rejouer ! (appuyez sur entrer)\n")
                else :
                    input("Manqué...(appuyez sur entrer)\n")

        else :
            input("Au tour de l'IA !\n(appuyez sur entrer quand vous êtes prêt...)")
            effect = 1
            while effect > 0 and not (jeu_j2.victoire() or jeu_j1.victoire()) :
                effect = j2.joue(jeu_j1)
                cls()
                print("\n ~~~===> IA\n")
                jeu_j2.affiche(humain=True, cacher=True)
                print()
                jeu_j1.affiche(humain=True)
                if effect > 0 :
                    input("    Touché ! L'IA rejoue ! (appuyez sur entrer)\n")
                else :
                    input("Manqué...(appuyez sur entrer)\n")
        input("Nouvelle manche ...(appuyez sur entrer)\n")

    cls()
    input("\n\\\\\\\\ Fin de la partie ! ////\n\n(" + str(cpt) + " manches) (appuyez sur entrer)")
    if jeu_j2.victoire() :
        if multi :
            print("Joueur J1 : "+j1.nom+" a gagné !")
        else :
            print("     !! Victoire contre l'IA : "+j2.nom+" !!")
    else :
        if multi :
            print("Joueur J2 : "+j2.nom+" a gagné !")
        else :
            print("\n..:: Défaite ! ::..")
    return cpt

def demo_jA() :
    partie(jr.JoueurAlea(), afficher=True, laps=0.25)

def demo_jH() :
    partie(jr.JoueurHeuristique(), afficher=True, laps=0.3)

def demo_jL() :
    partie(jr.JoueurLigne(), afficher=True, laps=0.3)

def demo_jP() :
    partie(jr.JoueurProba(), afficher=True, laps=0.25)

def vs_jA() :
    partieVs(jr.JoueurAlea())

def vs_jH() :
    partieVs(jr.JoueurHeuristique())

def vs_jL() :
    partieVs(jr.JoueurLigne())

def vs_jP() :
    partieVs(jr.JoueurProba())

def vs_j17() :
    partieVs(jr.Joueur17())

def vs_multi() :
    partieVs(jr.JoueurHumain(None))



def jouer() :
    func = "Undefined"

    switcher =  {
        "1": vs_jA,
        "2": vs_jH,
        "3": vs_jL,
        "4": vs_jP,
        "5": vs_multi,
        "17": vs_j17,
        "0": exit
    }
    cls()
    request = "Choisissez la difficulté :"

    print("\n-= Jouer à la bataille navale =-\n")

    while func == "Undefined" :
        print("~" * len(request))
        rep = input(
        request + "\n\
 1 - Facile\n\
 2 - Moyenne\n\
 3 - Difficile\n\
 4 - Très difficile\n\n\
 5 - Multijoueur\n\n\
 0 - Retour\n\
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




# def esperance(joueur) :
#     cpt = 0
#     coups = 0
#     for i in range(1000) :
#         cpt += 1
#         coups += partie(joueur, afficher=False)
#     return cpt, coups

def convertTime(sec) :
    """ Rend un nombre de seconde en format "xm ys" """
    string = ""
    if sec >= 60 :
        string += str(sec//60) + "m "
    string += str(sec%60) + "s"
    return string

def distrib(joueur) :
    """ Fait jouer une IA 'joueur' 1000 fois, stocke dans un tableau le nombre
    de victoires pour un nombre de tours.

    la fonction peut prendre du temps, donc une barre de progression a été
    ajoutée (1).
    """
    # Le tableau s'arrête à 100 tours puisqu'il est impossible de jouer plus de
    # 100 tours
    # Le tableau commence à 17 puisqu'il est impossible de gagner en moins de
    # 17 tours (17 cases bateaux oblige)
    coups = [0 for i in range(17, 101)]
    string = "\n["
    for i in range(1000) :
        if i%100 == 0 :
            cls()
            print(string + "#" * int(i/100) + " " * int(10 - i/100) + "] ") # (1)
            if i >= 1 :
                end_time = time.clock()
                print("Temps restant estimé : " +\
                str(convertTime(round((end_time - start_time) * int(10 - i/100)))))
            start_time = time.clock()

        # print(".", end="")
        end_time = 0

        coups[partie(joueur, afficher=False) - 17] += 1
        joueur.__init__()
    cls()
    return i+1, coups

def histo(liste, xBounds, yBounds) :
    """ Retourne une chaine de caractère représentant un histogramme d'une
    liste de valeurs.
    /!/ L'histogramme peut prendre beaucoup de place à l'écran
    Entrée :
    -- liste : list(alpha)
            Liste de valeurs
    -- xBounds : (int, int)
            Bornes inférieures et supérieures de l'axe x
    -- yBounds : (int, int)
            Bornes inférieures et supérieures de l'axe y
    """
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
    """ Calcule et affiche la distribution et l'espérance du nombre de victoire
    en fonction du nombre de coups d'un joueur (IA). """
    cpt, coups = distrib(joueur)
    esp = 0
    for i in range(17, 101) :
        esp += i * coups[i-17]
    esp = esp/cpt
    print("\nEspérance du nombre de tours avant victoire pour "+joueur.nom+" : " + str(esp))
    input("\n\nAppuyez sur entrer...")

    upperbound = max(coups)

    # print(histo(coups, (17, 100), (0, upperbound)))
    dply.affiche_tabl(
                    [
                    ["Tour"] + [i for i in range(17, 101)],
                    ["Nb de victoires"] + coups
                    ]
                    , invert=True)

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

def info_jA():
    cls()
    title = "\nINFO IA ALEATOIRE"
    print(title + "\n"+"-" * len(title))
    print(jr.JoueurAlea().__doc__)
def info_jH():
    cls()
    title = "\nINFO IA HEURISTIQUE"
    print(title + "\n"+"-" * len(title))
    print(jr.JoueurHeuristique().__doc__)
def info_jL():
    cls()
    title = "\nINFO IA LIGNE"
    print(title + "\n"+"-" * len(title))
    print(jr.JoueurLigne().__doc__)
def info_jP():
    cls()
    title = "\nINFO IA PROBABILISTE SIMPLIFIE"
    print(title + "\n"+"-" * len(title))
    print(jr.JoueurProba().__doc__)
def info_main():
    cls()
    title = "\nA propos de cette fonction ..."
    doc = """\nCe menu vous permet de tester toutes les fonctions implémentées via une interface
console :
    - Démonstration de l'IA aléatoire
    - //            // //   heuristique
    - //            // //   heuristique en ligne
    - //            // //   probabiliste simplifiée
    - Jouer au jeu, seul ou à plusieurs
    - Donner des statistiques sur l'IA aléatoire
    - //     //  //           //  //   heuristique
    - //     //  //           //  //   heuristique en ligne
    - //     //  //           //  //   probabiliste simplifiée
        """
    print(title + "\n"+"-" * len(title))

    print(doc)


def main() :
    """ Ce menu vous permet de tester toutes les fonctions implémentées via une interface
    console :
    - Démonstration de l'IA aléatoire
    - //            // //   heuristique
    - //            // //   heuristique en ligne
    - //            // //   probabiliste simplifiée
    - Jouer au jeu, seul ou à plusieurs
    - Donner des statistiques sur l'IA aléatoire
    - //     //  //           //  //   heuristique
    - //     //  //           //  //   heuristique en ligne
    - //     //  //           //  //   probabiliste simplifiée
    """

    func = "Undefined"

    switcher =  {
        "11": demo_jA,
        "21": demo_jH,
        "31": demo_jL,
        "41": demo_jP,
        "5": jouer,
        "12": stats_jA,
        "22": stats_jH,
        "32": stats_jL,
        "42": stats_jP,
        "13": info_jA,
        "23": info_jH,
        "33": info_jL,
        "43": info_jP,
        "6": info_main,
        "0": exit
    }
    cls()
    title = "\n\tMENU PRINCIPAL"
    request = "Choisissez une opération (tapez le nombre correspondant) :"

    input("\n-= Modélisation probabiliste du jeu de la bataille navale =-\n(Appuyez sur entrée)")
    cls()
    while func == "Undefined" :
        print(title)
        print("~" * len(request))
        rep = input(
        request + "\n\
 IA Aléatoire\n\
    11 - Démonstration\n\
    12 - Statistiques\n\
    13 - Info?\n\
 IA Heuristique\n\
    21 - Démonstration\n\
    22 - Statistiques\n\
    23 - Info?\n\
 IA Heuristique ligne\n\
    31 - Démonstration\n\
    32 - Statistiques\n\
    33 - Info?\n\
 IA Probabiliste simplifiée\n\
    41 - Démonstration\n\
    42 - Statistiques\n\
    43 - Info?\n\
 5 - Jouer\n\
 6 - Info\n\
\n\
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
