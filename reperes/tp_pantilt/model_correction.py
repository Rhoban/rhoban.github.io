import numpy as np
import utils
import torch as th
from mlp import MLP

l1 = 0.195
l2 = 0.0825
net = None

def direct(alpha, beta):
    """
        Reçoit en paramètre les angles du robot, retourne la
        matrice homogène 4x4 permettant de passer du repère de l'effecteur au
        repère du monde.
    """
    return utils.Rz(alpha) @ utils.translation(0, 0, l1) @ utils.Ry(beta) @ utils.translation(0, 0, l2)




def laser(alpha, beta):
    """
        Reçoit en paramètre les angles du robot, retourne la
        position d'un laser qui serait émis par l'effecteur et qui arriverait au sol.

        Retourne None si le laser ne touche pas le sol.
    """
    T_world_effector = direct(alpha, beta)
    pos = T_world_effector[:3, 3]
    ux = T_world_effector[:3, 0]

    if ux[2] <= 0:
        ratio = - pos[2] / ux[2]
        pos_on_floor = pos + ratio * ux
        return pos_on_floor[:2]
    else:
        return [0., 0.]
    






def inverse(x, y):
    """
        Calcule Les angles cibles pour viser un point au sol
    """
    # Analytic
    alpha = np.arctan2(y, x)
    d1 = np.linalg.norm([x, y])
    d2 = np.linalg.norm([l1, d1])
    theta1 = np.arctan(d1 / l1)
    theta2 = np.arccos(l2 / d2)
    beta = np.pi - theta1 - theta2

    return [alpha, beta]

def inverse_nn(x, y):
    """
        Pareil que inverse, mais en utilisant le réseau de neurones
    """
    global net

    if net is None:
        net = MLP(2, 2)
        net.load()

    laser_pos = th.tensor([x, y])
    with th.no_grad():
        angles = net(laser_pos).numpy()
    return angles