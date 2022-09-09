import numpy as np

# cf https://rhoban.github.io/reperes/python2d

def rotation(alpha):
    return np.array([[np.cos(alpha), -np.sin(alpha), 0.],
                     [np.sin(alpha),  np.cos(alpha), 0.],
                     [           0.,             0., 1.]])

def translation(x, y):
    return np.array([[1., 0., x],
                     [0., 1., y],
                     [0., 0., 1.]])

def frame(alpha, x, y):
    return translation(x, y) @ rotation(alpha)

def transform(T, x, y):
    return (T @ [x, y, 1])[:2]

def frame_inv(T):
    R = T[:2, :2] # On extrait la rotation
    t = T[:2, 2:] # On extrait la translation
    upper = np.hstack((R.T, -R.T @ t))
    lower = np.array([0., 0., 1.])
    return np.vstack((upper, lower))
