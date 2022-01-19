---
title: Repères
layout: default
permalink: /reperes/intro
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

Lorsqu'un robot évolue, nous avons envie de pouvoir parler de la position et de l'orientation
des éléments qui le composent ou de son environnement.
Un robot étant mobile et/ou articulé, ses degrés de liberté font que certaines de ces positions
et orientations évoluent au cours du temps.
Aussi, les mesures capturées par les capteurs (Par exemple, les pixels sur l'image d'une caméra
ou la position des obstacles vues par un LiDAR) sont obtenues d'un point de vue intrinsèque à un
des composants, il est donc nécessaire de pouvoir les transposer d'un autre "point de vue",
c'est ce que nous allons formaliser ici.

En guise d'illustration, considérons la situation suivante:

<div class="text-center">
    <img src="/assets/imgs/motivation.svg" />
</div>

On peut imaginer les questions:

* Si on connaît la position/orientation du robot par rapport au sol, et du sol par rapport au
satellite, où se trouve le robot par rapport au satellite ?
* Supposons que le robot perçoive un obstacle de son propre point de vue, et que l'on connaisse
la position/orientation du robot par rapport au sol, où est cet obstacle par rapport au sol ?
* Sachant la position d'une caméra fixée sur un robot à un endroit connu, et un objet détecté sur l'image,
où est cet objet sur le sol ?
* Si un robot perçoit un objet d’intérêt et qu'il se déplace, où est l'objet après le déplacement ?

Pour répondre à ces questions, nous introduisons la notion de *repères* (les éléments notés entre
accolades sur la figure ci-dessus).

# Définitions

## Repères

Un repère est défini par:

* Un point d'**origine**,
* Un ensemble de vecteurs qu'on appelle la **base**.

Par exemple, $$(O, \vec{x_1}, \vec{y_1})$$ forme un repère d'origine $$O$$ et de base $$\vec{x_1}, \vec{y_1}$$:

<div class="text-center">
    <img src="/assets/imgs/repere.svg" />
</div>

Ici, nous nous intéresserons uniquement aux repères **orthonormés**, c'est à dire dont
les vecteurs de la base sont unitaires (de longueur $$1$$) et orthogonaux deux à deux.

## Coordonnées

On appelle coordonnées d'un point $$P$$ dans le repère $$(O, \vec x_1, \vec y_1)$$
les valeurs de $$\begin{bmatrix} x \\ y \end{bmatrix}$$ (respectivement $$\begin{bmatrix} x \\ y \\ z \end{bmatrix}$$ en 3D) tel que:

$$
\vec{OP} = x \vec{x_1} + y \vec{y_1}
$$

<div class="text-center">
    <img src="/assets/imgs/coordonnees.svg" />
</div>

Pour l'instant, vous pouvez considérer $$\begin{bmatrix} x \\ y \end{bmatrix}$$ comme une notation,
mais nous verrons plus tard qu'il s'agit d'un *vecteur colonne*.

## Coordonnées polaires

Dans un repère orthonormé, une autre représentation des coordonnées est la représentation **polaire**. Ces dernières,
notées $$\begin{bmatrix} \rho \\ \theta \end{bmatrix}$$, sont respectivement:

* $$\rho$$: la longueur $$\| \vec{OP} \|$$
* $$\theta$$: l'angle entre $$\vec{x_1}$$ et $$\vec{OP}$$

<div class="text-center">
    <img src="/assets/imgs/polaires.svg" />
</div>

## Conversions

### Polaire vers cartésien

Par définition des fonctions $$cos$$ et $$sin$$, on a:

$$
\begin{cases}
x = \rho cos(\theta) \\
y = \rho sin(\theta)
\end{cases}
$$

### Cartésien vers polaire

Dans la figure suivante:

<div class="text-center">
    <img src="/assets/imgs/polaires_cartesien.svg" />
</div>

On peut utiliser Pythagore dans le triangle rectangle pour trouver $$\rho = \sqrt{x^2 + y^2}$$.

Il est également possible de trouver $$\theta = atan(\frac{y}{x})$$. Mais cette formule souffre de deux problèmes:

1. Si $$x = 0$$, nous aurons une division par zéro,
2. Elle ne gère pas tous les quadrants du plan. En effet, sur la figure ci-dessus, on induit que $$P$$ est dans le
premier quadrant, mais ça n'est pas forcément le cas.

Un bon exemple pour comprendre ce second problème est de considérer les deux points
$$P = \begin{bmatrix}1 \\ 1\end{bmatrix}$$ et $$P' = \begin{bmatrix}-1 \\ -1\end{bmatrix}$$:

<div class="text-center">
    <img src="/assets/imgs/quadrants.svg" />
</div>

Comme on peut le constater, $$atan(\frac{-1}{-1})$$ = $$atan(\frac{1}{1})$$ = $$45 deg$$, or, on voudrait
$$\theta_1 = 45 deg$$ et $$\theta_2 = 135 deg$$.
Comme $$P'$$ est dans un autre quadrant que $$P$$, la formule ne fonctionne pas.

Pour résoudre ces problèmes, on peut utiliser la fonction $$atan2$$, qui prend **deux** arguments, $$y$$ et $$x$$
(dans cet ordre, en référence à $$\frac{y}{x}$$ passés à $$atan$$), la conversion peut donc se faire avec:

$$
\begin{cases}
\rho = \sqrt{x^2 + y^2} \\
\theta = atan2(y, x)
\end{cases}
$$

## Notations et convention

### Repères

Pour parler d'un repère, on pourra nommer son origine ainsi que les vecteurs de sa base $$(O, \vec{x_1}, \vec{y_1})$$.
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

<hr/>

Dans la partie suivante, nous parlerons des [changements de repères](/reperes/changements)