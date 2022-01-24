---
title: Interpolation
layout: default
permalink: /quadruped/interpolation
---

[&laquo; Retour](/quadruped/)

# Interpolation linéaire

Dans l'étape précédente, nous avons défini la position des moteurs à l'aide de position successives. Si
on dessinait la valeur des angles en fonction du temps, voici à quoi cela ressemblerait:

<div class="text-center">
<img src="/quadruped/img/steps.svg" width="350">
</div>

On aimerait éviter les changements "brutaux" de valeurs. Voici un exemple ce que l'on aimerait obtenir:

<div class="text-center">
<img src="/quadruped/img/lines.svg" width="350">
</div>

Pour cela, les cibles passent "progressivement" d'une valeur à une autre, on utilise une interpolation
linéaire.

# Objectif

On propose d'écrire une fonction `interpolate`, qui prend en paramètre:

* `values`: un tableau contenant des paires temps / valeur,
* `t`: le temps auquel on souhaite calculer la valeur interpolée.

On pourra par exemple tester cette méthode de cette façon:

```python
import matplotlib.pyplot as pyplot
import numpy as np

def interpolate(values, t):
    # Code à écrire!
    return 0

values = [ # Les valeurs à interpoler
    (0, 0),
    (1.2, 6),
    (2.5, -3),
    (3.3, -2),
    (4.2, -2),
    (5, 0)
]

ts = np.linspace(-1, 6, 100)
vs = [interpolate(values, t) for t in ts]

pyplot.scatter(ts, vs)
pyplot.show()
```

Si votre fonction fonctionne bien, vous devriez voir les points interpolé comme la figure de la section précédente.

# Version 3D

Créez une fonction `interpolate3d`, variante de `interpolate` qui fait l'interpolation entre des points 3D
(x, y, z).

# Dessin du triangle

En lançant le simulateur avec le mode `draw`:

```
python simulator.py -m draw
```

La fonction `draw` de `control.py` est appelée, et la trajectoire parcourue par le bout de la patte est déssinée
dans le simulateur.

L'objectif est de faire dessiner un triangle à notre robot, pour cela, voici comment procéder:

* Définissez trois points de passage (3D) avec chacun un temps (par exempe t=0, t=1 et t=2 secondes)
* Utilisez `interpolate3d` pour obtenir un point cible au temps `t` passé à `draw`
* Utilisez la fonction `inverse` implémentée dans la [précédente partie](/quadruped/kinematics) pour obtenir
des angles cibles que vous retournerez

<hr/>

Dans la prochaine partie, nous implémenterons le modèle cinématique inverse de [toutes les pattes](/quadruped/legs)
du robot
