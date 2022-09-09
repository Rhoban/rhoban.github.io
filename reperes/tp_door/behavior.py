import numpy as np
import utils

STATE:str = "init"

def T_frame_wall(A_frame, B_frame):
    """
    À partir des coordonnées du point A et B, construit la matrice de transformation
    homogène 2D (3x3) permettant de passer du repère mur au repère dans lequel les
    points A et B ont été observés
    """    
    pass

def navigate_to(P_robot):
    """
    Reçoit en entrée un point dans le repère robot, et produit la vitesse cible pour que le
    robot navigue vers ce point

    - Si le point n'est pas en face du robot, on tourne pour s'aligner avec lui
    - Sinon, on avance tout droit pour l'atteindre
    """    
    return 0, 0

def robot_tick(A_world, B_world, A_robot, B_robot, X_world):
    """
    Le comportement du robot. On reçoit en entrée les coordonnées de A et B dans le monde
    (on suppose qu'ils sont connus de par le plan), et de A et B dans le robot (on suppose
    que le robot les détecte), et de X dans le monde.

    L'objectif est d'entrer dans la maison en passant par la porte et d'atteindre la cible X

            /!\ Attention /!\ 
    Ne touchez pas au fichier sim.py !
    """
    global STATE

    # Le retour est la vitesse d'avance du robot [m/s], et la vitesse de rotation du robot [rad/s]
    return 0, 0
