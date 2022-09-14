---
title: Modèle direct de robots articulaires
layout: default
permalink: /reperes/inverse_kinematics
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

Précédemment, nous avons discuté de la cinématique directe des robots articulaires. Dans cd TD interactif,
nous allons discuter du problème inverse.

## Des exemples concrets

### Robot RL

<div class="text-center">
    <img src="/assets/imgs/rl.svg" width="500" />
</div>

* Exprimez le modèle géométrique direct du robot
* Exprimez le modèle géométrique inverse du robot


### Robot LR

<div class="text-center">
    <img src="/assets/imgs/lr.svg" width="500" />
</div>

* Exprimez le modèle géométrique direct du robot
* Exprimez le modèle géométrique inverse du robot

### Loi des cosinus

Dans un triangle **quelconque**, dont les côtés mesurent $$a$$, $$b$$ et $$c$$ et les angles sont $$\alpha$$, $$\beta$$
et $$\gamma$$, comme sur la figure suivante:

<div class="text-center">
<img src="/quadruped/img/al-kashi.svg" width=200>
</div>

Dans ce cas, on peut utiliser les égalités suivantes:

$$c^2 = a^2 + b^2 - 2ab cos \gamma$$

$$\gamma = arccos \frac{a^2 + b^2 - c^2}{2ab}$$

Autrement dit, à partir du moment ou trois des six valeurs ($$a$$, $$b$$, $$c$$, $$\alpha$$, $$\beta$$, $$\gamma$$) sont connues, il est possible de retrouver toutes les autres.
    
* [Article Wikipédia "Loi des cosinus"](https://fr.wikipedia.org/wiki/Loi_des_cosinus)

### Robot RR

<div class="text-center">
    <img src="/assets/imgs/rr.svg" width="500" />
</div>

* Exprimez le modèle géométrique direct du robot
* Exprimez le modèle géométrique inverse du robot

### Robot RRR

<div class="text-center">
    <img src="/assets/imgs/rrr.svg" width="500" />
</div>

* Exprimez le modèle géométrique direct du robot
* Exprimez le modèle géométrique inverse du robot
