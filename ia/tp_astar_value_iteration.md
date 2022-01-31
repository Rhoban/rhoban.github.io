---
title: TP A* et Value Iteration
layout: default
permalink: /ia/tp_astar_value_iteration/
---

<div class="text-center m-2 float-end">
    <img src="/ia/imgs/demo.png" width="300" />
</div>

[&laquo; Retour au sommaire](/ia)

Dans ce TP, l'objectif sera de guider un robot vers une case cible dans un monde "en grille". Nous implémenterons
deux algorithmes: *A\** et *Value Iteration*

# Ressources

<div class="alert alert-info d-flex align-items-center justify-content-center">
    <img src="/quadruped/img/zip.png" />

    <div>
        <big><a href="/ia/tp_astar_value_iteration.zip">Téléchargez l'archive tp_astar_value_iteration.zip</a></big>
        <br/>
        <em>Lisez les instructions ci-dessous</em>
    </div>
</div>

# Prise en main

Ouvrez l'archive et exécutez le code à l'aide de `python simulator.py`. Par défaut, cette commande
vous montre simplement le monde généré.

Il est également possible de préciser une "seed" (graine), permettant de générer un autre monde. Par exemple,
si vous lancez `python simulator.py -s 123`, vous verrez un monde différent de celui par défaut (qui
utilise la graine `0`).

L'objectif est, lorsque c'est possible, de trouver le plus court chemin menant le robot à la position cible
(ici la case verte). Un exemple est montré si vous utilisez le mode demo `python simulator.py -m demo`,
qui vous montre un chemin pour la graine 0 (codé en dur).

Parfois, il est impossible pour le robot de rejoindre la cible (regardez par exemple la carte pour la graine `32`).

**Lisez-le code attentivement**. Questions de compréhension:

* Lorsque le monde est généré, comment le nombre d'obstacles est-il choisi ?
* Le tableau `grid` est un tableau contenant les nombres `0`, `1` ou `2`. Que
    signifient ces valeurs?
* Comment est trouvée la solution dans le mode `demo` ?

# A\*

* À quoi sert la fonction `distance_estimation` de A\* ? Pourquoi la distance est-elle calculée
    de cette manière ?
* Si le code était complet, si on remplace le contenu de `distance_estimation` par
    `return 0`, quel sera l'effet sur l'algorithme du A\* ? (Si vous implémentez le code, n'hésitez pas
    à essayer!)

Complétez le code de `solve` qui explore les noeuds.

<div class="alert alert-info">
Indications: il s'agit ici de trouver le prochain noeud à explorer (celui ayant la distance la plus petite)
et de l'explorer. Faites attention au cas où il est impossible d'atteindre la cible!
</div>

Complétez le code de `build_path` qui construit le chemin vers la cible.

<div class="alert alert-info">
Indications: Le dictionnaire <kbd>parents</kbd> doit être utilisé ici: il permettra de "remonter" de
la cible au point de départ.
</div>

Vous pourrez tester votre code avec `python simulator.py -m a_star` (pensez à tester d'autres graines!)

# Value iteration

* Quelle est la fonction de récompense utilisée dans value iteration ?
* Une action `giveup`, qui donne systématiquement `-100` de score est ajoutée aux possibilités,
    pourquoi ?
* Comment choisir cette valeur (ici `-100`) pour que l'algorithme fonctionne ?

Implémentez le code manquant dans `do_iterations`.

<div class="alert alert-info">
Indications: il s'agit ici de récupérer la valeur de la meilleure action possible, et de la mettre à jour dans le
tableau <kbd>values</kbd>. Le flag <kbd>changed</kbd> permet de vérifier si au moins une valeur a changé durant
l'itération (condition pour arrêter l'algorithme).
</div>

Implémentez le code manquant dans `find_path`.

<div class="alert alert-info">
Indications: si votre tableau de valeurs a bien été calculé, vous pourrez vous appuyer sur <kbd>find_best_action</kbd>
pour obtenir la meilleure action à chaque étape, et sur <kbd>world.apply_move</kbd> pour appliquer cette action sur
votre position.
</div>

# Bilan

Expliquez la différence principale entre les deux algorithmes utilisés ici. Indiquez d'après vous dans quel
cas d'utilisation l'un ou l'autre est meilleur