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

Par exemple, $$(O, \vec{i}, \vec{j})$$ forme un repère d'origine $$O$$ et de base $$\vec{i}, \vec{j}$$:

<div class="text-center">
    <img src="/assets/imgs/repere.svg" />
</div>

Ici, nous nous intéresserons uniquement aux repères **orthonormés**, c'est à dire dont
les vecteurs de la base sont unitaires (de longueur $$1$$) et orthogonaux deux à deux.

## Coordonnées

On appelle coordonnées d'un point $$P$$ dans le repère $$(O, \vec i, \vec j)$$
les valeurs de $$\begin{bmatrix} x \\ y \end{bmatrix}$$ (respectivement $$\begin{bmatrix} x \\ y \\ z \end{bmatrix}$$ en 3D) tel que:

$$
\vec{OP} = x \vec{i} + y \vec{j}
$$

<div class="text-center">
    <img src="/assets/imgs/coordonnees.svg" />
</div>

Pour l'instant, vous pouvez considérer $$\begin{bmatrix} x \\ y \end{bmatrix}$$ comme une notation,
mais nous verrons plus tard qu'il s'agit d'un *vecteur colonne*.

<div class="alert alert-secondary d-flex align-items-center justify-content-center ">
    <div class="text-center">
        <img src="/assets/imgs/youtube.png" width="32" class="m-2" />
    </div>

    <div>
        <big><a target="_blank" href="https://www.youtube.com/watch?v=PXOAIJ-DQ-A">Capsule vidéo: Coordonnées cartésiennes (1/2)</a></big>
        <br/>
        <big><a target="_blank" href="https://www.youtube.com/watch?v=3WVT5pJ6rN8">Capsule vidéo: Coordonnées cartésiennes (2/2)</a></big>
    </div>
</div>

## Coordonnées polaires

Dans un repère orthonormé, une autre représentation des coordonnées est la représentation **polaire**. Ces dernières,
notées $$\begin{bmatrix} \rho \\ \theta \end{bmatrix}$$, sont respectivement:

* $$\rho$$: la longueur $$\| \vec{OP} \|$$
* $$\theta$$: l'angle entre $$\vec{i}$$ et $$\vec{OP}$$

<div class="text-center">
    <img src="/assets/imgs/polaires.svg" />
</div>

<div class="alert alert-secondary d-flex align-items-center justify-content-center ">
    <div class="text-center">
        <img src="/assets/imgs/youtube.png" width="32" class="m-2" />
    </div>

    <div>
        <big><a target="_blank" href="https://www.youtube.com/watch?v=fwEUYWZovY0">Capsule vidéo: Coordonnées polaires (1/2)</a></big>
        <br/>
        <big><a target="_blank" href="https://www.youtube.com/watch?v=fRWYfnuPM-0">Capsule vidéo: Coordonnées polaires (2/2)</a></big>
    </div>
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

Pour parler d'un repère, on pourra nommer son origine ainsi que les vecteurs de sa base $$(O, \vec{i}, \vec{j})$$.
Cependant, si nous n'en avons pas besoin, on pourra le représenter par un nom noté entre accolades
(par exemple $$\{r\}$$):

<div class="text-center">
    <img src="/assets/imgs/repere_implicite.svg" />
</div>

### Coordonnées d'un point dans un repère

Les coordonnées d'un point $$P$$ dans un repère $$\{ r \}$$ seront notées $$P_r$$. Ces coordonnées sont donc un vecteur
de dimension 2 ou 3 (selon si on travaille en 2D ou en 3D).

### Couleurs d'axe

Dans les illustrations et les logiciels, la convention de couleur est la suivante:

* <span style="color:red">Rouge pour l'axe $$\vec{x}$$</span>
* <span style="color:green">Green pour l'axe $$\vec{y}$$</span>
* <span style="color:blue">Bleu pour l'axe $$\vec{z}$$</span>

Pour s'en souvenir, pensez au moyen mémo-technique: **XYZ = RGB**

## Un "couteau-suisse" important: le produit scalaire

### Définition

Le [produit scalaire](https://fr.wikipedia.org/wiki/Produit_scalaire) (en anglais *dot product*, car il est noté par
un point) est une valeur scalaire obtenue à l'aide de deux vecteurs selon la définition suivante:

$$
\vec{u} \cdot \vec{v} =
\lVert \vec{u} \rVert
\lVert \vec{v} \rVert
cos(\widehat{\vec{u}, \vec{v}})
$$

Où $$\widehat{\vec{u}, \vec{v}}$$ est l'angle entre les deux vecteurs $$\vec{u}$$ et $$\vec{v}$$.

