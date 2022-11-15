import time
from scipy.optimize import minimize
import numpy as np
import control


def translation(x, y, z):
    return np.array([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])


def Rx(alpha):
    return np.array([[1, 0, 0, 0], [0, np.cos(alpha), -np.sin(alpha), 0], [0, np.sin(alpha), np.cos(alpha), 0], [0, 0, 0, 1]])


def Ry(alpha):
    return np.array([[np.cos(alpha), 0, np.sin(alpha), 0], [0, 1, 0, 0], [-np.sin(alpha), 0, np.cos(alpha), 0], [0, 0, 0, 1]])


def Rz(alpha):
    return np.array([[np.cos(alpha), -np.sin(alpha), 0, 0], [np.sin(alpha), np.cos(alpha), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


def frame_inv(T):
    R = T[:3, :3]  # On extrait la rotation
    t = T[:3, 3:]  # On extrait la translation
    upper = np.hstack((R.T, -R.T @ t))
    lower = np.array([0.0, 0.0, 0.0, 1.0])
    return np.vstack((upper, lower))


def direct(angles):
    """
    Reçoit en paramètre les angles du robot (dictionnaire), retourne la
    matrice homogène 4x4 permettant de passer du repère de l'effecteur au
    repère du monde.
    """

    T = np.eye(4)
    T = T @ Rz(angles[0])
    T = T @ translation(0.32, 0, 0.68)
    T = T @ Ry(angles[1])
    T = T @ translation(0, 0, 0.975)
    T = T @ Ry(angles[2])
    T = T @ translation(0, 0, 0.2)
    T = T @ Rx(angles[3])
    T = T @ translation(0.887, 0, 0)
    T = T @ Ry(angles[4])
    T = T @ translation(0.2, 0, 0)
    T = T @ Rx(angles[5])

    return T


def intersectFloor(P, V):
    Z = P[2]
    dZ = V[2]

    if dZ < 0:
        l = -float(Z / dZ)
        return P + l * V
    return None


T_effector_tool = np.array(
    [[0.0, 0.0, 1.0, 0.191], 
    [1.0, 0.0, 0.0, -0.1465], 
    [0.0, 1.0, 0.0, 0.0], 
    [0.0, 0.0, 0.0, 1.0]
])

def direct_tool(angles):
    """
    Reçoit en paramètre les angles du robot, retourne la matrice homogène 4x4 permettant de
    passer du repère de l'outtil au repère du monde.
    """

    T_world_effector = direct(angles)

    return T_world_effector @ T_effector_tool


def laser(angles):
    """
    Reçoit en paramètre les angles du robot (dictionnaire), retourne la
    position d'un laser qui serait émis par l'effecteur et qui arriverait au sol.

    Retourne None si le laser ne touche pas le sol.
    """

    T_world_effector = direct(angles)
    P = T_world_effector @ [0.0, 0.0, 0.0, 1.0]
    V = (T_world_effector @ [1.0, 0.0, 0.0, 1.0]) - P

    return intersectFloor(P, V)


def camera(angles, target, imgSize, aperture):
    """
    Reçoit en paramètre les angles du robot (dictionnaire), la position d'une cible dans
    le monde et la taille de l'image d'une caméra d'ouverture de 60°.

    Retourne la position de la cible dans l'image de la caméra, ainsi que sa taille
    (rayon, en pixels).
    """
    T_world_effector = direct(angles)
    T_effector_world = frame_inv(T_world_effector)
    target_world = [target[0], target[1], target[2], 1]

    # Expressing the target in the camera frame
    target_effector = T_effector_world @ target_world

    focale = (imgSize / 2) / (aperture / 2.0)

    x = -target_effector[1] * focale / target_effector[0]
    y = target_effector[2] * focale / target_effector[0]

    r = max(1, ((target_effector[2] + 0.042) * focale / target_effector[0]) - y)

    return [x, y, r]


def camera2(angles, aperture):
    """
    Reçoit en paramètre les angles du robot (dictionnaire), retourne la position des coins
    de l'image projetés à 2m, sauf si ils intersectent le sol
    """

    T_world_effector = direct(angles)
    P = T_world_effector @ [0.0, 0.0, 0.0, 1.0]

    delta = (np.tan(aperture / 2)) * 2
    V1 = T_world_effector @ [2.0, delta, delta, 1.0]
    V2 = T_world_effector @ [2.0, delta, -delta, 1.0]
    V3 = T_world_effector @ [2.0, -delta, -delta, 1.0]
    V4 = T_world_effector @ [2.0, -delta, delta, 1.0]

    res = [V1, V2, V3, V4]
    for k in range(len(res)):
        tmp = intersectFloor(P, res[k] - P)
        if tmp is not None:
            res[k] = tmp[0:3]
        else:
            res[k] = res[k][0:3]

    return res


def inverseTarget(x, y, z, yaw, pitch, roll):
    M = translation(x, y, z) @ Rz(yaw) @ Ry(pitch) @ Rx(roll)

    return M


def points(T_world_effector):
    P = (T_world_effector @ [0.0, 0.0, 0.0, 1.0])[:3]
    P1 = (T_world_effector @ [0.1, 0.0, 0.0, 1.0])[:3]
    P2 = (T_world_effector @ [0.0, 0.1, 0.0, 1.0])[:3]
    P3 = (T_world_effector @ [0.0, 0.0, 0.1, 1.0])[:3]

    return [P, P1, P2, P3]


def inverse(angles, x, y, z, yaw, pitch, roll):
    T_world_effector = inverseTarget(x, y, z, yaw, pitch, roll)
    targetPoints = points(T_world_effector)

    def inverseScore(X):
        currentPoints = points(direct(X))
        return sum([np.linalg.norm(targetPoints[k] - currentPoints[k]) for k in range(len(currentPoints))])

    Y = minimize(inverseScore, angles, method="Nelder-Mead", options={"fatol": 0.001})

    return Y.x


def board(T_world_board, t):
    T_board_tool = np.array([
        [-1., 0., 0., 0.2 + np.cos(t*5)*.1],
        [0., 1., 0.,  0.2 + np.sin(t*5)*.1],
        [0., 0., -1., 0.],
        [0., 0., 0., 1.],
    ])

    return T_world_board @ T_board_tool @ np.linalg.inv(T_effector_tool)
