# Projet de développement du jeux Puissance 4

Ce projet est développé à titre éducatif. Il a plusieurs objectif :
  - enseigner les rudiments de la gestion de code avec git
  - apprendre les rudiments du travail en équipe
  - apprendre à structurer le code 
    - séparation par fonction (traitement, affichage)
    - organisation en objets
  - faire quelques tests unitaires


# Les objectifs du programme 
## Les règles du jeu "Puissance 4"
Le jeux "Puissance 4" se joue à 2 joueurs sur une grille verticale de 6 lignes et 7 colonnes. Chaque joueur dispose de jetons d'une couleur différente de l'adversaire (Jaune ou rouge). Chacun joue alternativement un pion, qui 'tombe en bas de la colone choisie. Le joueur gagnant est celui qui aligne le premier 4 pions de sa couleur. l'alignement peut être vertical, horizontal et diagonal.

cf https://fr.wikipedia.org/wiki/Puissance_4 pour plus de détails.

![alt](https://fr.wikipedia.org/wiki/Puissance_4#/media/Fichier:Puissance4_01.svg "Plateau de Puissance 4")

## Les spécifications générales du jeu
### Les modes de jeu
Le programme que l'on va developer doit permettre 
- à un joueur humain de jouer contre un autre joueur humain (sur le même ordinateur).
- à un joueur humain de jouer contre l'ordinateur.

### Les niveau de difficulté
Lorsque le joueur joue contre l'ordinateur, il doit pouvoir choisir le niveau de difficulté.

### Le type affichage
Le programme pourra supporter 2 modes d'affichage :
- un mode texte : le jeu s'affiche sur une console texte
- un mode graphique : je jeux s'affiche dans une fenêtre spécifique avec de jolis graphismes.