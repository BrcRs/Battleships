from random import *

import naval as nvl
import config

import time
import string

class JoueurAlea() :
    """Stratégie aléatoire
    Joue à la bataille navale aléatoirement.
    """
    def __init__(self) :
        self.nom = "IA Aléatoire"

    def joue(self, bataille) :
        """ Tire une position aléatoire dans 'bataille' """
        x, y = randint(0, 9), randint(0, 9)

        # effect : int
        effect = bataille.joue((x, y))
        # effect est <= -1 quand la case visée a déjà été jouée
        while (effect <= -1) :

            x, y = randint(0, 9), randint(0, 9)
            effect = bataille.joue((x, y))
        return effect

    def joueContre(self, position, bataille) :
        """ Avec cette méthode, la position de tir est déterminée
        Fonction utilisée en mode joueur contre IA et joueur contre joueur"""
        return bataille.joue(position)

class JoueurHeuristique() :
    """Stratégie heuristique
    Joue aléatoirement dans un premier temps, puis cherche à toucher les cases
    adjacentes si un bateau est touché. """

    def __init__(self) :
        self.nom = "IA heuristique"
        self.prochains_coups = []
        self.coups_reussis = []

    def joue(self, bataille) :
        """ Tire une position dans 'bataille' d'après sa stratégie """
        effect = -1

        # effect est <= -1 quand la case visée a déjà été jouée
        while effect <= -1 :
            # Si aucun prochain coup stocké :
            if len(self.prochains_coups) == 0 :
                # Le tir est donné aléatoirement
                x, y = randint(0, 9), randint(0, 9)
            else :
                # Le premier prochain coup est tiré, et retiré de la liste
                x, y = self.prochains_coups.pop()

            effect = bataille.joue((x, y))

        if effect != 0 :
            # Dans ce cas la case visée contient un chiffre, ce qui correspond
            # à un bateau.
            self.coups_reussis.append((x, y))
            # Ajouter les cases adjacentes aux prochains coups
            cpt = 0
            for x_, y_ in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
                if (x + x_, y + y_) in self.coups_reussis :
                    cpt += 1
                    self.prochains_coups.append((x + x_ * -1, y + y_ * -1))
            # Si on ne peut pas déduire la direction du bateau touché :
            # Autrement dit aucune case adjacente n'était victorieuse :
            if cpt == 0 :
                # Toutes les cases adjacentes sont stockées comme 'à jouer'
                self.prochains_coups.append((x, y+1))
                self.prochains_coups.append((x+1, y))
                self.prochains_coups.append((x-1, y))
                self.prochains_coups.append((x, y-1))
        return effect

    def joueContre(self, position, bataille) :
        """ Avec cette méthode, la position de tir est déterminée.
        Fonction utilisée en mode joueur contre IA et joueur contre joueur"""
        return bataille.joue(position)

class JoueurLigne() :
    """Stratégie en ligne (nom améliorable)
    Stratégie heuristique non-proposée dans l'énoncé, à l'intérêt nuancé.

    Le comportement est le même que Heuristique, mais au lieu de jouer
    aléatoirement dans un premier temps, l'IA joue un motif de cases
    particulier pour maximiser les chances de toucher un bateau, motif que l'on
    remarque plus ou moins dans la version probabiliste simplifiée.

    Il s'agit de jouer une case sur 2, en formant un damier sur la grille.
    Cette stratégie exploite le fait qu'un bateau étant forcément de taille
    supérieure à 1, tester deux cases adjacentes est inefficace."""
    def __init__(self) :
        self.nom = "IA de ligne"
        self.prochains_coups = []
        self.coups_reussis = []
        """Le damier est 'hard-codé' car constant : """
        self.coups_defaut =\
        [(i, j) for i in range(0, 10, 2) for j in range(0, 10, 2) ] +\
        [(i, j) for i in range(1, 10, 2) for j in range(1, 10, 2)] +\
        [(i, j) for i in range(0, 10, 2) for j in range(1, 10, 2)] +\
        [(i, j) for i in range(1, 10, 2) for j in range(0, 10, 2)]

        #""" Un autre motif, moins efficace : """
        # self.coups_defaut =\
        # [(i, j) for i in range(0, 10) for j in range(0, 10)] +\
        # [(i, i+4) for i in range(0, 10)] +\
        # [(i, i-4) for i in range(0, 10)] +\
        # [(i, 4 - i) for i in range(9, -1, -1)] +\
        # [(i, 4 + i) for i in range(9, -1, -1)] +\
        # [(i, 9 - i) for i in range(9, -1, -1)] +\
        # [(i, i) for i in range(0, 10)]

    def joue(self, bataille) :
        """ Tire une position dans 'bataille' d'après sa stratégie """
        effect = -1
        # effect est <= -1 quand la case visée a déjà été jouée
        while effect <= -1 :
            if len(self.prochains_coups) == 0 :
                x, y = self.coups_defaut.pop()
            else :
                x, y = self.prochains_coups.pop()
            effect = bataille.joue((x, y))


        if effect != 0 :
            # Dans ce cas la case visée contient un chiffre, ce qui correspond
            # à un bateau.
            self.coups_reussis.append((x, y))
            # Ajouter les cases adjacentes aux prochains coups
            cpt = 0
            for x_, y_ in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
                if (x + x_, y + y_) in self.coups_reussis :
                    cpt += 1
                    self.prochains_coups.append((x + x_ * -1, y + y_ * -1))
            if cpt == 0 :
                self.prochains_coups.append((x, y+1))
                self.prochains_coups.append((x+1, y))
                self.prochains_coups.append((x-1, y))
                self.prochains_coups.append((x, y-1))
        return effect

    def joueContre(self, position, bataille) :
        """ Avec cette méthode, la position de tir est déterminée.
        Fonction utilisée en mode joueur contre IA et joueur contre joueur"""
        return bataille.joue(position)

