---
title: Exemple de value iteration
layout: default
permalink: /ia/dice_example
---

## Un dé

L'objectif de ce tutoriel est d'implémenter l'algorithme de *value iteration* sur un exemple simple.
voici le problème que nous allons résoudre:

<div class="alert alert-secondary">
    <div class="text-center float-end m-2">
        <img src="/ia/dice/dice.png" />
    </div>
    Un joueur lance un dé. Il a alors deux choix:
    <ul>
        <li>Garder le score du dé, le jeu se termine</li>
        <li>Relancer le dé, il perd alors un point</li>
    </ul>
    Par exemple, voici une séquence de jeu:
    <ul>
        <li>Je lance le dé, j'obtiens 1, je décide de relancer</li>
        <li>Je lance le dé, j'obtiens 2, je décide de relancer</li>
        <li>Je lance le dé, j'obtiens 6, je décide d'arrêter</li>
        <li>Score final: (-1) + (-1) + 6 = 4</li>
    </ul>
    L'objectif est de trouver la meilleure stratégie à ce jeu.
</div>

Nous allons implémenter l'algorithme suivant:

<div class="text-center">
    <img src="/ia/dice/vi.png" style="max-width:600px" />
</div>

## Représentation du jeu

On peut représenter ce jeu par le
[processus de décision markovien](https://fr.wikipedia.org/wiki/Processus_de_d%C3%A9cision_markovien)
suivant:

<div class="text-center">
    <img src="/ia/dice/mdp.svg" />
</div>

Ici:

* les noeuds bleus sont des états (`s1 ... s6`: les faces du dé, `st`: état terminal)
* les noeuds rouges sont les actions possibles (`throw`: lancer le dé, `finish`: terminer le jeu)
* les arcs noirs sont les effets possibles d'une action, ils sont annotés de leur probabilité
* les arcs rouges sont les actions que l'on peut effectuer à partir d'un état, l'étiquette correspond à la récompense
obtenue

En Python, on peut représenter les états par une liste de nombres, et le modèle par un dictionnaire:

```python
states = range(7)
nonterminal_states = states[1:]
```

L'état `0` est l'état terminal, et les autres états correspondent au numéro indiqué sur le dé.

Nous avons ensuite besoin de représenter le *modèle* du jeu, c'est à dire $$p(s' | s, a)$$, pour cela, on peut
utiliser un dictionnaire

```python
model = {}
for s in nonterminal_states:
    model[s] = [
        {
            'name': 'terminate',
            'reward': s,
            'target': [[1., 0]]   
        },
        {
            'name': 'rethrow',
            'reward': -1,
            'target': [[1/6., t] for t in range(1,7)]   
        },
    ]
```

Ici, le modèle est une liste d'actions représentées par un nom, une récompense, et une distribution de probabilité
sur les états cibles.

## Algorithme de value iteration

On peut alors écrire l'algorithme de *value iteration* comme cela:

```python
values = {s: 0 for s in states}

changed = True
while changed:
    changed = False
    for s in nonterminal_states:
        possible_values = []
        for a in model[s]:
            value = a['reward']
            for p, s_target in a['target']:
                value = value + p * values[s_target]
            possible_values.append(value)
        new_value = max(possible_values)
        if new_value != values[s]:
            changed = True
            values[s] = new_value
```

Ici, on itère sur tous les états, puis on cherche l'action ayant la meilleur valeur. Si cette valeur est différente
de la valeur actuelle, on la met à jour. On continue jusqu'à ce qu'on ait fait une itération complète sur tous
les états sans ayant mis à jour une seule valeur.

## Politique optimale

Une fois l'algorithme de *value iteration* exécuté, on dispose de la fonction de valeur de la politique optimale.
On peut à nouveau faire une passe sur les états pour lister toutes les actions qui correspondent à cette valeur:

```python
for s in nonterminal_states:
    print('== State %d, v=%f' % (s, values[s]))
    for a in model[s]:
        returns = a['reward']
        for p, s_target in a['target']:
            returns = returns + p * values[s_target]
        if returns == values[s]:
            print('- optimal action: %s' % a['name'])
```

On obtient alors:

```text
== State 1, v=3.000000
- optimal action: rethrow
== State 2, v=3.000000
- optimal action: rethrow
== State 3, v=3.000000
- optimal action: terminate
- optimal action: rethrow
== State 4, v=4.000000
- optimal action: terminate
== State 5, v=5.000000
- optimal action: terminate
== State 6, v=6.000000
- optimal action: terminate
```

La stratégie optimale est de relancer le dé pour les valeurs 1 et 2, de terminer pour les valeurs 4, 5 et 6. Pour la
valeur 3, les deux actions ont une espérance similaire.

[Version complète du script dice.py](/ia/dice/dice.py)