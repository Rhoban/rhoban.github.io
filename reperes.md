---
title: Repères
layout: default
permalink: /reperes/
---

Lorsqu'un robot évolue, nous avons envie de pouvoir parler de la position et d'orientation
des éléments. Un robot étant mobile et/ou articulé, ses degrés de liberté font que la position
relative des éléments change au cours du temps. Aussi, les mesures capturées par les capteurs
(Par exemple, les pixels sur l'image d'une caméra ou la position des obstacles vues par un LiDAR)
sont obtenues d'un point de vue intrinsèque.

En guise d'illustration, considérons la situation suivante:

<div class="text-center">
    <img src="/assets/imgs/motivation.svg" />
</div>

On peut imaginer les questions suivantes:

* Connaissant la position/orientation de mon robot, et sachant qu'il perçoit un obstacle, où se trouve
cet obstacle pour un autre robot ?
* Sachant la position d'une caméra fixée sur un robot à un endroit connu, et un objet détecté sur l'image,
où est cet objet sur le sol ?
* Si un satellite positionne un robot ainsi qu'une balise fixe au sol, où est le robot par rapport à la balise
fixe ?
* Si un robot perçoit un objet d'interêt et qu'il se déplace, où est l'objet après le déplacement ?

Pour répondre à ces questions, nous introduisons la notion de *repères* (les éléments notés entre
accolades sur la figure ci-contre).

# Définitions

## Repères

Un repère est défini par:

* Un point d'**origine**,
* Une **base**, qui est un ensemble de vecteurs

Par exemple, $$(O, \vec{x_1}, \vec{y_1})$$ forme un repère:

<div class="text-center">
    <img src="/assets/imgs/repere.svg" />
</div>

Ici, nous nous intéresserons uniquement aux repères **orthonormés**, c'est à dire dont
les vecteurs de la base sont unitaires (de longueur $$1$$) et orthogonaux deux à deux.

## Coordonnées

On appelle coordonnées d'un point $$P$$ dans le repère $$(O, \vec x_1, \vec y_1)$$
et on les notes $$\begin{bmatrix} x \\ y \end{bmatrix}$$ (respectivement $$\begin{bmatrix} x \\ y \\ z \end{bmatrix}$$ en 3D) tel que:

$$
\vec{OP} = x \vec{x_1} + y \vec{y_1}
$$

<div class="text-center">
    <img src="/assets/imgs/coordonnees.svg" />
</div>

Pour l'instant, vous pouvez considérer $$\begin{bmatrix} x \\ y \end{bmatrix}$$ comme une simple notation,
mais nous verrons plus tard qu'il s'agit d'un *vecteur colonne*.

## Notations et convention

### Repères

Pour parler d'un repère pourra nommer son origine ainsi que les vecteurs de sa base $$(O, \vec{x_1}, \vec{y_1})$$.
Cependant, si nous n'en avons pas besoin, on pourra simplement lui donner un nom. Par convention, ce nom sera
noté entre accolades (par exemple $$\{r\}$$) dans les figures:

<div class="text-center">
    <img src="/assets/imgs/repere_implicite.svg" />
</div>

### Coordonnées d'un point dans un repère

Les coordonnées d'un point $$P$$ dans un repère $${r}$$ seront notées $$P_r$$. Ces coordonnées sont donc un vecteur
de dimension 2 ou 3 (selon si on travaille en 2D ou en 3D).

### Couleurs d'axe

Dans les illustrations et les logiciels, la convention de couleur est la suivante:

* <span style="color:red">Rouge pour l'axe $$\vec{x}$$</span>
* <span style="color:green">Green pour l'axe $$\vec{y}$$</span>
* <span style="color:blue">Bleu pour l'axe $$\vec{z}$$</span>

Pour s'en souvenir, pensez au moyen mémo-technique: **XYZ = RGB**

Dans la partie suivante, nous parlerons des [changements de repères](changement_reperes.md)