<div class="alert alert-warning">
    Attention: souvenez-vous bien que la valeur `\vec{u} \cdot \vec{v}` est un scalaire (un nombre) et non pas un vecteur
</div>

### Propriétés

**Le produit scalaire d'un vecteur avec lui même**

Le produit scalaire de $$\vec{u}$$ avec lui-même est égal à sa norme au carré (le cosinus de $$0$$ étant égal à $$1$$):

$$
\vec{u} \cdot \vec{u} = \lVert \vec{u} \rVert ^2
$$

**Le produit scalaire est symétrique**

$$\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$$

Ce qui découle de la commutativité des termes de la définition donnée précédemment, et du fait que la fonction
cosinus est paire.

**Le produit scalaire est compatible avec l'addition**

$$
\vec{a} \cdot (\vec{b} + \vec{c})
= \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}
$$

Pour plus d'informations: [bilinéarité du produit scalaire](https://fr.wikipedia.org/wiki/Produit_scalaire#Bilin%C3%A9arit%C3%A9).

### Dans une base orthonormée

Si on considère deux vecteurs $$\vec{u}$$ et $$\vec{v}$$ dont les coordonnées respectives dans une base orthonormée sont
$$\begin{bmatrix} x_1 \\ y_1\end{bmatrix}$$ et $$\begin{bmatrix} x_2 \\ y_2\end{bmatrix}$$:

<div class="text-center">
    <img src="/assets/imgs/u_v.svg" />
</div>

$$\require{cancel}$$

Alors:

$$
\begin{array}{ll}
\vec{u} \cdot \vec{v}
& = (x_1 \vec{i} + y_1 \vec{j}) \cdot (x_2 \vec{i} + y_2 \vec{j}) \\
& = x_1 x_2 \cancelto{1}{(\vec{i} \cdot \vec{i})} + x_1 y_2 \cancelto{0}{(\vec{i} \cdot \vec{j})}
 + y_1 x_2 \cancelto{0}{(\vec{j} \cdot \vec{i})} + y_1 y_2 \cancelto{1}{(\vec{j} \cdot \vec{j})} \\
& = x_1 x_2 + y_1 y_2
\end{array}
$$

(En 3D, on peut faire exactement le même raisonnement, le produit scalaire devient alors $$x_1 x_2 + y_1 y_2 + z_1 z_2$$).

### Utilisation

**Trouver l'angle entre deux vecteurs**

On peut utiliser le produit scalaire pour trouver l'angle formé par deux vecteurs:

$$
\theta = cos^{-1} (\frac{x_1 x_2 + y_1 y_2}{\lVert \vec{u} \rVert \lVert \vec{v} \rVert})
$$

(Ne pas oublier que $$cos^{-1}$$ retourne une valeur entre $$0$$ et $$\pi$$).

**Vérifier de quel côté d'un demi-plan/demi-espace/segment/droite on se trouve**

Supposons que l'on ait un demi-plan (ou en 3D un demi-espace), défini par un point $$A$$ qui soit sur sa
bordure, et un vecteur $$\vec{u}$$ normal à sa séparation:

<div class="text-center">
    <img src="/assets/imgs/half_plane.svg" />
</div>

Pour tester si un point $$P$$ appartient au demi-plan (partie verte ci-dessus), on peut utiliser le
signe du produit scalaire $$\vec{u} \cdot \vec{AP}$$. Si ce dernier est positif, on sera dans le
demi-plan (dans la partie "verte"), si il est négatif, on sera à l'extérieur du demi-plan (dans la partie
"rouge"), et si il est nul, on sera sur la bordure.

**Projeter un point sur une droite**

Si on reprend l'exemple précédent, mais avec $$\vec{u}$$ unitaire, on a donc:

$$\vec{u} \cdot \vec{AP} = cos(\theta) \lVert \vec{AP} \rVert $$

Sur la figure suivante, on constate dans le triangle $$A$$, $$P$$, $$P'$$, que cette valeur est la distance
de $$P$$ à la bordure du demi-plan:

<div class="text-center">
    <img src="/assets/imgs/half_plane_unit.svg" />
</div>

On peut donc trouver $$AP' = \vec{u} (\vec{u} \cdot \vec{AP})$$

**Tester si deux vecteurs sont orthogonaux**

On peut tester si deux vecteurs sont orthogonaux, en vérifiant que:

$$\vec{u} \cdot \vec{v} = 0$$

**Tester si trois points sont alignés**

On peut tester si trois points $$A, B$$ et $$C$$ sont alignés en vérifiant que:

$$\vec{AB} \cdot \vec{AC} = \lVert \vec{AB} \rVert \lVert \vec{AC} \rVert$$

<hr/>

Dans la partie suivante, nous parlerons des [changements de repères](/reperes/changements)