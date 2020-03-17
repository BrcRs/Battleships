import Joueur as jr
import Bataille as btl
import naval as nvl

import time

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def partie(joueur, afficher=False, laps=1, clear=True, humain=False) :
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
            nvl.afficherLegende()
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
                nvl.afficherLegende()
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




# def esperance(joueur) :
#     cpt = 0
#     coups = 0
#     for i in range(1000) :
#         cpt += 1
#         coups += partie(joueur, afficher=False)
#     return cpt, coups

def convertTime(sec) :
    string = ""
    if sec >= 60 :
        string += str(sec//60) + "m "
    string += str(sec%60) + "s"
    return string

def distrib(joueur) :

    coups = [0 for i in range(17, 101)]
    string = "\n["
    for i in range(1000) :
        if i%100 == 0 :
            cls()
            print(string + "#" * int(i/100) + " " * int(10 - i/100) + "] ")
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



def main() :

    func = "Undefined"

    switcher =  {
        "1": demo_jA,
        "2": demo_jH,
        "3": demo_jL,
        "4": demo_jP,
        "5": jouer,
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
 5 - Jouer\n\
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
