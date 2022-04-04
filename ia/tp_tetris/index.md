---
title: TP Tetris
layout: default
permalink: /ia/tp_tetris
---

# Une IA pour Tétris

L'objectif de ce travail est de développer une IA pour le jeu Tétris. Pour ce faire nous allons utiliser la méthode [Value Iteration](/ia/dice_example).

Le code est en python.

# Installation

* L'archive contenant le code de départ est [ici](TetrisIA.zip)
* Après l'avoir téléchargé et extraite, installez numpy:
```
pip install numpy
```

(testé sur python version 3.8.2)

# Prise en main

## Premier Test

Pour tester si tout est en place, lancez la commande suivante:
```
python tetris.py --test-policy --6x6
```
(on suppose que python désigne votre commande pour python3, cela peut être py.exe sous windows)

La sortie ressemblera à cela:
```
----------------------------------------
score: 0
----------------------------------------
                    
                    
                    
                    
|      |            
|      |       22   
|      |       2    
|      |       2    
|      |            
|------|            

Action: [ 180 deg to left | 0 units to right ]
[press enter (Ctrl+C to quit)]
````

C'est tetris en mode texte. Appuyez sur Entrée et vous verez l'IA en marche.

l'option *--6x6* indique que l'arene de jeu est de taille 6x6. Sont également disponibles 4x4 et 5x5 (très utilisés en cas d'explosion d'état ...)

## Evaluation de la strategy

Vous pouvez évalement lancer une évaluation de la stratégie avec la commande suivante:

```
python tetris.py --eval-policy
```

Le système lancera alors 1000 parties et calculera moyenne, écart-type et médiane du nombre de lignes obtenues par partie.

A titre de comparaison, vous pouvez également lancer l'évaluation de la stratégie purement aléatoire avec:
```
python tetris.py --eval-random-policy
``` 

# Value Iteration

voir ici pour avoir la présentation de l'algoritme: https://rhoban.github.io/ia/dice_example

Trouver une stratégie (une "policy") consiste à trouver une action pour toute configuration possible du jeu. C'est notre but.

Le jeu est compliqué, et le nombre d'états possibles (*i.e.* de configurations) est a priori trop important pour être traité.

C'est pourquoi, pour le traitement dans l'algorithme de Value Iteration, on considère une simplification de l'état qui consiste à ne pas prendre en compte tous les trous qu'il peut y avoir dans la construction, mais seulement la hauteur du trou le plus haut. Cela nous permet de diminuer le nombre d'état à considérer.

Ainsi pour nous, un état du jeu à un moment donné consistera en
- une ligne d'horizon, c'est-à-dire la crête de la construction.
- la hauteur du plus haut trou dans la construction
- la pièce à placer (il y en a 7 en tout)
(Notez bien qu'il s'agit d'une simplification de la véritable configuration du jeu, codée dans la classe *Game*)


Et les actions possibles consistent en
- une rotation d'angle 0, 90, 180 ou 270°
- une position latérale à laquelle on laisse tomber la pièce sur la construction. (voir la classe *Action* dans le fichier *kernel.py*)

Chaque action sera codée par un entier (voir les méthodes *idx_of_action* et *action_of_idx*).
De même les états seront également codés par des entiers (voir les méthodes *game_state_of_idx* et *idx_of_game_state*)

Donc, notre but est de produire une stratégie, c'est à dire un (grand) tableau associant à chaque indice d'état, l'indice de l'action à faire dans cet état. 

**Votre but est de produire la fonction *compute_value_and_policy*** dont le prototype est proposé dans le fichier *value_iteration.py*.
Cette fonction devra retourner un couple *V,policy* ou *V* est un tableau donnant la fonction de valeur (utilisée dans Value Iteration) pour chaque état, et *policy* est également un tableau donnant la stratégie (cf. https://rhoban.github.io/ia/dice_example).

Actuellement, vous disposez du fichier *data/value_and_policy_6_6.pickle* qui propose une stratégie. Le fichier est chargé automatiquement (inspectez le code de *test_policy* ou de *eval_policy*). Ce fichier a été produit par une version de l'algorithme dont vous ne disposez pas (il faut justement que vous écriviez la fonction *compute_value_and_policy*).

Vous pourrez vous appuyer sur la fonction
*compute_transition_matrix()*, disponible dans le fichier *value_iteration.py*. Cette fonction calcule 2 matrices. L'une pour les transitions (notée *transitions*), l'autre pour les score (notée *scores*). La matrice comporte en ligne les états (simplifiés) du jeu, et en colonne les actions (on parle des indices).
Pour tout état *s* et pour toute action *a*, *transitions[s,a]* contient l'indice d'un état *s'* produit à partir de l'état *s* avec l'action *a*. Remarquons que cet état contient lui même une pièce courante "à placer", c'est un élément aléatoire de cet état *s'*.
Par ailleurs, *scores[s,a]* contient le différentiel de score entre l'état *s* et l'état *s'*, c'est-à-dire le nombre de lignes produites par l'action *a* sur *s*.

Remarquons que le *s'* de la description de l'algorithme de https://rhoban.github.io/ia/dice_example parcourt tous les successeurs de *s*. On pourra l'obtenir en faisant varier la piece courante de *s'* (on utilise la fonction *modify_current_piece_in_idx(s, p)* du fichier *kernel.py*). Cela est illustré par les fonctions *compute_successors(transitions, s, a)* et *compute_successor_matrix(transitions)* dont vous disposez.

Enfin, vous aurez besoin de la fonction récompense *compute_reward_matrix(scores)* qu'il vous faudra construire. Sans surprise, elle sera basée sur les scores.