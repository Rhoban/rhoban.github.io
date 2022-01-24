---
title: "TP: robot 2D"
layout: default
permalink: /reperes/tp_2d
---

[&laquo; Retour au sommaire](/reperes)

L'objectif du TP est de mettre sur pied une simulation élémentaire de robot mobile.

<div class="text-center m-2 float-end">
    <img src="/assets/imgs/tp_2d.png" width="300" />
</div>

# Ressources

<div class="alert alert-secondary d-flex align-items-center justify-content-center ">
    <div class="text-center">
        <img src="/assets/imgs/youtube.png" width="32" class="m-2" />
    </div>

    <div>
        <big><a target="_blank" href="https://www.youtube.com/watch?v=cCzQIGF-kZU">Capsule vidéo: Introduction au TP</a></big>
    </div>
</div>

<div class="alert alert-info d-flex align-items-center justify-content-center">
    <img src="/quadruped/img/zip.png" />

    <div>
        <big><a href="/reperes/tp_2d.zip">Téléchargez l'archive tp_2d.zip</a></big>
        <br/>
        <em>Lisez les instructions ci-dessous</em>
    </div>
</div>

# Lancement

Après avoir téléchargé l'archive ci-dessus, installez les dépendances:

```bash
python -m pip install pygame numpy # Linux
py -m pip install pygame numpy # Windows
```

Et lancez le tp:

```
python tp.py # Linux
py tp.py # Windows
```

Une fenêtre graphique intitulée `Robot` devrait s'ouvrir.

# 1. Affichage des FPS

En guise de préliminaire, nous allons calculer et afficher le nombre de FPS dans la fenêtre.

Dans le programme figurent deux variables `t0` et `t`. Pour le moment, elles ne sont utilisées que
pour afficher le temps écoulé depuis le lancement du programme (en haut de la fenêtre).

Introduire deux nouvelles variables `last_t` et `dt`. `last_t` est utilisée pour mémoriser la valeur de
`t` à la frame précédente; et `dt` mémorise le temps écoulé depuis la dernière *frame* (calculé en utilisant
`last_t`), c'est la *période*.

Puis, à l'aide de `dt`, calculez la fréquence de rafraîchissement (les *fps*) et affichez la dans la fenêtre avec
1 décimale.

# 2. Déplacement du robot

L'utilisateur peut déplacer le robot. Pour tester cela, lancer le programme et utilisez les flèches du clavier.
Ça marche, mais pas tout à fait comme il faudrait...

En effet, nous souhaitons que:


* Lorsque l'on appuie sur $$\uparrow$$, le robot **avance**
* Lorsque l'on appuie sur $$\downarrow$$, le robot **recule**
* Lorsque l'on appuie sur $$\leftarrow$$, le robot **pivote** sur
  la gauche. Plus précisément, il effectue une rotation sur lui-même
  sur la gauche sans se déplacer.
* Lorsque l'on appuie sur $$\rightarrow$$, le robot **pivote** sur
  la droite

Modifiez le programme de telle sorte à adopter ce comportement. Les vitesses de déplacement et de rotation sont à
votre discrétion (pour le moment).

Vous devrez prendre en considération la variable `robotOrient`. Avec cette information, construisez un vecteur
unitaire dont la direction est celle du robot. Puis, lorsque l'utilisateur appuie sur $$\uparrow$$ vous ajouterez
simplement ce vecteur à la position du robot pour le faire avancer. Le recul sera similaire. Pour la rotation du robot
sur lui même, pour que le robot tourne à gauche par exemple, vous ajouterez 1 degré à `robotOrient`. La rotation à
droite sera similaire.

N'oubliez pas que le robot est initialement dirigé vers le haut, et que l'axe des ordonnées graphiques va de
haut en bas.

<div class="text-center m-2 float-end">
    <img src="/assets/imgs/2d_robot_obstacles.png" width="300" />
</div>

# 3. Ajout d'obstacles

L'objectif de cette question est de permettre à l'utilisateur d'ajouter des obstacles dans l'environnement du robot
avec la souris. Les obstacles sont très simples, il s'agira de disques dont le rayon est fixé à 20 pixels une fois
pour toute.

Vous pouvez remarquer que les coordonnées de la souris sont affichées dans la fenêtre. En inspectant le code, vous
trouverez la variable `mousePos` qui les contient. Vous pourrez observer comment le code la met à jour à chaque frame.

Vous allez créer une liste `obstacles` sous la forme d'une variable globale dans le code. Ensuite, vous ferez en
sorte que lorsque l'utilisateur clique sur le bouton gauche de la souris, un obstacle est ajouté à l'environnement.
Vous stockerez ses coordonnées dans la liste évoquée précédemment. Puis, à chaque frame, vous afficherez tous les
obstacles de la liste.

Vous disposez d'un exemple de création de disque à la fin du code.

# 4. Repère graphique

Pour améliorer l'interface utilisateur, nous souhaitons maintenant introduire des fonctionnalités pour modifier la vue:
translation, zoom et rotation.

Pour faire cela convenablement il faut introduire 2 concepts: les coordonnées du **repère monde** et les coordonnées du
**repère graphique**. Ces deux repères seront orthonormés.

Le repère graphique est celui que nous utilisons déjà dans le code. L'unité est le pixel et vous avez remarqué que
l'origine est située dans le coin en haut à gauche, l'axe des abscisses va de gauche à droite et l'axe des ordonnées
va de haut en bas (ce qui est classique dans le monde du graphisme).

