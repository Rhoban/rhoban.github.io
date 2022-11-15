import numpy as np
import pinocchio as pin

model = [
    # Axis            Relative position
    [[0.0, 0.0, 1.0], [0.0, 0.0, 0.0]],
    [[0.0, 1.0, 0.0], [0.32, 0.0, 0.68]],
    [[0.0, 1.0, 0.0], [0.0, 0.0, 0.975]],
    [[1.0, 0.0, 0.0], [0.0, 0.0, 0.2]],
    [[0.0, 1.0, 0.0], [0.887, 0.0, 0.0]],
    [[1.0, 0.0, 0.0], [0.2, 0.0, 0.0]],
]

screw_axises = []
M = np.eye(4)
for axis, relative_position in model:
    M[:3, 3] += relative_position
    screw_motor = np.array([0.0, 0.0, 0.0, *axis])
    screw_axises.append(pin.SE3(M).toActionMatrix() @ screw_motor)


def fk_jacobian(thetas):
    T = np.eye(4)
    J = []
    for screw_axis, theta in zip(screw_axises, thetas):
        J.append(pin.SE3(T).toActionMatrix() @ screw_axis)
        T = T @ pin.exp6(screw_axis * theta)
    T = T @ M
    J = np.vstack(J).T

    return T, J


def inverse_target(x, y, z, yaw, pitch, roll):
    T = pin.exp6(np.array([x, y, z, 0.0, 0.0, 0.0]))
    T = T * pin.exp6(np.array([0.0, 0.0, 0.0, 0.0, 0.0, yaw]))
    T = T * pin.exp6(np.array([0.0, 0.0, 0.0, 0.0, pitch, 0.0]))
    T = T * pin.exp6(np.array([0.0, 0.0, 0.0, roll, 0.0, 0.0]))
    return T.np


def ik(thetas, T_world_target):
    T, J = fk_jacobian(thetas)
    error = pin.log6(T_world_target @ pin.SE3(T).inverse().np)
    return np.array(thetas) + np.linalg.pinv(J) @ error
