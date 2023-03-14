---
title: Variante hexapode
layout: default
permalink: /quadruped/hexapod
---

[&laquo; Retour](/quadruped/)

## Assemblage du robot

<div class="text-center mb-2">
    <img src="/quadruped/img/hexapod.png" width="300" />
</div>

<div class="alert alert-info d-flex align-items-center justify-content-center">
    <img src="/quadruped/img/onshape.png" width="48" class="m-2" />

    <div>
        <big><a href="https://cad.onshape.com/documents/b3c76efa067c048eb62315bd/w/939d052c7ff15d37bbafeb47/e/5a1d349e9f30d2b073ade5d0">Assemblage OnShape complet</a></big>
        <br/>
        <em>Cet assemblage vous permettra d'obtenir les dimensions nécessaires!</em>
    </div>
</div>

## Utilisation dans le simulateur (modèle `hexapod`)

La variante hexapode peut être obtenue à l'aide des options suivantes:

```
python simulator.py -r hexapod
```

Tous les modes présentés dans le TP (`direct`, `inverse`, `legs`, `draw`, `walk`) sont également compatibles!

<div class="text-center mb-2">
    <img src="/quadruped/img/hexapod_pybullet.png" width="300" />
</div>

## Utilisation dans le simulateur (modèle `hexapod_fast`)

Vous pouvez également utiliser le modèle `hexapod_fast`, qui ne contient que des formes pures (le rendu sera moins
beau, mais le temps de calcul sans doute meilleur):

```
python simulator.py -r hexapod_fast
```

<div class="text-center mb-2">
    <img src="/quadruped/img/hexapod_fast_pybullet.png" width="300" />
</div>