Nous allons considérer le **repère monde**. Initialement, l'origine du repère monde sera positionnée au centre de
l'image. Son axe des abscisses ira de gauche à droite, et son axe des ordonnées ira de bas en haut. L'unité du repère
monde sera le mètre et par défaut, un mètre sera représenté par 50 pixels.

Dans cette nouvelle version du programme, les éléments seront repérés dans le repère monde. Cela veut dire que les
coordonnées du robot, tout comme celles des obstacles seront stockées **relativement au repère monde** et non au
repère graphique comme c'est le cas actuellement.

* **Écrire deux fonctions `worldToGraphics(M)` et `graphicsToWorld(M)` où `M` est un vecteur coordonnée
(comportant 2 composantes donc), qui convertissent les coordonnées d'un point du repère monde vers le repère graphique
et réciproquement. Les fonctions retourneront les conversions**

* **En utilisant ces deux fonctions modifiez le programme sans changer ses fonctionnalités de telle sorte que les
coordonnées du robot (de `robotPos`) et celles des obstacles soient stockées dans le repère monde.**

Attention, les coordonnées graphiques seront *in fine* arrondies pour être entières.

# 5. Déplacements de la caméra

Introduire une fonctionnalité de translation et de zoom de la vue. Précisément, l'utilisateur utilisera les touche
`z`, `q`, `s`, `d` pour déplacer la vue vers le haut, la gauche, le bas et la droite. Et puis les touches
`p` et `m` pour zoomer et dé-zoomer respectivement.

Pour cela, vous introduirez une variable `viewPos` qui contiendra les coordonnées de l'origine du repère graphique,
ainsi qu'une variable `graphicScale` qui conservera le ratio de dimension entre les deux repères (graphique et monde).
Ces variables seront utilisées dans les fonctions `worldToGraphics(M)` et `graphicsToWorld(M`. `graphicScale` sera
également utilisé dans la fonction d'affichage du robot pour contrôler la taille du sprite, ainsi que sur la dimension
des disques représentant les obstacles.

Dessinez le repère monde dans la fenêtre. Bien sûr ce dernier doit suivre les mouvements de la vue.

# 6. Gestion des vitesses

Notre but maintenant est de contrôler la vitesse du robot indépendamment du rafraîchissement de la fenêtre et du zoom.
Sinon, la vitesse de déplacement du robot va être très dépendante de la puissance de votre machine, en particulier.

Pour ce faire, pour les commande d'avance et de recul du robot, ainsi que de rotation. En prenant en compte la période
de rafraîchissement du robot (l'inverse des FPS que vous avez calculé en Question 1), faite en sorte que le robot
avance et recule à la vitesse d'une unité-monde par seconde et de 60 degrés par seconde respectivement.

vous pourrez vérifier cela en modifiant le temps d'attente pour chaque frame définit à la fin du code par l'instruction:

```python
time.sleep(0.01)
# Ralentint l'execution: ça ne devrait PAS ralentir le robot
```

# 7. Champ de vision

Dans cette question, on se propose de considérer le "champ de vision" du robot. On va supposer que le robot
"voit" devant lui sur un secteur angulaire symétrique de 120 degrés, en particulier, les obstacles non visibles
par le robot seront représentés grisés (voir démo).

On considère le **repère-robot**. Comme précédemment, vous allez écrire deux fonctions `worldToRobot(M)`
et `robotToWorld(M)` qui calculeront le passage des coordonnées monde aux coordonnées robot et réciproquement.

A l'aide de ces fonctions, dessinez le repère-robot (sous le robot) dans la fenêtre.

Ensuite, lors de l'affichage, pour chacun des obstacles, vous utiliserez `worldToRobot(M)` pour calculer ses
coordonnées (cartésiennes) dans le repère robot. Puis, vous calculerez les coordonnées polaires de l'obstacle
dans le repère robot.

A l'aide de ses coordonnées polaires, vous déterminerez si l'obstacle est dans le champ de vision du robot ou non,
ce qui vous permettra de déterminer sa couleur d'affichage.

# 8. Collisions

Nous allons nous occuper ici de la collision éventuelle du robot
avec un obstacle.

Pour chaque obstacle, vous calculerez la distance entre l'obstacle
et le robot (dans le repère monde). Fort de cette information, vous
déterminerez si le robot est en contact ou non avec l'obstacle.

S'il est en contact, alors vous n'autoriserez le déplacement du
robot que **si se dernier lui permet de s'éloigner de l'obstacle,
ou bien reste à la même distance (rotation sur lui-même)**.

Du point de vue algorithmique, chaque obstacle pourra "interdire"
au robot d'avancer dans sa direction courante. Le robot pourra
toujours pivoter cependant.

<div class="alert alert-info">
    <b>Indication:</b> Pour tester si l'avance du robot est autorisée
    relativement à un obstacle donné, vous pourrez regarder les
    coordonnées polaires de l'obstacle en question dans le repère robot,
    ou bien (et c'est plus efficace) vous pourrez considérer le produit
    scalaire du vecteur robot-obstacle avec le premier vecteur de la
    base du repère robot.
</div>

# 9. (subsidiaire) Projectiles

Implémentez la possibilité de tirer des projectiles avec le
robot. Les projectiles, déclenchés par la barre espace, partiront du
robot, dans sa direction. Ils évolueront à vitesse
constante. Lorsqu'un projectile rencontre un obstacle, l'obstacle
disparaît.