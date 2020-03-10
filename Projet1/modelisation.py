import Joueur as jr
import Bataille as btl

import time

"""
Programmer une fonction qui joue aléatoirement au jeu : une grille aléatoire
est tirée, chaque coup du jeu est ensuite tiré aléatoirement (on pourra tout de
même éliminer les positions déjà jouées) jusqu’à ce que tous les bateaux soient
touchés. Votre fonction devra renvoyer le nombre de coups utilisés pour
terminer le jeu.
"""

# definition de la fonction :
def partie(joueur, afficher=False, laps=1) :
    # tirage aléatoire d'une grille
    jeu = btl.Bataille()
    cpt = 0

    if (afficher) :
        jeu.affiche()
        time.sleep(laps)
    # Tant que le joueur n'a pas gagné :
    while (not jeu.victoire()) :
        cpt += 1
        # Toucher une position selon la stratégie du joueur (hasard)
        joueur.joue(jeu)

        if (afficher) :
            jeu.affiche()
            time.sleep(laps)


    print("Victoire du joueur en " + str(cpt) + " tours")
    print("Stratégie : " + joueur.__doc__)
    return cpt


def main() :

    func = "Erreur"

    jA = jr.JoueurAlea()
    jH = jr.JoueurHeuristique()

    switcher =  {
        "1": jA,
        "2": jH,
        "0": exit
    }

    print("\n-= Modélisation probabiliste du jeu de la bataille navale =-\n")

    while func == "Erreur" :
        print("~" * len("Choisissez une stratégie de joueur (tapez le chiffre correspondant) :"))
        rep = input("Choisissez une stratégie de joueur (tapez le chiffre correspondant) :\n1 - Aléatoire\n2 - Heuristique\n3 - Probabiliste simplifiée\n0 - Quitter\n >>> ")

        func = switcher.get(rep, "Erreur")

        if (func == "Erreur") :
            print("Erreur : entrée invalide.")

    if int(rep) != 0 :
        print()
        # partie(func)
        partie(func, afficher=True, laps=0.01)

if __name__ == "__main__" :
    main()
