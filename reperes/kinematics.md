---
title: Modèle direct de robots articulaires
layout: default
permalink: /reperes/kinematics
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

Dans cette partie, nous allons montrer comment nous pouvons utiliser les changements de repères et
les matrices de transformation vues précédemment pour modéliser un robot articulaire.

# Présentation du robot RRR

Le robot auquel on s'intéresse est une patte a trois degrés de libertés rotatifs (pensez par exemple
à des servomoteurs):

<div class="text-center">
    <img src="/assets/imgs/rrr.svg" width="500" />
</div>

* Les angles $$(\alpha, \beta, \gamma)$$ sont les valeurs contrôlées directement par l'asservissement des
moteurs du robot, c'est **l'espace articulaire**
* La position du bout de la patte $$(x, y, z)$$ est celle qu'on aimerait contrôler dans la pratique, c'est
**l'espace opérationnel**

L'objectif de cette partie est de déterminer $$(x, y, z)$$ en connaissant $$(\alpha, \beta, \gamma)$$, nous
allons voir que ce problème peut être résolu en utilisant des changements de repères.

# Transformations élémentaires

On rappelle que les transformations élémentaires sont:

## Translation

$$
\tau (x,y,z) = 
\begin{bmatrix}
1 & 0 & 0 & x \\
0 & 1 & 0 & y \\
0 & 0 & 1 & z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

## Rotation autour de l'axe x

$$
R_x (\alpha) = 
\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & cos(\alpha) & -sin(\alpha) & 0 \\
0 & sin(\alpha) & cos(\alpha) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

## Rotation autour de l'axe y

$$
R_y (\alpha) = 
\begin{bmatrix}
cos(\alpha) & 0 & sin(\alpha) & 0\\
0 & 1 & 0 & 0 \\
-sin(\alpha) & 0 & cos(\alpha) & 0\\
0 & 0 & 0 & 1
\end{bmatrix}
$$


## Rotation autour de l'axe z

$$
R_z (\alpha) = 
\begin{bmatrix}
cos(\alpha) & -sin(\alpha) & 0 & 0 \\
sin(\alpha) & cos(\alpha) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

# Étapes

Supposons que, lorsque les trois angles valent $$0$$, la patte soit dans la configuration suivante:

<div class="text-center">
    <img src="/assets/imgs/leg.svg" width="500" />
</div>

Ici, on introduit également un repère sur le tronc ($$\{ r_1 \}$$), un repère par degré de liberté
($$\{ r_2 \}$$, $$\{ r_3 \}$$, $$\{ r_4 \}$$) et un repère final au bout de la patte $$\{ r_5 \}$$.

Les repères des articulations ($$\{ r_2 \}$$, $$\{ r_3 \}$$, $$\{ r_4 \}$$) sont positionnées sur
l'articulation **avant** qu'elle ait pivoté.

On appellera ($$\{ r_2' \}$$, $$\{ r_3' \}$$, $$\{ r_4' \}$$) les mêmes repères, mais positionnées
sur l'articulation **après** qu'elle ait pivoté.

On cherche alors à déterminer:

$$
T_{_r1 r_5} (\alpha, \beta, \gamma)
$$

La matrice de transformation (homogène 4x4) permettant de passer du repère du bout de la patte (de l'effecteur
du robot) au repère du tronc du robot.

(Par la suite, on omettra $$\alpha, \beta, \gamma$$ par simplicité d'écriture)

## Méthode

On peut découper ce problème en partant de la fin, et en se demandant qu'est-ce que:

$$
T_{r_4' r_5} 
$$

Cette transformation est uniquement une translation (on rappelle que $$\{ r_4' \}$$ est le repère positionné sur
l'articulation après qu'elle ait tourné) de $$L_4$$:

$$
T_{r_4' r_5}  = \tau(L_4, 0, 0)
$$

On peut alors chercher:

$$
T_{r_4 r_4'} 
$$

Ici, il s'agit uniquement de passer d'une articulation **après** qu'elle ait pivoté à une articulation **avant**
qu'elle ait pivoté. L'articulation de $$\{ r_4 \}$$ pivotant autour de l'axe $$y$$ d'un angle $$\gamma$$, on peut
donc écrire:

$$
T_{r_4 r_4'} = R_y(\gamma)
$$

Grâce à la règle d'annulation du subscript, on a donc:

$$
T_{r_4 \color{red}{r_4'}} T_{\color{red}{r_4'} r_5} = T_{r_4 r_5}
$$

Et donc

$$
T_{r_4 r_5} = R_y(\gamma) \tau(L_4, 0, 0)
$$

## Formulation

En continuant d'appliquer la même méthode, on obtient alors une formulation pour la matrice que l'on cherche:

$$
T_{r_1 r_5}
=
\tau(L_1, 0, 0)
R_z (\alpha)
\tau(L_2, 0, 0)
R_y (\beta)
\tau(L_3, 0, 0)
R_z (\gamma)
\tau(L_4, 0, 0)
$$

En remplaçant $$\alpha$$, $$\beta$$ et $$\gamma$$ par les angles des moteurs, on obtiendra alors la matrice
homogène 4x4 de transformation permettant de passer du repère attaché au bout de la patte au repère du corps du
robot.

Pour savoir où est l'effecteur (le point $$D$$) dans le corps, on peut simplement remarquer que:

$$
D_{r_5} = 
\begin{bmatrix}
0 \\ 0 \\ 0 \\ 1
\end{bmatrix}
$$

Et calculer:

$$
D_{r_1} = T_{r_1 \color{red}{r_5}} D_{\color{red}{r_5}}
$$
