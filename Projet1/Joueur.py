from random import *

class JoueurAlea() :
    """Stratégie aléatoire"""
    def __init__(self) :
        self.nom = "Joueur Aléatoire"

    def joue(self, bataille) :
        x, y = randint(0, 9), randint(0, 9)
        effect = bataille.joue((x, y))
        while (effect == -1) :

            x, y = randint(0, 9), randint(0, 9)
            effect = bataille.joue((x, y))

class JoueurHeuristique() :
    """Stratégie heuristique"""
    def __init__(self) :
        self.nom = "Joueur heuristique"
        self.prochains_coups = []
        self.coups_reussis = []

    def joue(self, bataille) :

        effect = -1
        while effect == -1 :
            if len(self.prochains_coups) == 0 :
                x, y = randint(0, 9), randint(0, 9)
                effect = bataille.joue((x, y))
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
