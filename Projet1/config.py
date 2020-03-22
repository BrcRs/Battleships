# x_ascii : boolean, vrai si les caractères de l'ascii étendu sont autorisés
x_ascii = True # A modifier au besoin

""" reference : dict(int : (str, int))
Structure qui pour un type de case associe un nom et une valeur : sa taille si
c'est un bateau.
"""
reference = {
    0 : ('vide', 0),
    1 : ('porte-avions', 5),
    2 : ('croiseur', 4),
    3 : ('contre-torpilleurs', 3),
    4 : ('sous-marin', 3),
    5 : ('torpilleur', 2),
    6 : ('tiré', -1),
    7 : ('touché', -2)
}


""" symbols : dict(str, char)
Associe un symbole à un type de case.
"""
symbols = {}
if x_ascii :
    symbols = {
        "miss" : "X",
        "hit" : "!",
        "boat" : "■",
        "corner_high_left" : "┌",
        "corner_high_right" : "┐",
        "corner_low_left" : "└",
        "corner_low_right" : "┘",
        "vertical_bar" : "│",
        "horizontal_bar" : "─"
    }
else :
    symbols = {
        "miss" : "X",
        "hit" : "!",
        "boat" : "O",
        "corner_high_left" : "+",
        "corner_high_right" : "+",
        "corner_low_left" : "+",
        "corner_low_right" : "+",
        "vertical_bar" : "|",
        "horizontal_bar" : "~"
    }
