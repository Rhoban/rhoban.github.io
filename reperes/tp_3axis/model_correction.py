import math
from scipy.optimize import minimize
import numpy as np

bx = 0.07
bz = 0.25
l1 = 0.085
l2 = 0.185
l3 = 0.250

def direct(joints):
    """
    Reçoit en paramètre la position des articulations du robot, retourne
    la position du bout de l'effecteur
    """

    global l1, l2, l3, bx, bz

    P = np.array([math.cos(joints['motor2']), 0., math.sin(joints['motor2'])]) * l2
    P += np.array([math.cos(joints['motor2'] - joints['motor3']), 0., math.sin(joints['motor2'] - joints['motor3'])]) * l3

    P += np.array([l1, 0., 0.])
        
    return [
        bx + P[0]*math.cos(-joints['motor1']) - P[1]*math.sin(-joints['motor1']),
        P[0]*math.sin(-joints['motor1']) + P[1]*math.cos(-joints['motor1']),
        bz + P[2] 
    ]

def alKashi(c, a, b):
    return math.acos(min(1, max(-1, (a**2 + b**2 - c**2)/(2*a*b))))

def inverse(x, y, z):
    """
    Reçoit en paramètre une position cible, retourne la position des moteurs
    pour atteindre cette position cible
    """

    global l1, l2, l3

    x -= bx
    z -= bz

    alpha1 = -math.atan2(y, x)

    D = math.sqrt(x*x + y*y) - l1
    d = math.sqrt(D**2 + z**2)

    beta = math.asin(z/d)
    gamma = alKashi(l3, l2, d)
    alpha2 = gamma + beta

    theta = alKashi(d, l2, l3)
    alpha3 = math.pi - theta

    return [alpha1, alpha2, alpha3]

def inverseIterative(x, y, z):
    """
    Reçoit en paramètre une position cible, retourne la position des moteurs
    pour atteindre cette position cible

    Ici, on utilisera une fonction de score et scipy.minimize au lieu du modèle
    analytique
    """
    P = np.array([x,y,z])

    def score(X):
        d = direct({'motor1': X[0], 'motor2': X[1], 'motor3': X[2]})
        return np.linalg.norm(d-P)

    Y = minimize(score, [0., 0., 0.])

    return Y.x

def trianglePoints(x, z, h, w):
    """
    Reçoit les paramètres géométriques du triangle, retourne la position des
    trois points du triangle
    """
    return [
        [x, 0, h+z], [x, -w/2, z], [x, w/2, z]
    ]

def triangle(x, z, h, w, t):
    """
    Reçoit les paramètres géométriques du triangle, déplace le bout du robot le long
    du triangle
    """

    points = trianglePoints(x, z, h, w)

    # Sélection de deux points
    P1 = np.array(points[(int(t)) % 3])
    P2 = np.array(points[(int(t) + 1) % 3])
    
    # Interpolation entre les deux points
    T = math.fmod(t, 1)
    pos = P2*T + (1-T)*P1

    return inverse(pos[0], pos[1], pos[2])

def circlePoints(x, z, r, N=16):
    """
    Retourne N points qui approximent un cercle de rayon r en position (x,z)
    """

    points = []
    delta = math.pi*2/N
    for segment in range(N):
        points.append([x, math.cos(delta*segment)*r, z + math.sin(delta*segment)*r])
    
    return points

def circle(x, z, r, t, duration):
    """
    Retourne les angles afin que le bout de l'effecteur suive un cercle donné par
    les points ci-dessus
    """

    N = 16
    points = circlePoints(x, z, r, N)

    # Sélection de deux points
    part = int(math.fmod(t, duration)*N/duration)
    P1 = np.array(points[part])
    P2 = np.array(points[(part+1) % N])
    
    # Interpolation entre les deux points
    T = math.fmod(t, duration / N) / (duration / N)
    pos = P2*T + (1-T)*P1

    return inverse(pos[0], pos[1], pos[2])