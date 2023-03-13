import numpy as np

# Cf: https://rhoban.github.io/reperes/python3d

def translation(x, y, z):
    return np.array([[1, 0, 0, x],
                     [0, 1, 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0, 1]])

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

def frame_inv(T):
    R = T[:3, :3] # On extrait la rotation
    t = T[:3, 3:] # On extrait la translation
    upper = np.hstack((R.T, -R.T @ t))
    lower = np.array([0., 0., 0., 1.])
    return np.vstack((upper, lower))
