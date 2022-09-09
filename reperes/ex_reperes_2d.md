---
title: "TP Porte"
layout: default
permalink: /reperes/tp_door
---

# Présentation

Un robot à deux roues veut entrer dans une maison. Pour cela, on a placé deux balises sur les murs (les points $$A$$
et $$B$$). On suppose que l'on connaît la position de ces balises dans le monde $$\{w\}$$, et que le robot les repère
à dans son propre repère $$\{r\}$$ à l'aide de capteurs.

<div class="text-center">
    <img src="/assets/imgs/house.svg" width="400" />
</div>

On sait que le centre d'une porte $$P$$ se trouve à une distance de 2m le long du mur entre les balises $$A$$
et $$B$$. L'objectif est que le robot atteigne une position cible $$X$$.

Pour ce faire, on propose de paser par un point de dégagement $$P_{ext}$$, puis de franchir la porte, et enfin
de se rendre vers la cible $$X$$.

# TP

## Prise en main

<div class="alert alert-info d-flex align-items-center justify-content-center">
    <img src="/quadruped/img/zip.png" />

    <div>
        <big><a href="/reperes/tp_door.zip">Téléchargez l'archive tp_door.zip</a></big>
        <br/>
        <em>Lisez les instructions ci-dessous</em>
    </div>
</div>

Téléchargez l'archive et exécutez `sim.py`, vous devriez voir une scène similaire à l'image ci-dessous.
Si vous appuyez sur *ESPACE*, la scène devrait se re-générer aléatoirement:

<div class="text-center">
    <img src="/assets/imgs/tp_door.png" width="400" />
</div>

Dans le code, vous éditerez le fichier `behavior.py` (**et uniquement celui-ci**). La fonction `robot_tick`
de ce dernier est appellée par le simulateur, en lui fournissant les coordonnées de $$A$$ et $$B$$ dans le monde.
Cette fonction retourne alors la vitesse linéaire (*m/s*) et de rotation (*rad/s*) pour le robot.

Essayez de changer la ligne:

```python
# Dans behavior.py
return 0, 0
```

En:

```python
return 1, 0 # 1 m/s, 0 rad/s
```

Ou:
```python
return 0, 1 # 0 m/s, 1 rad/s
```

Et observez l'effet dans le code.

<div class="alert alert-info">
    Indication: le fichier <kbd>utils.py</kbd> contient le code fournit dans la partie
    <a href="/reperes/python2d">implémentation Python</a> des repères 2D.
</div>

## Naviguer

Avant de nous occuper de la porte, nous allons commencer par programmer la fonction de navigation. Pour l'instant,
changez `robot_tick` afin qu'elle retourne:

```python
return navigate_to(A_robot)
```

Et implémentez le code de `navigate_to` afin de produire des vitesses permettant de se rendre vers le point passé
en paramètre dans le repère du robot. Si la cible n'est pas alignée, le robot tournera sur lui-même, sinon il ira
tout droit. 

Si tout se passe bien, le robot devrait alors se diriger vers le point $$A$$.

## Repérer le robot (et X) dans le monde

Implémentez la fonction `T_frame_wall`, qui prend en paramètre la position de $$A$$ et de $$B$$ dans un repère,
et qui utilise ces points pour construire la matrice de transformation permettant de passer du repère mur au
repère dans lequel $$A$$ et $$B$$ ont été repéré.

Calculez alors `T_world_wall` et `T_robot_wall` dans `robot_tick`.

Vous pouvez désormais calculer la position de $$X$$, $$P_{in}$$ et $$P_{ext}$$ dans le repère robot.

## Passer la porte!

Implémentez le code permettant au robot de:

* Passer par $$P_{ext}$$,
* Passer par $$P_{in}$$,
* Aller en $$X$$.

Afin de franchir la porte.

Vous pourrez vous aider de la variable d'état global `STATE`, afin de savoir à quelle "étape" vous en êtes.

