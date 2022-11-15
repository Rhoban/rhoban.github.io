import math
import time
import numpy as np
from onshape_to_robot import simulation
from colorama import Fore, Back, Style
from transforms3d.quaternions import mat2quat, quat2mat
from transforms3d.axangles import axangle2mat
import pybullet as p
import pygame
import argparse
import control
import model

sim = simulation.Simulation("6axis/robot.urdf", fixed=True, panels=True)
parser = argparse.ArgumentParser()
parser.add_argument("--mode", "-m", type=str, default="test")
args = parser.parse_args()
sliders = {}
target = None


def resetBasePositionWithMatrix(target, T):
    R = T[0:3, 0:3]
    T = T.T[3, :3]
    Q = mat2quat(R)
    p.resetBasePositionAndOrientation(target, list(T), [Q[1], Q[2], Q[3], Q[0]])


if args.mode == "direct":
    target = p.loadURDF("frame/robot.urdf")
elif args.mode == "laser":
    target = p.loadURDF("target/robot.urdf")
elif args.mode == "direct_tool":
    target = p.loadURDF("frame/robot.urdf")
    tool = p.loadURDF("tool/robot.urdf")
elif args.mode == "board":
    tool = p.loadURDF("tool/robot.urdf")
    tool_target = p.loadURDF("frame/robot.urdf")
    board_target = p.loadURDF("frame/robot.urdf")

    T_world_board = np.eye(4)
    T_world_board[:3, 3] = [1.5 + np.random.uniform(-0.25, 0.25), 0.0, 1.0 + np.random.uniform(-0.25, 0.25)]
    T_world_board[:3, :3] = axangle2mat([0.0, 1.0, 0.0], -np.pi / 2 + np.random.uniform(-0.4, 0.4)) @ axangle2mat(
        [0.0, 0.0, 1.0], -np.pi / 2
    )
    resetBasePositionWithMatrix(board_target, T_world_board)
elif args.mode == "camera" or args.mode == "camera2":
    target = p.loadURDF("target2/robot.urdf")
    sliders["target_x"] = p.addUserDebugParameter("target_x", -2, 2, 1)
    sliders["target_y"] = p.addUserDebugParameter("target_y", -2, 2, 0)
    sliders["target_z"] = p.addUserDebugParameter("target_z", -2, 2, 0)
    sliders["aperture"] = p.addUserDebugParameter("aperture", 5, 95, 60)

    imgSize = 200
    pygame.init()
    window = pygame.display.set_mode((imgSize, imgSize))
    pygame.display.set_caption("Camera")

joints = sim.getJoints()
if args.mode == "board":
    pass
elif args.mode in ["inverse", "inverse_control"]:
    sliders["target_x"] = p.addUserDebugParameter("target_x", -2, 2, 1.5)
    sliders["target_y"] = p.addUserDebugParameter("target_y", -2, 2, 0)
    sliders["target_z"] = p.addUserDebugParameter("target_z", 0, 2, 1)
    sliders["target_yaw"] = p.addUserDebugParameter("target_yaw", -math.pi, math.pi, 0)
    sliders["target_pitch"] = p.addUserDebugParameter("target_pitch", -math.pi, math.pi, 0)
    sliders["target_roll"] = p.addUserDebugParameter("target_roll", -math.pi, math.pi, 0)

    target = p.loadURDF("frame/robot.urdf")
else:
    for joint in joints:
        sliders[joint] = p.addUserDebugParameter(joint, -math.pi, math.pi, 0.0)

lastLine = time.time()
lastInverse = 0
targets = {"r" + str(k + 1): 0 for k in range(6)}

