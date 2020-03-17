from random import *

import naval as nvl

import time

import string

class JoueurAlea() :
    """Stratégie aléatoire"""
    def __init__(self) :
        self.nom = "IA Aléatoire"

    def joue(self, bataille) :
        x, y = randint(0, 9), randint(0, 9)
        effect = bataille.joue((x, y))
        while (effect <= -1) :

            x, y = randint(0, 9), randint(0, 9)
            effect = bataille.joue((x, y))
        return effect

    def joueContre(self, position, bataille) :
        return bataille.joue(position)

class JoueurHeuristique() :
    """Stratégie heuristique"""
    def __init__(self) :
        self.nom = "IA heuristique"
        self.prochains_coups = []
        self.coups_reussis = []

    def joue(self, bataille) :

        effect = -1
        while effect <= -1 :
            if len(self.prochains_coups) == 0 :
                x, y = randint(0, 9), randint(0, 9)
            else :
                x, y = self.prochains_coups.pop()
            effect = bataille.joue((x, y))


        if effect != 0 :
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
        # print(self.coups_reussis)
        # print(self.prochains_coups)
        return effect
    def joueContre(self, position, bataille) :
        return bataille.joue(position)

class JoueurLigne() :
    """Stratégie en ligne"""
    def __init__(self) :
        self.nom = "IA de ligne"
        self.prochains_coups = []
        self.coups_reussis = []
        self.coups_defaut =\
        [(i, j) for i in range(0, 10, 2) for j in range(0, 10, 2) ] +\
        [(i, j) for i in range(1, 10, 2) for j in range(1, 10, 2)] +\
        [(i, j) for i in range(0, 10, 2) for j in range(1, 10, 2)] +\
        [(i, j) for i in range(1, 10, 2) for j in range(0, 10, 2)]

        # self.coups_defaut =\
        # [(i, j) for i in range(0, 10) for j in range(0, 10)] +\
        # [(i, i+4) for i in range(0, 10)] +\
        # [(i, i-4) for i in range(0, 10)] +\
        # [(i, 4 - i) for i in range(9, -1, -1)] +\
        # [(i, 4 + i) for i in range(9, -1, -1)] +\
        # [(i, 9 - i) for i in range(9, -1, -1)] +\
        # [(i, i) for i in range(0, 10)]

    def joue(self, bataille) :

        effect = -1
        while effect <= -1 :
            if len(self.prochains_coups) == 0 :
                x, y = self.coups_defaut.pop()
            else :
                x, y = self.prochains_coups.pop()
            effect = bataille.joue((x, y))


        if effect != 0 :
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
        return bataille.joue(position)

class JoueurProba() :
    """
    À chaque tour, pour chaque bateau restant, on calcule la probabilité pour
    chaque case de contenir ce bateau sans tenir compte de la position des
    autres bateaux. Pour cela, en examinant toutes les positions possibles du
    bateau sur la grille, pour chaque case on obtient le nombre de fois où le
    bateau apparaît potentiellement. On dérive ainsi la probabilité jointe de
    la présence d’un bateau sur une case (en considérant que la position des
    bateaux est indépendante). Donner une petite formalisation de ce texte.
    Pourquoi l’hypothèse d’indépendance est fausse ? Proposer une
    implémentation intelligente de cette stratégie. Comparer vos résultats.
    """
    """Stratégie Probabiliste"""
    def __init__(self) :
        self.nom = "IA Probabiliste"
        self.restants = [
        (5, nvl.reference[5][1]),
        (4, nvl.reference[4][1]),
        (3, nvl.reference[3][1]),
        (2, nvl.reference[2][1]),
        (1, nvl.reference[1][1]),
                        ]
        self.probas = nvl.genere_grille_vide()

    def joue(self, bataille) :
        self.probas = nvl.genere_grille_vide()

        effect = -1
        while (effect <= -1) :
            # Pour chaque bateau restant
            """ Calculer la probabilité pour chaque case de contenir ce
            bateau sans tenir compte de la position des autres bateaux.
            """
            for b in self.restants :
                if b[1] == 0 :
                    continue
                for i in range(10) :
                    for j in range(10) :

                        if bataille.get((i,j)) == -1 :
                            self.probas[i][j] = 0
                        else :
                            t = 0
                            bonus = 0
                            if bataille.get((i,j)) == -2 :
                                bonus = 1

                                self.probas[i][j] = 0
                            """Vertical"""
                            peut_poser = True
                            for u in range(1, nvl.reference[b[0]][1]) :
                                if not bataille.checkBound((i+u,j)) or bataille.get((i+u, j)) == -1 :
                                    peut_poser = False
                                    break
                                if bataille.get((i+u, j)) == -2 :
                                    bonus += 1
                            if peut_poser :
                                for u in range(t, nvl.reference[b[0]][1]) :
                                    if bataille.get((i+u, j)) != -2 :
                                        self.probas[i+u][j] += 1 + bonus * 2

                            """Horizontal"""
                            peut_poser = True
                            for v in range(1, nvl.reference[b[0]][1]) :
                                if not bataille.checkBound((i,j+v)) or bataille.get((i, j+v)) == -1 :
                                    peut_poser = False
                                    break
                                if bataille.get((i, j+v)) == -2 :
                                    bonus += 1
                            if peut_poser :
                                for v in range(t, nvl.reference[b[0]][1]) :
                                    if bataille.get((i, j+v)) != -2 :
                                        self.probas[i][j+v] += 1 + bonus * 2



            """Choisir une position dans probas"""
            flatProbas = [item for sublist in self.probas for item in sublist]
            maxiProba = max(flatProbas)
            x = flatProbas.index(maxiProba)//10
            y = (flatProbas.index(maxiProba)+10)%10
            effect = bataille.joue((x, y))
        """"""
        # print([h[0] for h in self.restants if h[1] != 0])
        # nvl.affiche_tabl([[i for i in range(10)]] + self.probas, replace=("0", " "))
        # time.sleep(4)
        """"""
        if effect != 0 :
            # print(effect)
            for i in range(len(self.restants)) :
                if self.restants[i][0] == effect :
                    self.restants[i] = (self.restants[i][0], self.restants[i][1] - 1)

            # self.coups_reussis.append((x, y))
        # while self.curr < len(self.restants) and (self.restants[self.curr][1] == 0) :
        #     self.curr += 1
        return effect
    def joueContre(self, position, bataille) :
        return bataille.joue(position)

class JoueurHumain() :
    """A vous de jouer !"""
    def __init__(self, adv) :
        self.nom = "\"Encore un humain\""
        self.adversaire = adv

    # def __init__(self) :
    #     self.nom = "\"Encore un humain\""
    #     self.adversaire = None

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
