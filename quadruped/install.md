---
title: Installation sous windows
layout: default
permalink: /quadruped/install
---

[&laquo; Retour](/quadruped/)

# Linux

Installez les dépendances:

```
pip3 install numpy scipy pybullet matplotlib
```

# Windows

Attention, l'installation nécessite environ 10Go, vérifiez avant tout
que vous avez l'espace suffisant.

## Installation des build tools visual studio

Allez sur la page suivante: [Téléchargements (Microsoft)](https://visualstudio.microsoft.com/fr/downloads/)

**N'installez pas** visual studio. Au lieu de cela, rendez vous en bas de
la page. Développez la partie "Outils de build pour Visual Studio
2019", puis téléchargez "Build Tools pour Visual Studio 2019".

Ensuite, lancez l'installateur. Cochez la partie "Build Tools pour
C++" uniquement.  Attention, c'est un peu long...

## Installation de python3 avec Microsoft Store

Rendez-vous dans le Microsoft Store et installez Python (3.8 ou 3.9). Vous pourrez
vérifier que ça fonctionne en tappant:

```
py
```

Dans un terminal

## Mise à jour de pip

Lancez:

```
py -m pip install pip --upgrade pip
```

## Installation des dépendances

Pour installez les dépendances:

```
py -m pip install numpy scipy pybullet matplotlib
```

### Attention, l'installation a été testé avec python 3.8.5

<hr/>

Dans la prochaine partie, nous [prendrons en main le simulateur](/quadruped/intro).
