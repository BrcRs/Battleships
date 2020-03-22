import config as cfg
import naval as nvl
import matplotlib.pyplot as plt


def affiche(grille) :
    """ list(list(int)) * int  -> void
    Affiche la grille de jeu (utiliser imshow du module matplotlib.pyplot).
    """
    plt.grid(True)
    plt.imshow(grille)
    plt.show()

def affiche_mat(grille) :
    """ list(list(alpha)) -> str
    Renvoie une chaine de caractère représentant la matrice passée en paramètre.
    """
    string = ""
    for i in range(len(grille)) :
        for j in range(len(grille[0])) :
            if (grille[i][j] == 0) :
                string += " \t"

            else :
                string += str(grille[i][j]) + "\t"
        string += "\n"
    return string

def affiche_tabl(mat, invert=False, replace=("0", "0")) :
    """ Affiche d'une façon élégante une matrice d'éléments sous la forme d'un
    tableau.

    Entrée :
     --   mat : list(list(alpha))
     --  invert : boolean
            Si égal à True, les lignes deviennent colonnes et inversement.
     -- replace : (str, str)
            Pendant la construction du tableau, si un élément est égal à
            replace[0] après avoir été converti en str, est remplacé par
            replace[1].

    Sortie :
     -- : void
    """
    # matyCopy : list(list(alpha))
    matCopy = mat.copy()

    """ Processus d'inversion """
    if invert :
        matCopy2 = [[] for j in range(len(matCopy[0]))]
        for i in range(len(matCopy)) :
            for j in range(len(matCopy[i])) :
                matCopy2[j].append(matCopy[i][j])
        matCopy = matCopy2
    """                       """

    # sizes : list(int), liste des tailles des colonnes
    sizes = [0] * len(matCopy[0])

    """ Mise à jour des tailles optimales des colonnes """
    for i in range(len(matCopy)) :
        for j in range(len(matCopy[i])) :
            # sizes[j] prend pour valeur la longueur du plus long élément de la
            # colonne j
            sizes[j] = max(sizes[j], len(str(matCopy[i][j])))
    """                                                """

    """ Insertion d'une ligne de séparation (pour les intitulés de colonnes) """
    matCopy.insert(1, ["-" * (sizes[i]) for i in range(len(matCopy[0]))])

    # tab : str, résultat
    tab = cfg.symbols["corner_high_left"]

    for j in range(len(matCopy[i])) :
        tab += cfg.symbols["horizontal_bar"] * (sizes[j] + 2)

    tab += cfg.symbols["horizontal_bar"] * (len(matCopy[0]) - 1) +\
            cfg.symbols["corner_high_right"]+"\n"

    for i in range(len(matCopy)) :
        tab += cfg.symbols["vertical_bar"]

        for j in range(len(matCopy[i])) :
            tab += " "

            if str(matCopy[i][j]) == replace[0] :
                tab += replace[1] + " " * ((sizes[j]) - len(str(matCopy[i][j])))

            else :
                tab += str(matCopy[i][j]) + " " * ((sizes[j]) - len(str(matCopy[i][j])))
            tab += " " + cfg.symbols["vertical_bar"]
        tab += "\n"
    tab += cfg.symbols["corner_low_left"]

    for j in range(len(matCopy[i])) :
        tab += cfg.symbols["horizontal_bar"] * (sizes[j] + 2)

    tab += cfg.symbols["horizontal_bar"] * (len(matCopy[0]) - 1) +\
    cfg.symbols["corner_low_right"]

    print(tab)


def afficherLegende() :
    """ Affiche une légende des symboles utilisés."""
    print("    '"+cfg.symbols["hit"]+"' : bateau touché\n    '"+cfg.symbols["boat"]+"' : bateau\n    '"+cfg.symbols["miss"]+"' : coup raté\n")


def frame_bataille(mat, humain=False, cacher=False) :
    """ Retourne une chaine de caractère représentant un plateau de jeu de
    bataille navale, encadré.

    Entrée :
    --   mat : list(list(alpha))
    --  humain : boolean
            Si égal à True, ajoutera aux axes une graduation allant de A à J
            pour la verticale et de 1 à 10 pour l'horizontale
            (origine : haut gauche)
    --  cacher : boolean
            Si égal à True, cachera les cases bateaux, mais indiquera le nmbre
            de bateaux restants
    Sortie :
    -- res : str
    """
    # bats : set(), bateaux restants
    bats = set()

    # res : str, resultat
    res = ""

    """ Ajout de la graduation horizontale """
    if humain :
        res += "   "
        for i in range(10) :
            res += " " + str(i +1) + " "
        res += "\n  "

    """ Ajout de la bordure supérieure """
    res += cfg.symbols["corner_high_left"] + cfg.symbols["horizontal_bar"] * 3 * len(mat[0]) + cfg.symbols["corner_high_right"] +"\n"

    """ Ajout ligne par ligne """
    for i in range(len(mat)) :
        if humain :
            """ Ajout de la graduation verticale """
            res += chr(ord('A') + i) + " " + cfg.symbols["vertical_bar"]

        else :
            res += cfg.symbols["vertical_bar"]
        for j in range(len(mat[0])) :
            if mat[i][j] == 0 :
                res += "   "

            elif mat[i][j] == -1 :
                res += " "+cfg.symbols["miss"]+" "
            elif mat[i][j] == -2 :
                res += " "+cfg.symbols["hit"]+" "
            elif cacher :
                bats.add(mat[i][j])
                res += "   "
            else :
                res += " "+cfg.symbols["boat"]+" "
        res += cfg.symbols["vertical_bar"]+"\n"

    """ Ajout de la bordure inférieure """
    if humain :
        res += "  "+cfg.symbols["corner_low_left"] + cfg.symbols["horizontal_bar"] * 3 * len(mat[0]) + cfg.symbols["corner_low_right"] +"\n"
        if cacher :
            res += "Nombre de bateaux restants : " + str(len(bats))
    else :
        res += cfg.symbols["corner_low_left"] + cfg.symbols["horizontal_bar"] * 3 * len(mat[0]) + cfg.symbols["corner_low_right"] +"\n"

    return res

def main() :
    affiche(nvl.genere_grille())

if __name__ == "__main__" :
    main()