while True:
    if sim.t > 1.0:

        joints = sim.getJoints()
        if args.mode not in ["inverse", "inverse_control", "board"]:
            for joint in joints:
                targets[joint] = p.readUserDebugParameter(sliders[joint])

        if args.mode == "direct":
            T = model.direct(list(targets.values()))
            resetBasePositionWithMatrix(target, T)

        if args.mode == "direct_tool":
            T = model.direct(list(targets.values()))
            resetBasePositionWithMatrix(tool, T)
            T = model.direct_tool(list(targets.values()))
            resetBasePositionWithMatrix(target, T)

        elif args.mode == "laser":
            pos = model.laser(list(targets.values()))
            if pos is not None:
                m = model.direct(list(targets.values()))
                T = m.T[3, :3]
                p.resetBasePositionAndOrientation(target, [pos[0], pos[1], 0.0], [0, 0, 0, 1])

                if time.time() - lastLine > 0.1:
                    lastLine = time.time()
                    p.addUserDebugLine(list(T), [pos[0], pos[1], 0.0], [1.0, 0.0, 0.0], 1, 0.15)

        elif args.mode == "camera" or args.mode == "camera2":
            target_x = p.readUserDebugParameter(sliders["target_x"])
            target_y = p.readUserDebugParameter(sliders["target_y"])
            target_z = p.readUserDebugParameter(sliders["target_z"])
            aperture = p.readUserDebugParameter(sliders["aperture"])
            pos = [target_x, target_y, target_z]
            p.resetBasePositionAndOrientation(target, pos, [0, 0, 0, 1])
            view = model.camera(list(targets.values()), pos, imgSize, np.deg2rad(aperture))

            window.fill((200, 200, 200))
            pygame.draw.line(window, (150, 150, 150), (imgSize / 2, 0), (imgSize / 2, imgSize), 1)
            pygame.draw.line(window, (150, 150, 150), (0, imgSize / 2), (imgSize, imgSize / 2), 1)
            pygame.draw.circle(window, (150, 0, 0), (int(view[0] + imgSize / 2), int(imgSize / 2 - view[1])), int(view[2]))
            pygame.display.flip()

            if args.mode == "camera2" and time.time() - lastLine > 0.5:
                lastLine = time.time()
                corners = model.camera2(list(targets.values()), np.deg2rad(aperture))
                for corner in corners:
                    if corner is not None:
                        m = model.direct(list(targets.values()))
                        T = m.T[3, :3]
                        p.addUserDebugLine(list(T), list(corner), [0.0, 0.0, 1.0], 1, 0.55)
                attach = ((0, 1), (1, 2), (2, 3), (3, 0))
                for entry in attach:
                    if corners[entry[0]] is not None and corners[entry[1]] is not None:
                        p.addUserDebugLine(list(corners[entry[0]]), list(corners[entry[1]]), [0.0, 0.0, 1.0], 1, 0.55)

        elif args.mode == "inverse" or args.mode == "inverse_control":
            x = p.readUserDebugParameter(sliders["target_x"])
            y = p.readUserDebugParameter(sliders["target_y"])
            z = p.readUserDebugParameter(sliders["target_z"])
            yaw = p.readUserDebugParameter(sliders["target_yaw"])
            pitch = p.readUserDebugParameter(sliders["target_pitch"])
            roll = p.readUserDebugParameter(sliders["target_roll"])

            if args.mode == "inverse":
                T = model.inverseTarget(x, y, z, yaw, pitch, roll)
            else:
                T = control.inverse_target(x, y, z, yaw, pitch, roll)
            resetBasePositionWithMatrix(target, T)

            if (time.time() - lastInverse) > 0.05:
                lastInverse = time.time()
                if args.mode == "inverse":
                    values = model.inverse(list(targets.values()), x, y, z, yaw, pitch, roll)
                else:
                    values = control.ik(list(targets.values()), T)
                targets = {"r" + str(k + 1): values[k] for k in range(6)}
        elif args.mode == "board":
            T_world_effector = model.direct(list(targets.values()))
            resetBasePositionWithMatrix(tool, T_world_effector)

            T_world_tool = model.direct_tool(list(targets.values()))
            resetBasePositionWithMatrix(tool_target, T_world_tool)

            T_world_effectorTarget = model.board(T_world_board, sim.t)
            values = control.ik(list(targets.values()), T_world_effectorTarget)
            targets = {"r" + str(k + 1): values[k] for k in range(6)}

            def touches_board(point_world):                
                point_board = np.linalg.inv(T_world_board) @ [*point_world, 1]
                return abs(point_board[2]) < 5e-3

            
            tool_world = T_world_tool[:3, 3]
            T_world_tool2 = model.direct_tool(list(targets.values()))
            tool_world2 = T_world_tool2[:3, 3]

            if touches_board(tool_world) and touches_board(tool_world2):
                print("Segment touching the board")
                p.addUserDebugLine(tool_world[:3], tool_world2, [0., 1., 0.], 5., 10.)
            else:
                print("Not touching the board")
            

        sim.resetJoints(targets)

    sim.tick()
