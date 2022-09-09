---
title: Implémentation Python
layout: default
permalink: /reperes/python2d
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

Dans les chapitres précédents, nous avons vu comment représenter un repère et effectuer un
changement de repère. Maintenant, nous allons voir comment nous pouvons implémenter cela en
Python.

# Numpy et le calcul matriciel

Pour commencer, nous allons importer la bibliothèque *numpy*, qui permet d'effectuer de
multiples opérations d'algèbre linéaire, dont le calcul matriciel:

```python
import numpy as np
```

Pour créer une matrice dans *numpy*, il suffit d'encapsuler une liste dans un `np.array`:

```python
# Une matrice 2x2
M = np.array([[1, 2],
              [3, 4]])
# Un vecteur
v = np.array([5, 6])
```

Pour effectuer une opération matricielle, on peut utiliser la fonction `np.dot`, ou l'opérateur
`@`:

```python
np.dot(M, v) # array([17, 39])
# ou
M @ v  # array([17, 39])
```

(Ici, $$17 = 1*5 + 2*6$$ et $$39 = 3*5 + 4*6$$)

<div class="alert alert-warning">
    Attention: comme vous le remarquez ici, <code class="language-plaintext highlighter-rouge">v</code>
    ne dispose que d'une dimension, <em>numpy</em> suppose donc qu'il s'agit d'un vecteur colonne.
    Si vous écrivez <code class="language-plaintext highlighter-rouge">v @ M</code>,
    <em>numpy</em> supposera que <code class="language-plaintext highlighter-rouge">v</code> est un
    vecteur ligne, et le résultat sera différent.
</div>

# Matrice de rotation

On peut donc implémenter une matrice de rotation de la façon suivante:

```python
def R(alpha):
    return np.array([[np.cos(alpha), -np.sin(alpha)],
                     [np.sin(alpha), np.cos(alpha)]])
```

Pour transformer les coordonnées d'un point, on pourra donc utiliser:

```python
# Un point de coordonnees 1, 2
P = np.array([1, 2])
# Ce point rotaté de 0.3 radians
P_rot = R(0.3) @ P
```

La transposée de la matrice s'obtient avec `.T`:

```python
R(0.5) @ R(0.5).T
# array([[1., 0.],
#        [0.,  1.]])
```

# Changements de repères

L'addition de deux `np.array` s'effectue élément par élément, on peut donc écrire le code du
changement de repère de la façon suivante:

```python
# Un point P est en 1, 2 dans r2
P_r2 = np.array([1., 2.])
# L'origine de r2 dans r1
A = np.array([5., 2.])
# L'angle entre x1 et x2 (les vecteurs x des deux repères)
alpha = 0.3

# L'implémentation du changement de repère
P_r1 = R(alpha) @ P_r2 + A # array([5.36429608, 4.20619318])
# On peut le faire dans l'autre sens pour retrouver P_r2
P_r2 = R(alpha).T @ (P_r1 - A) # array([1., 2.])
```

# Coordonnées homogènes

En coordonnées homogènes, on pourra écrire les opérations "pures":

```python
def rotation(alpha):
    return np.array([[np.cos(alpha), -np.sin(alpha), 0.],
                     [np.sin(alpha),  np.cos(alpha), 0.],
                     [           0.,             0., 1.]])

def translation(x, y):
    return np.array([[1., 0., x],
                     [0., 1., y],
                     [0., 0., 1.]])
```

Et le changement de repère:

```python
def frame(alpha, x, y):
    return translation(x, y) @ rotation(alpha)
```

En utilisant la formule vue dans [la partie matricielle](/reperes/matrix), on peut également
écrire une fonction qui calcule l'inverse de cette matrice:

```python
def frame_inv(T):
    R = T[:2, :2] # On extrait la rotation
    t = T[:2, 2:] # On extrait la translation
    upper = np.hstack((R.T, -R.T @ t))
    lower = np.array([0., 0., 1.])
    return np.vstack((upper, lower))
```

Ainsi, le même exemple que précédemment pourra s'écrire:

```python
# Un point P est en 1, 2 dans r2
P_r2 = np.array([1., 2., 1.])
# L'origine de r2 dans r1
A = np.array([5., 2., 1.])
# L'angle entre x1 et x2 (les vecteurs x des deux repères)
alpha = 0.3

T_r1_r2 = frame(alpha, A)
T_r2_r1 = frame_inv(T_r1_r2)

P_r1 = T_r1_r2 @ P_r2 # array([5.36429608, 4.20619318, 1.        ])
P_r2 = T_r2_r1 @ P_r1 # array([1., 2., 1.]
```

<hr/>

Dans la prochaine partie, nous verrons comment les [repères peuvent être utilisé](/reperes/utilisation)