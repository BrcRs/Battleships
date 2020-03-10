import naval as nvl
import Joueur

class Bataille :

    def __init__(self) :
        self.grille = nvl.genere_grille()
        nbvies = 0
        for i in range(1, 6) :
            nbvies += nvl.reference[i][1]
        self.vies = nbvies

    def joue(self, position) :
        """ Etant donnée une position, joue cette position et renvoie la valeur
        de la case en celle-ci.
        """
        if not self.checkBound(position) :
            return -1
        x, y = position
        cible = self.grille[x][y]

        if cible == 0 :
            self.grille[x][y] = -1
        elif cible != -1 :
            self.vies -= 1
            self.grille[x][y] = -1

        return cible


    def victoire(self) :
        return self.vies == 0

    def affiche(self) :
        print(nvl.frame_bataille(self.grille))

    def checkBound(self, position) :
        x, y = position
        return x < len(self.grille) and x >= 0 and y < len(self.grille[0]) and y >= 0

    # def reset(self) :
