---
title: Implémentation Python
layout: default
permalink: /reperes/python3d
mathjax: true
---

[&laquo; Retour au sommaire](/reperes)

Dans cette partie, nous allons reprendre ce qui a été vu sur les [rotations et transformations 3D](/reperes/3d)
et l'implémenter en Python.

Le code sera la suite de la [partie 2D](/reperes/python2d)

# Transformations élémentaires

On peut définir une translation par un vecteur étant comme étant:

```python
def translation(vector):
    return np.array([[1, 0, 0, vector[0]],
                     [0, 1, 0, vector[1]],
                     [0, 0, 1, vector[2]],
                     [0, 0, 0, 1]])
```

Et les rotations autour des trois axes:

```python
def Rx(alpha):
    return np.array([[1, 0, 0, 0],
                     [0, np.cos(alpha), -np.sin(alpha), 0],
                     [0, np.sin(alpha), np.cos(alpha), 0],
                     [0, 0, 0, 1]])

def Ry(alpha):
    return np.array([[np.cos(alpha), 0, np.sin(alpha), 0],
                     [0, 1, 0, 0],
                     [-np.sin(alpha), 0, np.cos(alpha), 0],
                     [0, 0, 0, 1]])
        
def Rz(alpha):
    return np.array([[np.cos(alpha), -np.sin(alpha), 0, 0],
                     [np.sin(alpha), np.cos(alpha), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
```

# Inverse

De manière très similaire à la version 2D, on peut inverser une matrice de transformation:

```python
def frame_inv(T):
    R = T[:3, :3] # On extrait la rotation
    t = T[:3, 3:] # On extrait la translation
    upper = np.hstack((R.T, -R.T @ t))
    lower = np.array([0., 0., 0., 1.])
    return np.vstack((upper, lower))
```
