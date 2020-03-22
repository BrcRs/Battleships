import naval as nvl
import config
import display as dply
import Joueur

class Bataille :

    def __init__(self) :
        self.grille = nvl.genere_grille()

        nbvies = 0
        for i in range(1, 6) :
            nbvies += config.reference[i][1]
        # self.vies : int, nombre de cases bateaux restantes
        self.vies = nbvies

    def joue(self, position) :
        """ Etant donnée une position, joue cette position et renvoie la valeur
        de la case en celle-ci. Màj la case visée si le coup est valide.
        """
        if not self.checkBound(position) :
            return -1
        x, y = position
        cible = self.grille[x][y]

        if cible == 0 :
            self.grille[x][y] = -1
        elif cible > -1 :
            self.vies -= 1
            self.grille[x][y] = -2

        return cible


    def victoire(self) :
        return self.vies == 0

    def affiche(self, humain=False, cacher=False) :
        """ Affiche l'état de la grille
        Entrée :
        -- humain : boolean
                Si True, ajoute une graduation à l'affichage de la grille
        -- cacher : boolean
                Si True, affiche les cases bateaux comme des cases vides
                    Autrement dit, n'affiche pas les cases bateaux.
                    (pratique pour jouer en versus0)
        """
        print(dply.frame_bataille(self.grille, humain, cacher))


    def checkBound(self, position) :
        """ Renvoie vraie si la position est à l'intérieur de la grille """
        x, y = position
        return x < len(self.grille) and x >= 0 and y < len(self.grille[0]) and y >= 0

    def get(self, position) :
        x, y = position
        return self.grille[x][y]

    # def reset(self) :
