import naval as nvl

def eq(grilleA,grilleB) :
    """ list(list(int)) * list(list(int)) -> bool
    Teste l’égalité entre deux grilles
    """
    for i in range (len(grilleA)):
        for j in range (len(grilleA[0])):
            if grilleA[i][j] != grilleB[i][j]:
                return False
    return True

def copyMat(grille) :
    """ list(list(int)) -> list(list(int))
    Renvoie la copie de grille
    """
    nouvGrille = nvl.genere_grille_vide()
    for i in range(len(grille)) :
        for j in range(len(grille[0])) :
            nouvGrille[i][j] = grille[i][j]
    return nouvGrille

def maxLen(liste) :
    """ Etant donnée une liste de listes, renvoie la longueur de la liste
    contenue la plus longue.
    """
    maxi = 0
    for x in liste :
        maxi = max(len(x), maxi)
    return maxi
