---
title: "Repères: exercices d'application"
layout: default
permalink: /reperes/ex_reperes
---

[&laquo; Retour au sommaire](/reperes)

Dans cet exercice, on notera $$\{ w \}$$ le repère monde, et $$\{ r \}$$ le repère robot. Le robot se trouve
donc sur le point $$A$$ et son "avant" est le vecteur $$\vec{i'}$$:

<div class="text-center">
    <img src="/assets/imgs/robot_world.svg" />
</div>

# Partie 1

Chaque question de cette partie sont indépendantes.

## Question 1

Le robot se situe en $$\begin{bmatrix} 17 \\ 22 \end{bmatrix}$$ dans le repère monde, son orientation est $$\alpha = 32 \deg$$. 
Il voit le point $$P$$ dans son propre repère en $$\begin{bmatrix} -2 \\ 7 \end{bmatrix}$$.

*Où est le point $$P$$ dans le repère monde ?*

## Question 2

Le robot dispose de son orientation dans le repère monde à l'aide de sa boussole, il sait ainsi que
$$\alpha = 120 \deg$$, et il perçoit le point $$P$$ en $$\begin{bmatrix} 18 \\ 4 \end{bmatrix}$$ dans son repère.
Ce point $$P$$ est connu pour se trouver dans le repère monde en $$\begin{bmatrix} -5 \\ 9 \end{bmatrix}$$
(on peut imaginer que c'est un obstacle connu).

*Où se trouve le robot?*

## Question 3

Le point $$P$$ se situe en $$\begin{bmatrix} 5 \\ -2 \end{bmatrix}$$ dans le repère monde. Le robot se situe en
$$\begin{bmatrix} 8 \\ 3 \end{bmatrix}$$ dans le repère monde. Il avance tout droit (c'est à dire le long du
vecteur $$\vec{i'}$$) et se retrouve en $$(9, 4$$).

*Où se situe le point $$P$$ dans le repère du robot ?*

## Question 4

Le point $$P$$ se situe en $$\begin{bmatrix} 4 \\ 2 \end{bmatrix}$$ dans le repère robot, qui lui même est situé en
$$\begin{bmatrix} -4 \\ 8 \end{bmatrix}$$ et a une orientation de $$12 \deg$$ dans le repère monde. Le robot se déplace et arrive
en $$\begin{bmatrix} -7 \\ 9 \end{bmatrix}$$ avec une orientation de $$14 \deg$$.

*Où est le point $$P$$ dans le repère robot à présent ?*

# Partie 2

Dans cette partie, on partira des données suivante:

<hr/>

*La position du robot est repérée dans le monde par un dispositif externe, il se trouve
en $$\begin{bmatrix} 2.5 \\ 2 \end{bmatrix}$$.*

*Le point $$P$$ est un point dont la position dans le monde est connue pour être en
$$\begin{bmatrix} 1 \\ 4 \end{bmatrix}$$. Le robot a déterminé l'orientation de ce point dans son
propre repère comme étant de $$1.6 rad$$.*

<hr/>


* Quelle est l'orientation du robot dans le monde ?
* Quelle est la position de $$P$$ dans le repère robot ?
* Le robot a repéré un autre point $$Q$$ en $$\begin{bmatrix} 2 \\ -1.5\end{bmatrix}$$ dans son repère,
où est-il dans le monde ?
* Le robot avance de 1m droit devant lui (selon le vecteur $$\vec{i'}$$), quelle est sa nouvelle position dans le
repère monde ?
* Le robot pivote de $$0.3 rad$$ (sur lui même). Quelle est désormais la position du point $$P$$ dans le repère du
robot?