class JoueurProba() :
    """ Joueur à stratégie probabiliste simplifiée
    À chaque tour, pour chaque bateau restant, on calcule la probabilité pour
    chaque case de contenir ce bateau sans tenir compte de la position des
    autres bateaux. Pour cela, en examinant toutes les positions possibles du
    bateau sur la grille, pour chaque case on obtient le nombre de fois où le
    bateau apparaît potentiellement. On dérive ainsi la probabilité jointe de
    la présence d’un bateau sur une case (en considérant que la position des
    bateaux est indépendante).
    """
    def __init__(self) :
        self.nom = "IA Probabiliste simplifiée"
        # self.restants : list((int, int)), tient à jour les bateaux restants
        # /!\ Notez que la stratégie n'exploitera pas la connaissance du nombre
        # de cases restantes pour chaque bateau (ce serait de la triche) bien
        # qu'on la stocke ici par soucis d'implémentation
        self.restants = [
        (5, config.reference[5][1]),
        (4, config.reference[4][1]),
        (3, config.reference[3][1]),
        (2, config.reference[2][1]),
        (1, config.reference[1][1]),
                        ]
        # self.probas : list(list(int)), une grille initialisée à 0, contiendra
        # les probabilités cumulées de la position possible des bateaux
        self.probas = nvl.genere_grille_vide()

    def joue(self, bataille) :
        # self.probas : list(list(int)), est ré-initialisée à chaque tour
        self.probas = nvl.genere_grille_vide()

        # t : int, décalage (voir plus loin)
        t = 0
        # bonus : int
        bonus = 0
        # peut_poser : boolean
        peut_poser = False

        effect = -1
        # effect est <= -1 quand la case visée a déjà été jouée
        while (effect <= -1) :
            """ Calculer la probabilité pour chaque case de contenir ce
            bateau sans tenir compte de la position des autres bateaux.
            """
            # Pour chaque bateau restant :
            for b in self.restants :
                # Si le bateau est coulé (taille à 0) :
                if b[1] == 0 :
                    # On ne calcule plus sa probabilité
                    continue
                # Pour chaque case de 0 à 99 :
                for i in range(10) :
                    for j in range(10) :
                        # Si la case à été jouée et n'était pas un bateau :
                        if bataille.get((i,j)) == -1 :
                            # Pas de bateau ici
                            self.probas[i][j] = 0
                        else :
                            t = 0
                            bonus = 0
                            # Si la case était un bateau et a été jouée
                            if bataille.get((i,j)) == -2 :
                                # Les probabilités seront "boostées"
                                bonus = 1
                                # En revanche, impossible de toucher un bateau
                                # ici (case déjà jouée)
                                self.probas[i][j] = 0
                                # La case aura toujours une probabilité égale à
                                # 0 si elle a déjà été jouée, donc lors de
                                # l'attribution des probabilités aux cases que
                                # le bateau pourrait couvrir, on ignore la case
                                # d'origine
                                t = 1

                            """Peut-on poser 'b' verticalement ?"""
                            peut_poser = True
                            # Parcours des cases direction sud :
                            for u in range(1, config.reference[b[0]][1]) :
                                # Si la case explorée est hors-limite ou
                                # qu'elle a été jouée et n'a pas touché de
                                # bateau :
                                if not bataille.checkBound((i+u,j)) or bataille.get((i+u, j)) == -1 :
                                    peut_poser = False
                                    break
                                # Si la case explorée est un bateau touché, les
                                # chances qu'une autre case bateau se trouve
                                # proche sont plus grandes :
                                if bataille.get((i+u, j)) == -2 :
                                    # On booste les probabilités des cases
                                    # explorées
                                    bonus += 1
                            """ Attribution des probabilités """
                            if peut_poser :
                                # on peut attribuer leurs probabilités aux
                                # cases que le bateau pourrait couvrir sur sa
                                # longueur (avec un bonus significatif) :
                                for u in range(t, config.reference[b[0]][1]) :
                                    if bataille.get((i+u, j)) != -2 :
                                        self.probas[i+u][j] += 1 + bonus * 2

                            """Peut-on poser 'b' horizontalement ?"""
                            peut_poser = True
                            for v in range(1, config.reference[b[0]][1]) :
                                # Si la case explorée est hors-limite ou
                                # qu'elle a été jouée et n'a pas touché de
                                # bateau :
                                if not bataille.checkBound((i,j+v)) or bataille.get((i, j+v)) == -1 :
                                    peut_poser = False
                                    break
                                # Si la case explorée est un bateau touché, les
                                # chances qu'une autre case bateau se trouve
                                # proche sont plus grandes :
                                if bataille.get((i, j+v)) == -2 :
                                    bonus += 1
                            """ Attribution des probabilités """
                            if peut_poser :
                                # on peut attribuer leurs probabilités aux
                                # cases que le bateau pourrait couvrir sur sa
                                # longueur (avec un bonus significatif) :
                                for v in range(t, config.reference[b[0]][1]) :
                                    if bataille.get((i, j+v)) != -2 :
                                        self.probas[i][j+v] += 1 + bonus * 2



            """Choisir une position dans probas"""
            # C'est le moment où après avoir calculé une grille de
            # probabilités on choisit la case ayant la plus forte probabilité
            # de contenir un bateau
            flatProbas = [item for sublist in self.probas for item in sublist]
            maxiProba = max(flatProbas)
            x = flatProbas.index(maxiProba)//10
            y = (flatProbas.index(maxiProba)+10)%10
            effect = bataille.joue((x, y))

        # Sortie de boucle while effect <= -1
        """ A décommenter pour pouvoir observer l'évolution de la grille de
        probabilité pendant la démo : """
        # print([h[0] for h in self.restants if h[1] != 0])
        # nvl.affiche_tabl([[i for i in range(10)]] + self.probas, replace=("0", " "))
        # time.sleep(4)
        """Fin décommenter"""

        """Màj des bateaux restants en cas de tir réussi"""
        if effect != 0 :
            for i in range(len(self.restants)) :
                if self.restants[i][0] == effect :
                    self.restants[i] = (self.restants[i][0], self.restants[i][1] - 1)

        return effect
    def joueContre(self, position, bataille) :
        """ Avec cette méthode, la position de tir est déterminée.
        Fonction utilisée en mode joueur contre IA et joueur contre joueur"""
        return bataille.joue(position)

