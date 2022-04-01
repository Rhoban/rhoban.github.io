---
title: IA
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

# Test

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
