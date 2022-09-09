import numpy as np

def direct(angles):
    """
        Reçoit en paramètre les angles du robot, retourne la
        matrice homogène 4x4 permettant de passer du repère de l'effecteur au
        repère du monde.
    """
    return np.array([[1.0, 0.0, 0.0, 0.5],
                     [0.0, 1.0, 0.0, 0.5],
                     [0.0, 0.0, 1.0, 0.0],
                     [0.0, 0.0, 0.0, 1.0]])

def laser(angles):
    """
        Reçoit en paramètre les angles du robot, retourne la
        position d'un laser qui serait émis par l'effecteur et qui arriverait au sol.

        Retourne None si le laser ne touche pas le sol.
    """
    return [1.0, 0.0]

def camera(angles, target, imgSize, aperture):
    """
        Reçoit en paramètre les angles du robot, la position d'une cible dans
        le monde et la taille de l'image d'une caméra d'ouverture de aperture radians.

        Retourne la position de la cible dans l'image de la caméra, ainsi que sa taille
        (rayon, en pixels).
    """
    return [0.0, 0.0, 5]

def camera2(angles):
    """
    Reçoit en paramètre les angles du robot, retourne la position des coins
    de l'image projetés à 2m, sauf si ils intersectent le sol
    """

    return [ [1.5, 0.5, 0.], [0.5, 0.5, 0.], [0.5, -0.5, 0.], [1.5, -0.5, 0.]]

def inverseTarget(x, y, z, yaw, pitch, roll):
    """
    Reçoit la position d'un repère cible et retourne la matrice (homogène) de transformation
    pour ce repère cible
    """

    return np.eye(4)

def points(M):
    """
    Reçoit une matrice de changement de repère et retourne la position des points
    [0,0,0], [0.1,0,0], [0,0.1,0] et [0,0,0.1] dans ce repère

    """

    return []

def inverse(targets, x, y, z, yaw, pitch, roll):
    """
    Reçoit la position actuelle des moteurs et une position cible, retourne une nouvelle position
    cible pour les moteurs pour que l'effecteur atteigne la position et l'orientation cible
    """

    # Utiliser scipy.minimize

    return {'motor'+str(k+1): 0 for k in range(6)}