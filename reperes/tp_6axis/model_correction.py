import math
import time
from scipy.optimize import minimize
import numpy as np

def Rz(alpha):
    return np.array([[math.cos(alpha), -math.sin(alpha), 0., 0.],
                      [math.sin(alpha), math.cos(alpha), 0., 0.],
                      [0., 0., 1., 0.],
                      [0., 0., 0., 1.]])

def Rx(alpha):
    return np.array([[1., 0., 0., 0.],
                      [0., math.cos(alpha), -math.sin(alpha), 0.],
                      [0., math.sin(alpha), math.cos(alpha), 0.],
                      [0., 0., 0., 1.]])

def Ry(alpha):
    return np.array([[math.cos(alpha), 0., math.sin(alpha), 0.],
                      [0., 1., 0., 0.],
                      [-math.sin(alpha), 0., math.cos(alpha), 0.],
                      [0., 0., 0., 1.]])

def T(x, y, z, multiplier=1000.0):
    return np.array([[1., 0., 0., x/multiplier],
                      [0., 1., 0., y/multiplier],
                      [0., 0., 1., z/multiplier],
                      [0., 0., 0., 1.]])

def inv(M):
    R = M[0:3, 0:3]
    T = M.T[3,:3]
    
    Mi = M.copy()
    Mi[0:3, 0:3] = R.T
    Mi.T[3, :3] = (-R.T.dot(T.T))

    return Mi

def direct(angles):
    """
        Reçoit en paramètre les angles du robot (dictionnaire), retourne la
        matrice homogène 4x4 permettant de passer du repère de l'effecteur au
        repère du monde.
    """

    M = np.eye(4)
    M = Rx(-angles['motor6']).dot(T(10.0, 0, 0))
    M = Ry(angles['motor5']).dot(T(285.0, 0, 0).dot(M))
    M = Rx(-angles['motor4']).dot(T(230.0, 0, 0).dot(M))
    M = Ry(-angles['motor3']).dot(T(105.0, 0, 0).dot(M))
    M = Ry(angles['motor2']).dot(T(0.0, 0, 275.0).dot(M))
    M = Rz(-angles['motor1']).dot(T(0.0, 0, 105.0).dot(M))
    M = T(0.0, 0.0, 45.0).dot(M)

    return M

def intersectFloor(P, V):
    Z = P[2]
    dZ = V[2]

    if dZ < 0:
        l = -float(Z/dZ)    
        return P + l*V
    return None

def laser(angles):
    """
        Reçoit en paramètre les angles du robot (dictionnaire), retourne la
        position d'un laser qui serait émis par l'effecteur et qui arriverait au sol.

        Retourne None si le laser ne touche pas le sol.
    """

    M = direct(angles)
    P = M.dot(np.array([0., 0., 0., 1.]).T)
    V = M.dot(np.array([1., 0., 0., 1.]).T) - P

    return intersectFloor(P, V)

def camera(angles, target, imgSize, aperture):
    """
        Reçoit en paramètre les angles du robot (dictionnaire), la position d'une cible dans
        le monde et la taille de l'image d'une caméra d'ouverture de 60°.

        Retourne la position de la cible dans l'image de la caméra, ainsi que sa taille
        (rayon, en pixels).
    """
    M = direct(angles)
    targetInCameraFrame = inv(M).dot(np.array([target[0], target[1], target[2], 1]).T)

    focale = (imgSize/2)/(aperture/2.0)

    x = -targetInCameraFrame[1] * focale/targetInCameraFrame[0]
    y = targetInCameraFrame[2] * focale/targetInCameraFrame[0]

    r = max(1, ((targetInCameraFrame[2] + 0.042) * focale/targetInCameraFrame[0]) - y)

    return [x, y, r]

def camera2(angles, aperture):
    """
    Reçoit en paramètre les angles du robot (dictionnaire), retourne la position des coins
    de l'image projetés à 2m, sauf si ils intersectent le sol
    """

    M = direct(angles)
    P = M.dot(np.array([0., 0., 0., 1.]).T)
    
    delta = (math.tan(aperture/2))*2
    V1 = M.dot(np.array([2., delta, delta, 1.]).T)
    V2 = M.dot(np.array([2., delta, -delta, 1.]).T)
    V3 = M.dot(np.array([2., -delta, -delta, 1.]).T)
    V4 = M.dot(np.array([2., -delta, delta, 1.]).T)

    res = [V1, V2, V3, V4]
    for k in range(len(res)):
        tmp = intersectFloor(P, res[k] - P)
        if tmp is not None:
            res[k] = tmp[0:3]
        else:
            res[k] = res[k][0:3]

    return res

def inverseTarget(x, y, z, yaw, pitch, roll):
    M = T(x,y,z,multiplier=1.).dot(Rz(yaw).dot(Ry(pitch).dot(Rx(roll))))

    return M

def points(M):
    P = M.dot(np.array([0., 0., 0., 1.]).T)[:3]
    P1 = M.dot(np.array([0.1, 0., 0., 1.]).T)[:3]
    P2 = M.dot(np.array([0., 0.1, 0., 1.]).T)[:3]
    P3 = M.dot(np.array([0., 0., 0.1, 1.]).T)[:3]

    return [P, P1, P2, P3]

def inverse(targets, x, y, z, yaw, pitch, roll):
    M = inverseTarget(x, y, z, yaw, pitch, roll)
    targetPoints = points(M)

    def inverseScore(X):
        joints = {'motor'+str(k+1): X[k] for k in range(6)}
        currentPoints = points(direct(joints))
        return sum([np.linalg.norm(targetPoints[k] - currentPoints[k]) for k in range(len(currentPoints))])

    X = [targets[x] for x in targets]
    s = time.time()
    Y = minimize(inverseScore, X, method='Nelder-Mead', options={'fatol': 0.001})

    return {'motor'+str(k+1): Y.x[k] for k in range(6)}

