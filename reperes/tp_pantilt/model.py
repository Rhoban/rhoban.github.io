import numpy as np

def direct(alpha, beta):
    """
        Reçoit en paramètre les angles du robot, retourne la
        matrice homogène 4x4 permettant de passer du repère de l'effecteur au
        repère du monde.
    """
    return np.array([[1.0, 0.0, 0.0, 0.5],
                     [0.0, 1.0, 0.0, 0.5],
                     [0.0, 0.0, 1.0, 0.0],
                     [0.0, 0.0, 0.0, 1.0]])

def laser(alpha, beta):
    """
        Reçoit en paramètre les angles du robot, retourne la
        position d'un laser qui serait émis par l'effecteur et qui arriverait au sol.

        Retourne None si le laser ne touche pas le sol.
    """
    return [1.0, 0.0]

def inverse(x, y):
    """
        Calcule Les angles cible pour viser un point au sol
    """
    return [0., 0.]

def inverse_nn(x, y):
    """
        Pareil que inverse, mais en utilisant le réseau de neurones
    """
    return [0., 0.]