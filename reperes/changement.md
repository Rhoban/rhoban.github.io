---
title: Changements de repères
layout: default
permalink: /reperes/changements
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

Dans la [partie précédente](reperes.md), nous avons introduit le concept de *repères*. Jusqu'ici,
ces derniers permettent de définir la position d'un point dans le plan ou l'espace.

Dans cette partie, nous allons discuter de comment changer un point de repère.

# Changement de base

Supposons tout d'abord que seule la base de deux repères est différente, mais que l'origine est la même.
On peut par exemple prendre $$\{r_1\} = (O, \vec{x_1}, \vec{y_1})$$ et $$\{r_2\} = (O, \vec{x_2}, \vec{y_2})$$:

<div class="text-center">
    <img src="/assets/imgs/2bases.svg" />
</div>

On notera:

* $$\begin{bmatrix} x \\ y \end{bmatrix}$$ les coordonnées de $$P_{r_1}$$, le point $$P$$ dans le repère $$\{ r_1 \}$$
* $$\begin{bmatrix} x' \\ y' \end{bmatrix}$$ les coordonnées de $$P_{r_2}$$, le point $$P$$ dans le repère $$\{ r_2 \}$$

Ce qui équivaut à dire:

$$
\vec {OP} = 
\begin{cases}
x \vec {x_1} + y \vec{y_1} \\
x' \vec{x_2} + y' \vec{y_2} \space \space \space \space  (1)
\end{cases}
$$

<div class="alert alert-info">
    <b>Question</b>: si on connaît les coordonnées `(x', y')` de `P` dans `\{ r_2 \}`, comment trouver les coordonnées
`(x, y)` de `P` dans `\{ r_1 \}` ?
</div>

Dans cette partie, nous allons supposer que nous savons décomposer $$\vec{x_2}$$ et $$\vec{y_2}$$ en fonction de
$$\vec{x_1}$$ et $$\vec{y_1}$$, c'est à dire que l'on connaît $$(\lambda_1, \lambda_2, \lambda_3, \lambda_4)$$ tels que:

$$
\vec{x_2} = \lambda_1 \vec{x_1} + \lambda_2 \vec{y_1} \\
\vec{y_2} = \lambda_3 \vec{x_1} + \lambda_4 \vec{y_1} 
$$

Dans ce cas, on peut donc substituer $$\vec{x_2}$$ et $$\vec{y_2}$$ dans $$(1)$$:

$$
x' \vec{x_2} + y' \vec{y_2} \\
= x' (\lambda_1 \vec{x_1} + \lambda_2 \vec{y_1}) + y' (\lambda_3 \vec{x_1} + \lambda_4 \vec{y_1}) \\
= 
\underbrace{(\lambda_1 x' + \lambda_3 y')}_{x} \vec{x_1}
+
\underbrace{(\lambda_2 x' + \lambda_4 y')}_{y} \vec{y_1}
$$

Ce qui nous permet d'identifier $$x$$ et $$y$$:

$$
x = (\lambda_1 x' + \lambda_3 y') \\
y = (\lambda_2 x' + \lambda_4 y')
$$

Nous noterons cette opération:
$$\begin{bmatrix} x \\ y \end{bmatrix} = R_{r_1 r_2} \begin{bmatrix} x' \\ y' \end{bmatrix}$$

De manière générale, pour se rappeller du "sens" de l'opération, on appliquera la règle d'annulation
du subscript:

$$
P_{r_1} = R_{r_1 \color{red}{r_2}} P_{\color{red}{r_2}}
$$

Ici, $$\{ \color{red}{r_2} \}$$ disparaît après l'opération.

Nous utilisons la lettre $$R$$ ici car cette transformation dans des bases orthonormées est en fait une
*rotation* (nous y reviendront plus tard).

# Changement de repère

Prenons maintenant deux repères,
$$\{ r_1 \} = (O, \vec{x_1}, \vec{y_1})$$ et 
$$\{ r_2 \} = (A, \vec{x_2}, \vec{y_2})$$:

<div class="text-center">
    <img src="/assets/imgs/2reperes.svg" />
</div>

On appellera $$\begin{bmatrix} x' \\ y' \end{bmatrix}$$ les coordonnées de $$P$$ dans $$\{ r_2 \}$$, et on souhaite trouver
$$\begin{bmatrix} x \\ y \end{bmatrix}$$, les coordonnées de $$P$$ dans $$\{ r_1 \}$$.

On introduit un repère intermédiaire $$\{r_3\} = (A, \vec{x_1}, \vec{y_1})$$. Sur la figure ci-dessus,
on peut le voir en opacité réduite: on a "reporté" les vecteurs $$\vec{x_1}$$ et $$\vec{x_2}$$ de
$$\{ r_1 \}$$ autour de l'origine $$A$$.

Grâce à la partie précédente, on peut exprimer la position du point $$P$$ dans $$\{ r_3 \}$$:

$$
P_{r_3} = R_{r_3 r_2}(P_{r_2})
$$

(Notez que l'opération $$R_{r_3 r_2}$$ est la même que $$R_{r_1 r_2}$$, car seule la base est utilisée
dans ce changement)

Une fois cela fait, on peut facilement retrouver $$\begin{bmatrix} x \\ y \end{bmatrix}$$ par **translation**.
En effet, on observe par relation de Chasles que: $$\vec{OP} = \vec{OA} + \vec{AP}$$. Les vecteurs étant dans
la même base, cette propriété est vraie pour leurs coordonnées, et donc:

$$
P_{r_1} = R_{r_1 r_2} (P_{r_2}) + A_{r_1}
$$

<div class="alert alert-info">
    <b>Changement de repère</b>
    <hr/>

    Soit un repère `\{ r_1 \} = (O, \vec{x_1}, \vec{y_1})`,
    un repère `\{ r_2 \} = (A, \vec{x_2}, \vec{y_2})`
    et un point `P`, on a:
    $$P_{r_1} = R_{r_1 r_2} (P_{r_2}) + A_{r_1}$$

    <hr/>

    Avec:

    <ul>
    <li>`P_{r_1}` sont les coordonnées de `P` dans `\{ r_1 \}`</li>
    <li>`R_{r_1 r_2}` est l'opération du changement de base des vecteurs de la base de `\{ r_2 \}` vers les vecteurs
    de la base de `\{ r_1 \}`</li>
    <li>`P_{r_2}` sont les coordonnées de `P` dans `\{ r_2 \}`</li>
    <li>`A_{r_1}` sont les coordonnées de `A` dans `\{ r_1 \}`</li>
    </ul>
</div>

Par la suite, nous verrons comment nous pouvons exprimer les vecteurs d'une base en fonction d'une autre base
à l'aide de [rotations](/reperes/rotations).
