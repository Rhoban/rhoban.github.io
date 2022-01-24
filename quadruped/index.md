---
title: Locomotion quadrupède
layout: default
permalink: /quadruped/
---

Dans ce module, nous travaillerons sur un simulateur, avec comme objectif de faire marcher un robot quadrupède dans un simulateur physique.

<div class="text-center mb-2">
    <img src="/assets/imgs/sim.png" width="200" />
</div>

<div class="alert alert-info d-flex align-items-center justify-content-center">
    <img src="/quadruped/img/zip.png" />

    <div>
        <big><a href="/quadruped/quadruped.zip">Téléchargez l'archive quadruped.zip</a></big>
        <br/>
        <em>Ceci est le projet initial à compléter au cours du TP guidé</em>
    </div>
</div>

L'objectif est de compléter le contenu de `quadruped/control.py`. Chaque étape ci-dessous vous amènera à compléter une partie du code qui vous permettra d'obtenir une marche fonctionnelle. **Attention: ne touchez pas à `quadruped/simulator.py`**

# Séances

* [Installation et lancement](/quadruped/install)
* [Prise en main du simulateur](/quadruped/intro)
    * Objectif: `python simulator.py -m sandbox`
    * Ici vous pourrez placer le code de votre premier essai
* [Modèle géométrique inverse](/quadruped/kinematics)
    * Objectif: `python simulator.py -m inverse`
    * Le mode inverse sera fonctionnel
* [Interpolation linéaire](/quadruped/interpolation)
    * Objectif: `python simulator.py -m draw`
    * La patte du robot dessine un triangle, vous implémenterez `interpolation.py`
* [Contrôle des quatre pattes du robot](/quadruped/legs)
    * Objectif: `python simulator.py -m legs`
    * Vous contrôlez l'ensemble des pattes du robot en même temps en cartésien

# Rendu final

L'objectif final du projet est d'utiliser les fonctions écrites précédemment pour obtenir une locomotion quadrupède.
Vous pourrez écrire ce code dans la fonction `walk`, et utiliser le mode:

```
python simulator.py -m walk
```

Voici les objectifs:

* Les mouvements sont conçus dans l'espace opérationnel $$x, y, z$$ et utilisent le
[modèle géométrique inverse](/quadruped/kinematics) du robot
* Les mouvements sont "lisses", vous utiliserez des [interpolations lineéaires](/quadruped/interpolation)
* La vitesse de déplacement se basera sur les paramètres `speed_x` et `speed_y` disponibles par les
sliders latéraux
* En bonus, vous pourrez également écouter le paramètre `speed_rotation` pour gérer la rotation du robot.