class JoueurHumain() :
    """A vous de jouer !"""
    def __init__(self, adv=None) :
        self.nom = "\"Encore un humain\""
        self.adversaire = adv

    def setAdversaire(self, adv) :
        self.adversaire = adv

    def joue(self, bataille) :
        first_round = True
        effect = -1
        while (effect <= -1) :
            if not first_round :
                print("Saisie incorrecte")
            else :
                first_round = False
            ans = input("Entrez une coordonnée du type A5\n>>> ")
            ans = ans.upper()
            if not (len(ans) >= 2 and ans[0] in string.ascii_uppercase and ans[1] in string.digits) or (len(ans) > 2 and ans[2] not in string.digits) :
                effect = -1
                continue

            x, y =  ord(ans[0]) - ord('A'), int(ans[1:]) - 1
            print(str((x,y)))
            effect = self.adversaire.joueContre((x, y), bataille)
        return effect

    def getEnnemi(self) :
        return self.adversaire

    def joueContre(self, position, bataille) :
        return bataille.joue(position)

class Joueur17() :
    """Stratégie imbattable

    """
    def __init__(self) :
        self.nom = "IA Imbattable"

    def joue(self, bataille) :
        """ Tire une position exacte dans 'bataille' """
        for x in range(10) :
            for y in range(10) :
                if bataille.get((x, y)) > 0 :
                    return bataille.joue((x, y))
        return -1

    def joueContre(self, position, bataille) :
        """ Avec cette méthode, la position de tir est déterminée
        Fonction utilisée en mode joueur contre IA et joueur contre joueur"""
        return bataille.joue(position)
