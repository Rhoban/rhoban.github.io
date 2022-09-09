---
title: "Coordonnées: exercice"
layout: default
permalink: /reperes/ex_coordonnees
---

[&laquo; Retour au sommaire](/reperes)

# Coordonnées

On considère les repères $$\{ r_1 \}$$, $$\{ r_2 \}$$ et $$\{ r_3 \}$$ suivants:

<div class="text-center">
    <img src="/assets/imgs/reperes_grille.svg" />
</div>

Tous les points sont positionnés sur une grille unitaire permettant une lecture graphique.

* Trouvez les coordonnées de $$P_{r_1}$$ et de $$Q_{r_1}$$
* Trouvez les coordonnées de $$P_{r_2}$$ et de $$Q_{r_2}$$
* Trouvez les coordonnées de $$C_{r_1}$$
* Trouvez les coordonnées de $$P$$ dans le repère $$(A,\vec{i'}, \vec{j'})$$
* Trouvez les coordonnées de $$P$$ dans le repère $$(Q,\vec{i}, \vec{j})$$
* Soit le point $$S$$ tel que $$S_{r_3} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$, trouvez $$S_{r_1}$$
* Trouvez les coordonnées de $$P_{r_3}$$
* Même question si on avait $$35°$$ au lieu de $$45°$$ pour l'angle entre $$\vec{i}$$ et $$\vec{i'}$$

# Géométrie et vecteurs

Un robot veut entrer dans une maison. Pour cela, on a placé deux balises sur les murs (les points $$A$$ et $$B$$),
que le robot a repéré dans son repère monde $$\{w\}$$, où il connaît également sa position $$R$$ et on orientation
$$\alpha$$:

<div class="text-center">
    <img src="/assets/imgs/house.svg" />
</div>

On sait que le centre d'une porte $$P$$ se trouve à une distance $$d$$ le long du mur entre les balises $$A$$
et $$B$$.

Les calculs ci-dessous ne sont pas numérique (on s'attend à des formules):

* Calculez la position du point $$P$$

Afin d'entrer dans la maison sans entrer en collision avec les murs, on propose de passer tout d'abord par un
point intermédiaire $$P'$$, situé à une distance $$l$$ de $$P$$ perpendiculairement au mur.

* Calculez la position du point $$P'$$.
* Proposez une manière de vérifier si le robot se situe dans la maison où à l'extérieur de la maison (sur la figure,
le point $$P'$$ est à l'extérieur).
* Calculez la distance du robot au mur.
* Calculez l'angle dont le robot doit tourner pour faire face au point $$P'$$.