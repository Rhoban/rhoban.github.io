---
title: Notations matricielles
layout: default
permalink: /reperes/matrix
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

Dans les parties précédentes, nous avons vu le lien entre un changement de base et une rotation.
Dans cette partie, nous allons voir que nous pouvons utiliser l'algèbre des matrices pour
représenter ces transformations.

# Matrices, vecteurs et multiplication

Les **matrices** sont des objets mathématiques qui sont représentées sous forme de tableaux à deux
dimensions, par exemple:

$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

Les **vecteurs** sont des matrices à une seule colonne:

$$
\begin{bmatrix}
e \\
f
\end{bmatrix}
$$

La multiplication matricielle $$A \times B$$ s'effectue en multipliant les lignes de $$A$$ par les colonnes
de $$B$$, voici un exemple:

<div class="text-center">
    <img src="/assets/imgs/multiplication.svg" width="300" />
</div>

Ici, on multiplie une matrice 2x2 par une matrice 2x1 (un vecteur). On multiplie donc d'abord les éléments de
la première ligne $$\begin{bmatrix}a & b\end{bmatrix}$$ par ceux de l'unique colonne $$\begin{bmatrix}e \\ f\end{bmatrix}$$,
ce qui donne $$a \times e + b \times f$$, puis les éléments de la deuxième ligne $$\begin{bmatrix}a & b\end{bmatrix}$$
par la même colonne pour obtenir $$c \times e + d \times f$$.

<div class="alert alert-danger">
    Attention, ce calcul n'est <b>pas</b> commutatif. C'est à dire que `A B != B A`.
    Dans le cas d'une multiplication <em>matrice x vecteur</em>, `B A` n'est même pas correct car
    les dimensions ne sont pas bonnes (`A` doit avoir autant de colonnes que `B` de lignes).
</div>

# Matrice de rotation

## Expression

L'équation suivante du changement de base entre deux repères orthonormés 2D avec un angle
$$\alpha$$:

$$
\begin{cases}
x = cos(\alpha) x' - sin(\alpha) y' \\
y = sin(\alpha) x' + cos(\alpha) y
\end{cases}
$$

Peut donc s'écrire en notation matricielle:

$$
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\underbrace{
\begin{bmatrix}
cos(\alpha) & -sin(\alpha) \\
sin(\alpha) & cos(\alpha)
\end{bmatrix}
}_{R(\alpha)}
\begin{bmatrix}
x' \\
y'
\end{bmatrix}
$$

On appelle $$R(\alpha)$$ la **matrice de rotation**.

## Utilisation

Si on dispose de deux repères $$\{ r_1 \} = (O, \vec{x_1}, \vec{y_1})$$ et $$(O, \vec{x_2}, \vec{y_2})$$ avec un angle
$$\alpha$$ entre $$\{ r_2 \} = \vec{x_1}$$ et $$\vec{x_2}$$, alors la matrice de rotation $$R(\alpha)$$ est
la matrice de changement de base de $$\{ r_2 \}$$ vers $$\{ r_1 \}$$:

$$
R_{r_1 r_2} = R(\alpha)
$$

Dans $$\{ r_2 \}$$, les coordonnées du vecteur $$\vec{x_2}$$ sont $$\begin{bmatrix} 1 \\ 0 \end{bmatrix}$$, après
changement de base on obtient:

$$
\begin{bmatrix}
cos(\alpha) & -sin(\alpha) \\
sin(\alpha) & cos(\alpha)
\end{bmatrix}
\begin{bmatrix}
1 \\
0
\end{bmatrix}
=
\begin{bmatrix}
cos(\alpha) \\
sin(\alpha)
\end{bmatrix}
$$

Aussi, les coordonnées de $$\vec{y_2}$$ sont $$\begin{bmatrix} 0 \\ 1 \end{bmatrix}$$, on obtient donc:

$$
\begin{bmatrix}
cos(\alpha) & -sin(\alpha) \\
sin(\alpha) & cos(\alpha)
\end{bmatrix}
\begin{bmatrix}
0 \\
1
\end{bmatrix}
=
\begin{bmatrix}
-sin(\alpha) \\
cos(\alpha)
\end{bmatrix}
$$

