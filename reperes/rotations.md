---
title: Rotations
layout: default
permalink: /reperes/rotations
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

# Des changements de base aux rotations

Dans la [partie précédente](/reperes/changements), nous avons dit que si on pouvait exprimer
les vecteurs d'une base $$(\vec{x_2}, \vec{y_2})$$ en fonction des vecteurs d'une autre base
$$(\vec{x_1}, \vec{y_1})$$ sous la forme:

$$
\vec{x_2} = \lambda_1 \vec{x_1} + \lambda_2 \vec{y_1} \\
\vec{y_2} = \lambda_3 \vec{x_1} + \lambda_4 \vec{y_1} 
$$

On pouvait alors effectuer un **changement de base**:

$$
\begin{cases}
x = (\lambda_1 x' + \lambda_3 y') \\
y = (\lambda_2 x' + \lambda_4 y')
\end{cases}
\space \space \space \space (1)
$$

Ces quatres nombres $$(\lambda_1, \lambda_2, \lambda_3, \lambda_4)$$ sont en fait soumis à trois contraintes,
car les repères sont orthonormés:

1. Le vecteur $$\vec{x_2}$$ est unitaire: $$\|\vec{x_2}\| = 1$$
2. Le vecteur $$\vec{y_2}$$ est unitaire: $$\|\vec{y_2}\| = 1$$
3. Les vecteurs $$\vec{x_2}$$ et $$\vec{y_2}$$ sont orthogonaux.

Ils peuvent donc êtes entièrement définis par un seul nombre, comme par exemple l'angle $$\alpha$$ entre
$$\vec{x_1}$$ et $$\vec{x_2}$$.

# De l'angle au changement de base

On peut donc dessiner la figure suivante:

<div class="text-center">
    <img src="/assets/imgs/2bases_lambdas.svg" />
</div>

Qui nous permet de trouver, par trigonométrie:

$$
\lambda_1 = cos(\alpha) \\
\lambda_2 = sin(\alpha) \\
\lambda_3 = -sin(\alpha) \\
\lambda_4 = cos(\alpha) \\
$$

On peut donc en déduire la formule suivante en les substituant dans 1 $$(1)$$:

$$
\begin{cases}
x = cos(\alpha) x' - sin(\alpha) y' \\
y = sin(\alpha) x' + cos(\alpha) y
\end{cases}
\space \space \space \space (2)
$$

# Rotation

Prenons un point $$P$$ dans un repère $$(O, \vec{x_1}, \vec{y_1})$$, et essayons de calculer les coordonnées
de $$P'$$, son image par une rotation d'un angle $$\alpha$$ dans ce même repère.

Une manière de voir ce problème est de considérer un nouveau repère $$(O, \vec{x_2}, \vec{y_2})$$, avec un
angle de $$\alpha$$ entre $$\vec{x_1}$$ et $$\vec{x_2}$$:

<div class="text-center">
    <img src="/assets/imgs/rotation.svg" />
</div>

Dans ce nouveau repère, les coordonnées de $$P'$$ sont les mêmes que celles de $$P$$ dans le repère initial
(avant que le point n'aie rotaté). On peut donc directement appliquer l'équation $$(2)$$:

$$
\begin{cases}
x = cos(\alpha) x' - sin(\alpha) y' \\
y = sin(\alpha) x' + cos(\alpha) y
\end{cases}
$$

Où $$\begin{bmatrix} x \\ y \end{bmatrix}$$ sont les coordonnées du point après rotation et
$$\begin{bmatrix} x' \\ y' \end{bmatrix}$$ celles du point avant la rotation.

C'est pour cette raison qu'on pourra appeller cette équation la **formule de la rotation**.

Dans la partie suivante, nous verrons que nous pouvons utiliser [l'algèbre matriciel](/reperes/matrix)
pour représenter les changements de base.