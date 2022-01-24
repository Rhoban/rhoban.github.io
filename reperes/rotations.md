---
title: Rotations
layout: default
permalink: /reperes/rotations
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

# Des changements de base aux rotations

Dans la [partie précédente](/reperes/changements), nous avons dit que si on pouvait exprimer
les vecteurs d'une base $$(\vec{i'}, \vec{j'})$$ en fonction des vecteurs d'une autre base
$$(\vec{i}, \vec{j})$$ sous la forme:

$$
\vec{i'} = \lambda_1 \vec{i} + \lambda_2 \vec{j} \\
\vec{j'} = \lambda_3 \vec{i} + \lambda_4 \vec{j} 
$$

On pouvait alors effectuer un **changement de base**:

$$
\begin{cases}
x = \lambda_1 x' + \lambda_3 y' \\
y = \lambda_2 x' + \lambda_4 y'
\end{cases}
\space \space \space \space (1)
$$

Ces quatres nombres $$(\lambda_1, \lambda_2, \lambda_3, \lambda_4)$$ sont en fait soumis à trois contraintes,
car les repères sont orthonormés:

1. Le vecteur $$\vec{i'}$$ est unitaire: $$\|\vec{i'}\| = 1$$
2. Le vecteur $$\vec{j'}$$ est unitaire: $$\|\vec{j'}\| = 1$$
3. Les vecteurs $$\vec{i'}$$ et $$\vec{j'}$$ sont orthogonaux.

Ils peuvent donc êtes entièrement définis par un seul nombre, comme par exemple l'angle $$\alpha$$ entre
$$\vec{i}$$ et $$\vec{i'}$$.

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

Prenons un point $$P$$ dans un repère $$(O, \vec{i}, \vec{j})$$, et essayons de calculer les coordonnées
de $$P'$$, son image par une rotation d'un angle $$\alpha$$ dans ce même repère.

Une manière de voir ce problème est de considérer un nouveau repère $$(O, \vec{i'}, \vec{j'})$$, avec un
angle de $$\alpha$$ entre $$\vec{i}$$ et $$\vec{i'}$$:

<div class="text-center">
    <img src="/assets/imgs/rotation.svg" />
</div>

La rotation est une opération *linéaire*, c'est à dire qu'elle commute aux opérations sur les vecteurs.
De ce fait, dans ce nouveau repère, les coordonnées de $$P'$$ sont les mêmes que celles de $$P$$ dans le
repère initial (avant que le point n'aie rotaté).On peut donc directement appliquer l'équation $$(2)$$:

$$
\begin{cases}
x = cos(\alpha) x' - sin(\alpha) y' \\
y = sin(\alpha) x' + cos(\alpha) y
\end{cases}
$$

Où $$\begin{bmatrix} x \\ y \end{bmatrix}$$ sont les coordonnées du point après rotation et
$$\begin{bmatrix} x' \\ y' \end{bmatrix}$$ celles du point avant la rotation.

C'est pour cette raison qu'on pourra appeller cette équation la **formule de la rotation**.

<hr/>

Dans la partie suivante, nous verrons que nous pouvons utiliser [l'algèbre matriciel](/reperes/matrix)
pour représenter les changements de base.