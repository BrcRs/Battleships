# Bataille navale (*Battleships*)
Projet du cours Statistique et informatique (LU3IN005), Sorbonne Université, Paris.

## Introduction

L'étude probabilistique d'un objet donné représente un grand intérêt dans la prise
de décision. Connaître les probabilités d'apparition d'un évênement équivaut à avoir
une certaine connaissance des futurs possibles, ce qui nous permet d'agir en prévision
de ceux-ci. Le jeu de la bataille navale se prête bien à une étude probabiliste. Nous
disposons d'une grille de 10 × 10 cases sur laquelle sont positionnés 5 bateaux de
tailles respectives 5, 4, 3, 3 et 2. Chaque tour, il nous faut faire feu sur une case de la
grille, sans que l'on connaisse la position des bateaux. Comment la probabilistique
peut nous aider à gagner au jeu de la bataille navale en un nombre minimum de
coups ?

C'est ce que nous allons essayer de déterminer à travers ce projet. Le rapport final peut être trouvé dans

    /Projet1/Rapport5.pdf

## De quoi s'agit-il

Notre application python permet de jouer au jeu de la bataille navale en joueur contre joueur, mais aussi en joueur contre IA, dont la difficulté peut être ajustée.
L'IA adopter l'une des stratégies suivantes :
- jouer aléatoirement
- jouer avec l'intuition de toucher autour des cases victorieuses (heuristique)
- jouer en tenant compte des probabilités

## Comment l'utiliser

Lancez :

    python3 modelisation.py

pour pouvoir utiliser notre application de bataille navale. Une interface terminal permet de choisir les options de jeu, tout est expliqué.

> Note : Modifiez 'config.py' pour personnaliser votre expérience (pour désactiver les caractères spéciaux notamment).