Donc, la première **colonne** de la matrice de rotation peut être vue comme les **coordonnées** du premier vecteur
de **l'ancienne base** exprimées dans la **nouvelle base**, et ainsi de suite:

$$
R =
\begin{bmatrix}
\vec{x_2}_{r_1} &
\vec{y_2}_{r_1} 
\end{bmatrix}
$$

Où $$\vec{x_2}_{r_1}$$ est le vecteur 2x1 des coordonnées de $$\vec{x_2}$$ dans $$\{ r_1 \}$$ et
$$\vec{y_2}_{r_1}$$ le vecteur 2x1 des coordonnées de $$\vec{y2}$$ dans $$\{ r_1 \}$$.

# Inverse d'une matrice de rotation

## Inverse et transposée

L'inverse d'une matrice de rotation $$R(\alpha)$$ est la matrice $$R(-\alpha)$$:

$$
R(-\alpha)
=
\begin{bmatrix}
cos(-\alpha) & -sin(-\alpha) \\
sin(-\alpha) & cos(-\alpha)
\end{bmatrix}
=
\begin{bmatrix}
cos(\alpha) & sin(\alpha) \\
-sin(\alpha) & cos(\alpha)
\end{bmatrix}
$$

Car $$cos(-\alpha) = cos(\alpha)$$ (la fonction $$cos$$ est paire) et $$sin(-\alpha) = -sin(\alpha)$$ (la
fonction $$sin$$ est impaire).

On remarque que la diagonale ne change pas, et que les deux éléments hors-diagonale ont simplement été
inversés: $$R(-\alpha)$$ est ce qu'on appelle la **transposée** de $$R(\alpha)$$; une matrice dans
laquelle les lignes et les colonnes ont été inversés, on le note:

$$R(-\alpha) = R(\alpha)^T$$

## Inverse de la matrice

Supposons que l'on prenne les coordonnées d'un point $$P$$, nous avons dit que:

$$
P' = R(\alpha) P
$$

Permettait de calculer l'image de $$P$$ par une rotation de $$\alpha$$. Dans ce cas:

$$
P = R(-\alpha) R(\alpha) P
$$

Devrait être vrai pour tout $$P$$, car il s'agit d'effectuer une rotation dans un sens, puis dans l'autre sens
du même angle $$\alpha$$.

Pour vérifier, on peut multiplier les matrices ensemble:

$$
R(-\alpha) R(\alpha)
=
\begin{bmatrix}
cos(\alpha) & -sin(\alpha) \\
sin(\alpha) & cos(\alpha)
\end{bmatrix}
\begin{bmatrix}
cos(\alpha) & sin(\alpha) \\
-sin(\alpha) & cos(\alpha)
\end{bmatrix}

\\
=

\begin{bmatrix}
\underbrace{cos(\alpha)^2 + sin(\alpha) ^2}_{1} &
\underbrace{cos(\alpha) sin(\alpha) - cos(\alpha) sin(\alpha)}_{0} \\
\underbrace{cos(\alpha) sin(\alpha) - cos(\alpha) sin(\alpha)}_{0} &
\underbrace{cos(\alpha)^2 + sin(\alpha) ^2}_{1}
\end{bmatrix}

\\
=
\underbrace{
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
}_{I}
$$

La matrice obtenue ($$I$$) est appellée la matrice identité (c'est un élément neutre dans la multiplication:
elle ne change pas la matrice ou le vecteur par lequel elle est multipliée).

Donc:

$$
R(\alpha) R(-\alpha)
= R(-\alpha) R(\alpha)
= I
$$

