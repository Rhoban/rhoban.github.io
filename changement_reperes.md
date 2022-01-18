---
title: Changements de repères
layout: default
permalink: /changement_reperes/
---

Dans la [partie précédente](reperes.md), nous avons introduit le concept de *repères*. Jusqu'ici,
ces derniers permettent de définir la position d'un point dans le plan ou l'espace.

Dans cette partie, nous allons discuter de comment changer un point de repère.

# Changement de base

Supposons tout d'abord que seule la base de deux repères est différente, mais que l'origine est la même.
On peut par exemple prendre $$\{r_1\} = (O, \vec{x_1}, \vec{y_1})$$ et $$\{r_2\} = (O, \vec{x_2}, \vec{y_2})$$:

<div class="text-center">
    <img src="/assets/imgs/2bases.svg" />
</div>

*Note: en 2D, ces deux bases correspondent à une rotation*

On notera:

* $$(x, y)$$ les coordonnées de $$P_{r_1}$$, le point $$P$$ dans le repère $$\{ r_1 \}$$
* $$(x', y')$$ les coordonnées de $$P_{r_2}$$, le point $$P$$ dans le repère $$\{ r_2 \}$$

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
\underbrace{(x' \lambda_1 + y' \lambda_3)}_{x} \vec{x_1}
+
\underbrace{(x' \lambda_2 + y' \lambda_4)}_{y} \vec{y_1}
$$

Ce qui nous permet de trouver $$x$$ et $$y$$.

# Changement de repère

