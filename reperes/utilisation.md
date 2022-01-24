---
title: Utilisation
layout: default
permalink: /reperes/utilisation
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

Comme expliqué dans [Modern Robotics, chapitre 3.1](/assets/MR.pdf), les repères peuvent servir
à plusieurs choses que nous allons décrire ici.

# Changer un point de repère

C'est la première application que nous avons expliquée, pour un point $$P$$ dont les coordonnées
$$P_{r_2}$$ sont connues dans un repère $$\{ r_2 \}$$:

<div class="text-center">
    <img src="/assets/imgs/changement_repere.svg" width="300" />
</div>

Alors, le changement de repère $$T_{r_1 r_2}$$ nous permettra d'obtenir ses coordonnées dans $$\{ r_1 \}$$:

$$
P_{r_1} = T_{r_1 r_2} P_{r_2}
$$

# Définir la position/orientation d'un objet

La matrice de transformation $$T_{w r}$$ d'un repère $$\{ r \}$$ attaché à un objet vers un
repère $$\{ w \}$$ monde, est une manière de représenter la position et l'orientation de cet
objet dans le monde:

<div class="text-center">
    <img src="/assets/imgs/pose.svg" width="300" />
</div>

* En 2D, une telle configuration correspond à **3 degrés de liberté**
* En 3D, une telle configuration correspond à **6 degrés de liberté**

cf [Modern Robotics, chapitre 2.1](/assets/MR.pdf)

# Transformer des coordonnées entre avant et après un mouvement

En mélangeant les deux concepts vus précédemment, imaginons qu'un repère $$\{ r_1 \}$$ soit attaché
à un objet rigide "avant" qu'il ait bougé, et qu'un repère $$\{ r_2 \}$$ soit attaché au même objet
"après" qu'il ait bougé:

<div class="text-center">
    <img src="/assets/imgs/motion.svg" width="300" />
</div>

Si on s'intéresse à un point $$P$$, dont on connaît les coordonnées avant le mouvement $$P_{r_1}$$,
on peut chercher les coordonnées $$P'_{r_1}$$ de ce même point après le mouvement, mais dans le
repère initial.

On peut remarquer que $$P_{r_1} = P'_{r_2}$$, comme le point est "attaché" à l'objet, ses coordonnées
dans le repère de l'objet sont les même avant et après le mouvement. On peut donc en déduire:

$$
P'_{r_1} = T_{r_1 r_2} P'_{r_2} = T_{r_1 r_2} P_{r_1}
$$

Cette dernière partie de l'équation semble étrange, car la règle d'annulation de l'indice voudrait que
$$T_{r_1 r_2}$$, transforme un point provenant de $$\{ r_2 \}$$. Il s'agit bien d'un changement de repère,
mais que l'on peut interpréter différemment. En effet, ici, nous transformons les coordonnées d'un point
$$P$$ exprimées dans $$\{ r_1 \}$$ avant un déplacement en des coordonnées du même point **également**
exprimées dans $$\{ r_1 \}$$ mais après le déplacement.


Dans la prochaine partie, nous verrons comment ce que nous avons vu peut être [généralisé en 3D](/reperes/3d)