Ce qui signifie que $$R(-\alpha) = R(\alpha)^T = R(\alpha)^{-1}$$, où $$-1$$ désigne ici
[l'inverse de la matrice](https://fr.wikipedia.org/wiki/Matrice_inversible) $$R(\alpha)$$.

# Changements de repères

<div class="text-center">
    <img src="/assets/imgs/changement_repere.svg" width="300" />
</div>

<div class="alert alert-info">
    Soit un repère `\{ r_1 \} = (O, \vec{x_1}, \vec{y_1})`,
    un repère `\{ r_2 \} = (A, \vec{x_2}, \vec{y_2})`,
    sachant que `\alpha` est l'angle entre `\vec{x_1}` et `\vec{x_2}`,
    pour point `P`, on a:
    $$P_{r_1} = R(\alpha) P_{r_2} + A_{r_1}$$

    <hr/>

    En inversant cette formule, on obtient:

    $$
    P_{r_2} = R(\alpha)^{-1} (P_{r_1} - A_{r_1})
    \space \space \space \space (1)
    $$
</div>

# Coordonnées homogènes

## Présentation

Comme on peut le remarquer, la formule du changement de repère ci-dessus comporte une partie
linéaire (la rotation) et une partie affine (la translation).

C'est pour cette raison qu'elle fait intervenir deux opérations:

* La **multiplication matricielle** $$R(\alpha) P_{r_2}$$,
* **L'addition vectorielle** avec $$A_{r_1}$$.

Il existe une méthode permettant de cumuler ces deux opérations dans une seule multiplication matricielle,
pour ce faire, on ajoutera un $$1$$ à la fin du vecteurs de coordonnées (il sera donc de dimension 3 en 2D
et de dimension 4 en 3D):

$$
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
$$

Ainsi, on utilisera des matrices dites **homogènes** de cette forme:

$$
\begin{bmatrix}
r_{11} & r_{12} & t_x \\
r_{21} & r_{22} & t_y \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
1
\end{bmatrix}
=

\begin{bmatrix}
r_{11} x + r_{12} y + t_x \\
r_{21} x + r_{22} y + t_ y \\
1
\end{bmatrix}
$$

On obtient des nouvelles coordonnées qui comportent la même rotation, mais avec également une translation.
Cette translation est rendue possible par la multiplication avec le terme $$1$$ du vecteur initial.
Ce $$1$$ est conservé par la multiplication avec la dernière ligne de la matrice homogène.

## Matrices de transformation

Ces matrices homogènes seront de dimension 3x3 en 2D et 4x4 en 3D, et auront donc la forme:

$$
T_{r_1 r_2}
=
\begin{bmatrix}
R(\alpha) & A_{r_1} \\
0_{1 \times 3} & 1
\end{bmatrix}
$$

On note ici $$T_{r_1 r_2}$$ la matrice de transformation du repère $$\{ r_2 \}$$ au repère
$$\{ r_1 \}$$. On pourra appliquer la même règle d'annulation du subscript qu'avec les rotations:

$$
P_{r_1} = T_{r_1 \color{red}{r_2}} P_{\color{red}{r_2}}
$$

Ici, $$\color{red}{r_2}$$ peut être éliminé. La même règle s'applique si on enchaîne les changements
de repères:

$$
P_{r_1} = T_{r_1 \color{red}{r_2}} T_{\color{red}{r_2} \color{red}{r_3}} P_{\color{red}{r_3}}
$$

## Inversion

En reprenant l'équation $$(1)$$, on a:

$$
P_{r_2} = R(\alpha)^{-1} P_{r_1} - R(\alpha)^{-1} A_{r_1}
$$

On peut donc en déduire $$T_{r_2 r_1}$$:

$$
T_{r_2 r_1}
=
\begin{bmatrix}
R(\alpha)^{-1} & -R(\alpha)^{-1} A_{r_1} \\
0_{1 \times 3} & 1
\end{bmatrix}
\space \space \space \space (2)
$$

Avec la règle vue précédemment:

$$
T_{r_1 \color{red}{r_2}} T_{\color{red}{r_2} r_1} = T_{r_1 r_1} = I
$$

$$T_{r_1 r_1}$$ est l'identité ($$I$$) car changer des coordonnées d'un repère à lui-même n'a aucun effet.
Donc, $$T_{r_2 r_1} = T_{r_1 r_2}^{-1}$$, l'inverse de $$T_{r_1 r_2}$$. Cependant, plutôt que d'inverser
la matrice, on utilisera plutôt l'équation $$(2)$$.