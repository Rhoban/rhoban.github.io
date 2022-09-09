---
title: TP Golf (Value Iteartion, Monte Carlo, Q-Learning)
layout: default
permalink: /ia/tp_golf/
---

<div class="text-center m-2 float-end">
    <img src="/ia/imgs/mini_golf.png" width="300" />
</div>

[&laquo; Retour au sommaire](/ia)

L'objectif de ce TP est de réaliser de l'apprentissage automatique sur un jeu (mini golf). La plupart du code
est déjà fourni, il faut donc essentiellement le lire et le comprendre afin de le compléter. Nous allons nous
concentrer sur trois algorithmes:

* Value Iteration
* Monte Carlo
* Q-Learning

# Ressources

<div class="alert alert-info d-flex align-items-center justify-content-center">
    <img src="/quadruped/img/zip.png" />

    <div>
        <big><a href="/ia/tp_golf.zip">Téléchargez l'archive tp_golf.zip</a></big>
        <br/>
        <em>Lisez les instructions ci-dessous</em>
    </div>
</div>

<div class="alert alert-secondary d-flex align-items-center justify-content-center ">
    <div class="text-center">
        <img src="/assets/imgs/youtube.png" width="32" class="m-2" />
    </div>

    <div>
        <big><a target="_blank" href="https://www.youtube.com/watch?v=LaKqhAemJD8">Capsule vidéo: les algorithmes en action</a></big>
    </div>
</div>

# Prise en main

## Archive

Télécharger et décompressez l'archive. Exécutez le jeu à l'aide de `python simulator.py`. Les contrôles
apparaissent dans le terminal.

Il y a trois fichiers source dans le projet:

* `render.py` qui gère l'affichage: vous n'avez pas à vous en occuper
* `simulator.py` qui gère le jeu en lui-même, il est important de comprendre ce que font les fonctions
* `agents.py` les agents dont nous allons compléter le code.

## Simulateur

Lisez `simulator.py` et essayez de répondre aux questions:

* Où est stockée la position actuelle de la balle ?
* Comment les obstacles sont ils représentés ?
* À quoi sert la fonction `get_kick_target` ?
* Où les déplacements de la balle sont ils simulés ? Comment ?
* Comment les collisions sont t-elles détectées, et où sont géré les rebonds de la balle contre les obstacles ?
* Quelle est la condition pour que la balle soit considérée comme entrée dans le trou ?
* Il est possible de jouer l'animation de la balle qui se déplace ou pas. Pourquoi ? Comment cela est-il
        implémenté ?
* Comment la balle est t-elle repositionnée dans le jeu, sans être déjà sur un obstacle ?

## Agents

Lisez `agents.py` (surtout la classe `Agent`) et essayez de répondre aux questions:

* À quoi servent les fonctions `position_to_state` et `state_to_position` ?
* Que fait la fonction `build_states` ?
* Comment l'agent par défaut choisit ses actions (lorsque vous appuyez sur `p`) ?
* Comment choisir quel agent sera utilisé dans le programme ?

# Value Iteration

## Compréhension

Lisez le code de `ValueIterationAgent`:

* Comment sont stockées les valeurs de la fonction $$V$$ ?
* La fonction `initialize` construit le modèle (déterministe) du jeu. Comment ce modèle est-il
    représenté ?
* À quoi sert le fichier `model.data` ?

## Construction du modèle

Changez le code pour que l'agent utilisé soit `ValueIterationAgent` et lancez le simulateur de manière à
générer le modèle de transition.

## Implémentation

Implémentez les fonctions manquantes, c'est à dire:

* `pick_action`: qui trouve l'action (et éventuellement le score) la meilleure pour un état donné,
    en utilisant le modèle et l'estimation actuelle de $V$ pour les récompenses futures.
    
* `learn`: qui fait une étape du value iteration (on pourra la déclencher avec `l`), c'est à
    dire qui met à jour $V$ pour chaque état (cf algorithme du value iteration).

Visualisez la carte des valeurs, et testez la politique avec la touche `p`.

# Model-free

## Compréhension

* Lisez le code de `pick_action`, comment l'action est t-elle sélectionnée ?
* Lisez le code de `learn`
* Que fait la ligne `episode = episode[-10:]` ? Pourquoi fait-on ça ?
* Quels sont les arguments passés à `update_q` ?
    Notamment, quelle est la différence entre `reward` et `returns` ?

## Implémentation Monte Carlo

Implémentez le code manquant dans `MonteCarloAgent` et exécutez l'algorithme.

## Implémentation Q-Learning

Pourquoi initialiser les valeurs de $$Q$$ à -10?

Implémentez le code manquant dans `QLearningAgent` et exécutez l'algorithme.
